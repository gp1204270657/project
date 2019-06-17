# coding=utf-8
class Field(object):
    # 初始化是获得二个参数，变成私有属性
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

#将Field转换为字符串时将返回 Field:xxx，XXX为传入的名字
    def __str__(self):
        return '< %s : %s >' % (self.__class__.__name__, self.name)


#创建StingField，自动调用父类的初始化方式
class StringField(Field):

    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntergeField(Field):
    def __init__(self,name):
        super(IntergeField,self).__init__(name,'bigint')

#创建元类
class ModelMetaclass(type):
    def __new__(cls, name, bases,attrs):
        if name=='Model1':
            return  type.__new__(cls, name, bases,attrs)
        print('Found model :%s' %name)
        #创建一个新的字典
        mapping=dict()
        #将每一个类的属性，通过.items()遍历其键值对。如果值是Field类，则打印键值，并将这一对键值绑定到mapping字典上
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s ==> %s ' %(k,v))
                mapping[k]=v
        #将刚刚传入值为Field类的属性删除
        for k in mapping.keys():
            attrs.pop(k)
        #创建一个专门的__mappings__属性，保存字典mapping
        attrs['__mapping__']=mapping
        #创建一个专门的__table__属性，保存传入的类的名称
        attrs['__table__']=name
        return type.__new__(cls, name, bases,attrs)

#一生二
class Model1(dict,metaclass=ModelMetaclass):
    def __init__(self,**kwargs):
        super(Model1,self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        set[key]=value

    #模拟建表注册
    def save(self):
        field=[]
        args=[]
        for k,v in self.__mapping__.items():
            field.append(v.name)
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' %(self.__table__,','.join(field),','.join([str(i) for i in args]))
        print('SQL:%s '%sql)
        print('ARGS:%s'% str(args))


class user(Model1):
    id=IntergeField('idh')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')

u=user(id=12345,name='clack',email='1204270657@qq.com',password='123123')
u.save()