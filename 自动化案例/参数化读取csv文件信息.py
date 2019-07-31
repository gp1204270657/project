#coding=utf-8
import csv
my_file="D:\\abc\\canshu.csv"
#新建的xles文件需要另存为csv文件才可以，且需要用记事本打开，设置为utf-8格式保存后，方可生效
data=csv.reader(open(my_file,'r',encoding='utf-8'))
for user in data:
    print(user[0])
    print(user[1])
    print(user[2])
