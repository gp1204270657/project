from random import randint


#生成一个随机字典
d={x:randint(60,100) for x in 'ABcdrf'}
#zip可以将里面的参数合并为一个元祖
z=zip(d.values(),d.keys())
#用sorted（）来进行降序排序
s=sorted(z,reverse=True)
print(s)

#通过部分条件来进行排序
data={x:randint(-10,10) for x in range(10,21)}
dict={k:v for k,v in data.items() if v>0}
print(dict)