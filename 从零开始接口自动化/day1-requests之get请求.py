#coding=utf-8
#导入库
import requests
#请求百度首页
# R=requests.get("https://www.baidu.com")
# par={"wd":"test"}
# R=requests.get("https://www.baidu.com",params=par)
R=requests.get("https://www.baidu.com")
print(R.encoding) #编码
print(R.content)  #返回内容自动解码
print(R.status_code) #响应码
print(R.text.title)
print(R.text)  #字符串方式的响应体，会自动根据响应头部的字符编码进行解码

print(R.headers) #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
print(R.cookies) #获取cookie
print(R.url)
print(R.json) #Requests中内置的JSON解码器

