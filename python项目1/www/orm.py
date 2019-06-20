#coding=utf-8
import asyncio,logging,aiomysql

def log (sql,args=()):
    logging.info('SQL:%s' % sql)

#创建数据库连接池，优点不用频繁的打开数据库
async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    #global语句是被用来声明是全局的变量
    global _pool
    _pool=await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        mixsize=kw.get('mixsize',1),
        loop=loop
    )

#创建执行select语句
async def select(sql,args,size=None):
    log(sql,args)
    # global _pool
    with (await _pool) as conn:
        cur=await conn.cursor(aiomysql.DictCursor)
        # 查询的返回格式会变成字典格式
        await cur.execute(sql.replace('?','%s'),args or ())
        # mysql中的占位符是?,所以用?来替代 '%s'
        if size:
            rs=await cur.fetchmany(size)
        else:
            rs=await cur.fetchall()
        # 如果传入size参数，就通过fetchmany()获取最多指定数量的记录，否则，通过fetchall()获取所有记录。
        await cur.close()
        logging.info('rows returned:%s'%len(rs))
        return rs

#创建执行insert，update，delete语句的通用函数
async def execute(sql,args):
    log(sql)
    with (await _pool) as conn:
        try:
            cur=await conn.cursor()
            await cur.execute(sql.replace('?','%s'),args)
            #不返回结果集，返回结果数
            affected=cur.rowcount
            await cur.close()
        except BaseException as e:
            raise
        return affected
def create_args_string(num):
    L=[]
    for n in range(num):
        L.append('?')
        return ','.join(L)


class ModelMetaclass(type):
    def __new__(cls, name, basrs,attrs):
        #排除Model类本身：
        if name=='Model':
            return type.__new__(cls, name, basrs,attrs)
        #获取table的名称
        tableName=attrs.get('_table_',None) or name
        logging.info('found model :%s (table :%s)'%(name,tableName))
        #获取所有的Field的主建名
        mappings=dict()
        primarykey=None
        fields=[]
        for k,v in attrs.iteam():
            if isinstance(v,Field):
                logging.info('found mapping :%s ==> %s' %(k,v))
                mappings[k]=v
                if v.primary_key:
                    #找到主键
                    if primarykey:
                        raise RuntimeError('Duplicate primary key for field :%s' %k)
                    primarykey=k
                else:
                    fields.append(k)
        if not primarykey:
            raise RuntimeError('Primary key not found')

        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields=list(map(lambda f :'`%s`' % f,fields))
        attrs['_mappings_']=mappings #保存属性跟列的映射关系
        attrs['_table_']=tableName
        attrs['_primary_key_']=primarykey
        attrs['_fields_']=fields
        #构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs['_select']='select `%s`,%s from `%s` '%(primarykey,','.join(escaped_fields),tableName)
        attrs['_insert_']='insert into `%s` (%s,%s) values (%s)' % (tableName,','.join(escaped_fields),primarykey,create_args_string(len(escaped_fields)+1))
        attrs['_update_']='update `%s` set %s where %s =?'%(tableName,','.join(map(lambda f:'`%s`=?'%(mappings.get(f).name or f),fields)),primarykey)
        attrs['_delete_']='delete from `%s` where `%s`=?' %(tableName,primarykey)
        return type.__new__(cls, name, basrs,attrs)




#定义所有orm映射的基类Model
class Model(dict,metaclass=ModelMetaclass):

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Model object has no attribute '%s' " %key )
    def __setattr__(self, key, value):
        self[key]=value

    def getvalus(self,key):
        return getattr(self,key,None)

    def getValusOrDefault(self,key):
        valus=getattr(self,key,None)
        if valus is None:
            field=self._mappings_[key]
            if field.default is not None:
                valus=field.default() if callable(field.default) else field.default
                logging.debug('using default valus for %s:%s'%(key,str(valus)))
                setattr(self,key,valus)
        return valus

#Field类及其子类
class Field(object):
    def __init__(self,name,column_type,primary_key,default):
        self.name=name
        self.column_type=column_type
        self.primary_key=primary_key
        self.default=default

    def __str__(self):
        return '<%s,%s:%s>' %(self.__class__.name,self.column_type,self.name)

class StringField(Field):
    def __init__(self,name=None,primary_key=False,default=None,ddl='varchar(100)'):
        super().__init__(name,ddl,primary_key,default)
class BooleanField(Field):
    def __init__(self,name=None,default=False):
        super().__init__(name,'boolean',False,default)
class IntergeField(Field):
    def __init__(self,name=None,primary_key=False,default=0):
        super().__init__(name,'bigint',primary_key,default)
class FloatField(Field):
    def __init__(self,name=None,primary_key=False,default=0.0):
        super().__init__(name,'real',primary_key,default)
class TextField(Field):
    def __init__(self,name=None,default=None):
        super().__init__(name,'text',False,default)


class Model(dict):

    ...

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ## find objects by where clause
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        ## find number by select and where
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        ## find object by primary key
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

#创建Model类的实例
class Model(dict):
    ...
    async def save(self):
        args=list(map(self.getValusOrDefault,self._fields_))
        args.append(self.getValusOrDefault(self._primary_key_))
        rows=await execute(self._insert_,args)
        if rows !=1:
            logging.warn("failed to insert recode : affected rows :%s"% rows)


    async def update(self):
        args=list(map(self.getValus,self._fields_))
        args.append(self.getValus(self._primary_key_))
        rows=await execute(self._update_,args)
        if rows !=1:
            logging.warn("failed to update recode : affected rows :%s"% rows)

    async def remove(self):
        args=[self.getValus(self._primary_key_)]
        rows=await execute(self._delete_,args)
        if rows !=1:
            logging.warn("failed to delete recode : affected rows :%s" % rows)
            