# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url="http://oa.mwbyd.cn"
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("login-password").click()
    time.sleep(0.5)
    driver.find_element_by_id("username").send_keys("13636561554")
    driver.find_element_by_id("password").send_keys("gaopeng+-0312")
    driver.find_element_by_id("loginBtn1").click()
    time.sleep(1)
    driver.find_element_by_link_text("办公").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='admin-offcanvas']/div/ul/li[4]/a").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='Workflow_170']/li[1]/a").click()
    time.sleep(0.5)
    now = time.strftime("%Y-%m-%d", time.localtime())
    driver.find_element_by_id("title").send_keys(now + "工作日报")
    # 层级定位双重定位,先等位父级位置
    m = driver.find_element_by_id("type")
    # 在定位子级位置
    m.find_element_by_xpath("//*[@id='type']/option[2]").click()
    time.sleep(0.5)
    driver.find_element_by_class_name("select2-search__field").send_keys("王文娟")
    driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
    time.sleep(0.5)
    iframe = driver.find_element_by_class_name("ke-edit-iframe")
    driver.switch_to_frame(iframe)
    driver.find_element_by_class_name("ke-content").send_keys(
        "今日工作:" + '\n'
         # "1.测试旺铺0.99C版本会员中心迁移" + '\n'
         "1.测试旺铺0.99C版本会员中心迁移" + '\n' + '\n'
        "明天安排：" + '\n'
        "1.测试旺铺0.99C版本会员中心迁移")
    # 退出iframe,返回原来的页面进行操作
    driver.switch_to_default_content()
    driver.find_element_by_name("RELEASE").click()
    time.sleep(1)
    alter = driver.switch_to_alert()
    alter.accept()
    print("Successful")


if __name__ == '__main__':
    login()
