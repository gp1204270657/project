#coding=utf-8
import threading,_thread
from time import sleep,ctime
loops=[4,2]
def loop(nloop,nsec,lock):
    print("start loop",nloop,"at:",ctime())
    sleep(nsec)
    print("loop",nloop,"done at :",ctime())
    #解锁
    lock.release()
def main():
    print("start at: ",ctime())
    locks=[]
    nloops=range(len(loops))
    for i in nloops:
        lock=_thread.allocate_lock()
        #锁定
        lock.acquire()
        #追加到数组中
        locks.append(lock)
    #执行多线程
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print("all end",ctime())

if __name__ == '__main__':
    main()