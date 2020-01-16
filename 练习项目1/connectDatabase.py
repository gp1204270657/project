#codint=utf-8
import pymysql
#打开数据库连接
db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='test'
)
#适用cursor（）方法创建一个游标对象cur
cur=db.cursor()
#适用execute执行查询
cur.execute("select * from user")

#适用fetchall()方法获取查询结果
data=cur.fetchall()

print(data)

db.close()