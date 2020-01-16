#coding=utf-8
import threading,_thread
from time import sleep,ctime
'''
我们应该避免使用thread 模块，原因是它不支持守护线程。当主线程退出时，所有的子线程不论它
们是否还在工作，都会被强行退出。有时我们并不期望这种行为，这时就引入了守护线程的概念。threading
模块则支持守护线程
'''
loops=[4,2]
def loop(nloop,nsec):
    print("start loop",nloop,"at",ctime())
    sleep(nsec)
    print("loop",nloop,"done at",ctime())
def maind():
    print("start at",ctime())
    threads=[]
    nloops=range(len(loops))

    #创建线程
    for i in nloops:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    #开始线程
    for i in nloops:
        threads[i].start()
    #等待所有线程结束
    for i in nloops:
        threads[i].join()
    print("all end",ctime())
if __name__ == '__main__':
    maind()