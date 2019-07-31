#coding=utf-8
from selenium import webdriver
import time
url="http://m.mail.10086.cn"
bs=webdriver.Chrome()
bs.maximize_window()
bs.get(url)
time.sleep(1)
bs.find_element_by_id("txtUser").send_keys("13636561554")
time.sleep(0.5)
bs.find_element_by_id("txtPass").send_keys("Gaopeng0312")
bs.find_element_by_id("loginBtn").click()
time.sleep(1)
bs.find_element_by_partial_link_text("彩云网盘").click()
time.sleep(1)
bs.switch_to_frame('diskDev')
time.sleep(1)
bs.find_element_by_id("uploadFileInput").send_keys("D:\\test\image.jpg")
time.sleep(1)
# bs.find_element_by_id("createDir").click()


