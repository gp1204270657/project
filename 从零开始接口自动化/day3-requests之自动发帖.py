#coding=utf-8
import requests

#获取博客园的链接

# r1=requests.get("https://www.cnblogs.com/nesson/")
# print(r1.status_code)
# print(r1.text)

par={
    "w":"youyouketang"
}
r2=requests.get("http://zzk.cnblogs.com/s/blogpost",params=par)
print(r2.status_code)
print(r2.text)