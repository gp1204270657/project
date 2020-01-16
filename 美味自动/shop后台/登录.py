#coding=utf-8
from selenium import webdriver
import time

# class JiLei():
#
#     def login(self):
bs = webdriver.Chrome()
url="http://shop.test.9now.net/bmanage/account/login?type="
bs.maximize_window()
time.sleep(0.5)
bs.get(url)
time.sleep(0.5)
bs.find_element_by_class_name("account-login").click()
time.sleep(0.5)
bs.find_element_by_name("username").send_keys("MWCSZAdmin")
bs.find_element_by_name("password").send_keys("mw123456")
time.sleep(8)
bs.find_element_by_class_name("mw-btn").click()






#
# if __name__ == '__main__':
#     JiLei().login()
