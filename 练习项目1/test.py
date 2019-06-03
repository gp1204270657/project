# coding=utf-8
from functools import reduce
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://news.baidu.com/"
driver.maximize_window()
time.sleep(2)
driver.get(url)
time.sleep(2)
driver.find_element_by_link_text("习近平这些重磅提醒要记牢").click()

# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 3, 5, 7, 9]))


# 杨辉三角
# def getYang():
#     L = [1]
#     a=1
#     while a<=10:
#         yield L
#         L.append(0)
#         L=[L[i-1]+L[i] for i in range(len(L))]
#         a+=1
#
# n=0
# result=[]
# for  t in getYang():
#     print(t)
#     result.append(t)
#     n=n+1
#     if n==10:
#         break

# 取回数
# def is_palindrome(n):
#     s_n = str(n)
#     print(s_n,s_n[::-1])
#     return s_n == s_n[::-1]
# output = filter(is_palindrome, range(10, 14))
# print('1~10000:', list(output))
