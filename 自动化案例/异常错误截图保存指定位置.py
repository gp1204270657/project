#coding=utf-8
from selenium import webdriver
hw=webdriver.Chrome()
hw.get("http://www.baidu.com")
try:
    hw.find_element_by_id("kwdd").send_keys("hah")
    hw.find_element_by_id("su").click()
except:
    #通过get_screenshot_as_file方法保存错误位置的截图到指定位置
    hw.get_screenshot_as_file("D:\\abc\\error_png\\error.png")
hw.quit()