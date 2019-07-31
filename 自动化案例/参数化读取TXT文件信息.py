#coding =utf-8

from selenium import webdriver
import os,time

source=open("D:\\abc\\data.txt","r")
values=source.readlines()
source.close()
for search in values:
    hw=webdriver.Chrome()
    hw.get("http://www.baidu.com")
    hw.find_element_by_id("kw").send_keys(search)
    hw.find_element_by_id("su").click()
    time.sleep(0.5)
    hw.quit()