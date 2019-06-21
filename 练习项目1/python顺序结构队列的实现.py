#-*- coding=utf-8 -*-
#顺序储存队列的python实现

class Queue(object):

    def __init__(self,length):
        self.queue=[]
        self.length=length

    def en_queue(self,e):
        #判读是否满了，是则删掉先进入的，对后进入的插进去
        if len(self.queue)>=self.length:
            # del self.queue[0]
            self.queue.pop(0)
            self.queue.append(e)
        else:
            self.queue.append(e)

        #如果不为空，删掉第一个数字，为空返回error
    def de_queue(self):
        if len(self.queue):
            del self.queue[0]
        else:
            print("error")

q=Queue(3)

q.en_queue(1)
print(q.queue)

q.en_queue(2)
print(q.queue)

q.en_queue(3)
print(q.queue)

q.en_queue(4)
print(q.queue)

q.en_queue(5)
print(q.queue)

q.de_queue()
print(q.queue)