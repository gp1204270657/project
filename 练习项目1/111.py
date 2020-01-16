# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url="http://oa.mwbyd.cn"
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\test'}
options.add_experimental_option('prefs', prefs)

def login():
    driver = webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Programs\Python\Python36\chromedriver.exe', chrome_options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("login-password").click()
    time.sleep(0.5)
    driver.find_element_by_id("username").send_keys("15607483181")
    driver.find_element_by_id("password").send_keys("1993119323aA")
    driver.find_element_by_id("loginBtn1").click()
    time.sleep(0.5)
    driver.find_element_by_link_text("销售").click()
    # time.sleep(1000)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/button[2]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='form-search']/div[6]/div[2]/select/option[4]").click()
    time.sleep(0.5)
    driver.find_element_by_name("search[start_time]").send_keys("2019-10-1")
    driver.find_element_by_name("search[end_time]").send_keys("2019-10-27")
    driver.find_element_by_name("search[end_time]").send_keys(Keys.ENTER)
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='dosearch']").click()
    time.sleep(0.5)
    driver.find_element_by_id("exportOrder").click()
    time.sleep(4)

if __name__ == '__main__':
    login()
