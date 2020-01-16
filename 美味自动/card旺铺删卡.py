# -*- coding=utf-8 -*-
from selenium import webdriver
from untillpackge import Login,fengzhuang
import time
drivers=webdriver.Chrome()
url="http://card.test.cn/index.php?m=&&m=&c=index&a=index"
find=fengzhuang.Find
# 调用登录模块来登录
Login.login(drivers,url)

find.xpath(drivers,"//*[@id='J_tmenu']/li[3]/a").click()
time.sleep(0.5)
find.xpath(drivers,"//*[@id='J_lmenu']/ul[1]/li[1]/a").click()
drivers.switch_to_frame('rframe_62')
time.sleep(0.2)
m=drivers.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr/td/div/select[1]")
m.find_element_by_xpath("//*[@value='shopid']").click()
find.name(drivers,"keyword").send_keys(215531)
time.sleep(0.2)
find.name(drivers,"search").click()
time.sleep(0.2)
find.xpath(drivers,"/html/body/div[3]/div[1]/table/tbody/tr[6]/td[19]/a[2]").click()
time.sleep(0.2)
m=drivers.find_element_by_xpath("//*[@id='searchform']/table/tbody/tr/td/div/select[1]")
m.find_element_by_xpath("//*[@value='mobile']").click()
find.name(drivers,"keyword").send_keys(13636561554)
time.sleep(0.5)
find.ID(drivers,"btn-search").click()