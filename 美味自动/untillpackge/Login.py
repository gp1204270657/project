# -*- coding=utf-8 -*-
from selenium import webdriver
import time
# 登录通用模块
def login(driver,url):
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("login-password").click()
    time.sleep(0.5)
    driver.find_element_by_id("username").send_keys("13636561554")
    driver.find_element_by_id("password").send_keys("gaopeng+-0312")
    driver.find_element_by_id("loginBtn1").click()
    time.sleep(1)