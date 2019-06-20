#coding=utf-8

def insert_sort(lists):

    #冒泡排序法
    num=len(lists)
    for i in range(0,num):
        for x in range(i+1,num):
            if lists[x]<lists[i]:
                temp=lists[x]
                lists[x]=lists[i]
                lists[i]=temp
            print(lists)

    print("排序后：",lists)
insert_sort([9,4,3,1])
