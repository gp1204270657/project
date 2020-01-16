#coding=utf-8
import threading,_thread
from time import sleep,ctime
from apply import apply
loops=[4,2]
class ThreadFunc(object):
    def __init__(self,func,args,name=""):
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        apply(self.func,self.args)


def loop(nloop,nsec):

