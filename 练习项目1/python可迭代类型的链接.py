#-*- coding=utf-8 -*-
#并行链接zip()
#串行链接 itertools.chain
from itertools import chain
#原始数据
print("---------原始数据----------")
a=[1,2,3,4,5,6]
b=('a','b','c','d')
c="ABCD"
print(a)
print(b)
print(c)
print("---------并行数据----------")
d=zip(a,b,c)
print(d)
for x,y,z in d:
    print(x,y,z)
print("---------串行数据----------")
e=chain(a,b,c)
print(e)
for i in e:
    print(i)

