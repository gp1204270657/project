#-*- coding =utf-8 -*-
from itertools import islice
class PintNum(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isWhiteNum(self,num):
        if num==2:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    def __iter__(self):
        for i in range(self.start,self.end+1):
            if self.isWhiteNum(i):
                yield i

p=PintNum(1,100)
for i in p:
    print(i)
#如何对迭代器进行切片操作
#from itertools import islice
'''
islice(iteable,stop)
islice(iteable,start,stop,step=1) ->islice object
'''
print("----------------对迭代器进行切片----------------")
a=islice(p,1,5)
for x in a:
    print(x)