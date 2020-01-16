#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
des_cap={}
des_cap['platformName']='Android'
des_cap['platformVersion']='8.0'
des_cap['deviceName']='Android Emulator'
des_cap['appPackage']='com.puscene.client'
des_cap['appActivity']='.activity.WelcomeActivity_'
dvicers=webdriver.Remote('http://localhost:4723/wd/hub',des_cap)
dvicers.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
dvicers.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(3)
TouchAction(dvicers).press(x=833,y=1479).move_to(x=355,y=1484).perform()


dvicers.find_element_by_id("com.puscene.client:id/guideStartButton").click()