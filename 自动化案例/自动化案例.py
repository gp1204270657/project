# coding = utf-8
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains
import time,os
bs=webdriver.Chrome()
# -----------------------------------下拉滚动条操作---------------------------------------------
# bs.maximize_window()
# bs.get("http://www.baidu.com")
# bs.find_element_by_id("kw").send_keys("selenium")
# bs.find_element_by_id("su").click()
# time.sleep(2)
# # 将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# bs.execute_script(js)
# print(1)
# time.sleep(3)
# # 将滚动条移动到页面的顶部
# js_="var q=document.documentElement.scrollTop=0"
# bs.execute_script(js_)
# print(2)
# time.sleep(3)
# bs.quit()
# -----------------------------------调用js操作---------------------------------------------
# bs.maximize_window()
# js_file=os.path.abspath("F:\/js.html")
# bs.get(js_file)
# # bs.implicitly_wait(10)
# bs.execute_script('$("#tooltip").fadeOut();')
#
# time.sleep(5)
# button = bs.find_element_by_class_name('btn')
# bs.execute_script('$(arguments[0]).fadeOut()',button)
# time.sleep(2)

# -----------------------------------上传文件操作---------------------------------------------
# update_file=os.path.abspath("F:\/update_file.html")
# bs.maximize_window()
# bs.get(update_file)
# time.sleep(1)
#找到上传的按钮直接使用send_key方法放入文件的路径即可
# bs.find_element_by_name("file").send_keys("F:\WeGame\data.txt")
# time.sleep(2)

# -----------------------------------下拉框选择处理----------------------------------------------
# bs.maximize_window()
# path=os.path.abspath("F:\/option.html")
# bs.get(path)
# time.sleep(2)
#找到下拉框的父选框
# father=bs.find_element_by_id("ShippingMethod")
#找到下拉的子菜单
# son=father.find_element_by_xpath("//*[@id='ShippingMethod']/option[4]")
# time.sleep(1)
# son.click()
# time.sleep(1)
# bs.quit()

# -----------------------------------alert/confirm/prompt 处理----------------------------------------------
# bs.maximize_window()
# url="http://www.baidu.com"
# bs.get(url)
# bs.find_element_by_link_text(u"设置").click()
# time.sleep(1)
# son=bs.find_element_by_class_name("setpref")
#模拟鼠标移动
# ActionChains(bs).move_to_element(son).perform()
# son.click()
# time.sleep(1)
# bs.find_element_by_class_name("prefpanelgo").click()
# alert=bs.switch_to_alert()
# time.sleep(2)
# test=alert.text
# print(test)
# alert.accept()
# -----------------------------------浏览器多窗口处理-----------------------------------------------
# url="http://www.yuexing.com"
# bs.maximize_window()
# bs.get(url)
# time.sleep(1)
# bs.get(url)
# #获取首页的窗口
# home=bs.current_window_handle
# time.sleep(2)
# #打开样板间的窗口
# bs.find_element_by_xpath("//*[@id='nav']/div/div[2]/a[2]").click()
# #获得所有的窗口
# allwindow=bs.window_handles
# #循环遍历所有的窗口，如果不是首页的窗口，就进行操作
# for handles in allwindow:
#     if handles !=home:
#         #切换到样板间的窗口
#         bs.switch_to_window(handles)
#         #获取样板间的窗口
#         room = bs.current_window_handle
#         #对当前页面进行操作，打开新的窗口
#         bs.find_element_by_xpath("//*[@id='model-list-layout']/div[1]/div[1]/a/img").click()
#         #获取此时所有的窗口
#         allwindow2= bs.window_handles
#         #循环遍历此时所有的窗口，如果不是首页跟样板间的窗口，就关闭
#         for handles2 in allwindow2:
#             if handles2!=home and handles2!=room:
#                 #切换到最新的窗口页面，然后关掉
#                 bs.switch_to_window(handles2)
#                 time.sleep(2)
#                 bs.close()
#         time.sleep(3)
#         #再次切换到样板机的窗口，来关闭
#         bs.switch_to_window(room)
#         bs.close()
# #最后返回原来的首页
# bs.switch_to_window(home)
# time.sleep(2)
# bs.find_element_by_id("tt").send_keys(u"切换成功")
# time.sleep(2)
# bs.quit()

# -----------------------------------对话框的处理-----------------------------------------------
# bs.maximize_window()
# url="http://www.baidu.com"
# bs.get(url)
# bs.find_element_by_link_text(u"登录").click()
# time.sleep(3)
# #层级定位
# div=bs.find_element_by_class_name("tang-foreground").find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']")
# div.click()
# time.sleep(1)
# #层级定位找到下面的元素
# name=bs.find_element_by_class_name("tang-foreground").find_element_by_name("userName")
# name.send_keys(u"13636561554")
# password=bs.find_element_by_class_name("tang-foreground").find_element_by_name("password")
# password.send_keys("gaopeng+-0312")
# #层级定位找到下面的元素，并输入验证码
# time.sleep(10)
# sub=bs.find_element_by_class_name("tang-foreground").find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']")
# sub.click()

# -----------------------------------定位frame中的元素-----------------------------------------------
# #\f为特殊符号 前面需要加一个/转意符
# path='F:\/frame.html'
# file_path=os.path.abspath(path)
# bs.maximize_window()
# bs.get(file_path)
# bs.implicitly_wait(10)
# #先定位最外层的frame
# bs.switch_to_frame("f1")
# #再定位下一层的frame
# bs.switch_to_frame("f2")
# #之后就可以定位frame2下的元素的位置进行操作
# bs.find_element_by_xpath("//*[@id='kw']").send_keys("test")
# bs.find_element_by_id("su").click()
# time.sleep(2)
# bs.quit()
# url="http://www.yuexing.com"
# -----------------------------------分隔符层级定位的练习-----------------------------------------------
# bs.maximize_window()
# bs.get(url)
# time.sleep(1)
# bs.get(url)
# # 先找到层次定位的父位置
# father=bs.find_element_by_xpath("/html/body/div[1]/div[8]/div/div[1]/ol/li/a").click()
# # 在定位找到父位置下的子位置
# son=bs.find_element_by_xpath("/html/body/div[1]/div[8]/div/div[1]/ol/li/div").find_element_by_xpath("/html/body/div[1]/div[8]/div/div[1]/ol/li/div/div/div/div[3]/a")
# # 再把鼠标移动到子位置上
# time.sleep(2)
# ActionChains(bs).move_to_element(son).perform()
# bs.find_element_by_xpath("/html/body/div[1]/div[8]/div/div[1]/ol/li/div/div/div/div[3]/a").click()
# # bs.quit()

# -----------------------------------分隔符checkbox练习-----------------------------------------------
# 文件的路径
# path='F:\checkbox.html'
# 返回文件的绝对路径
# file_path=os.path.abspath(path)
# 返回文件名称
# file_name=os.path.basename(path)
# 浏览器最大化
# bs.maximize_window()
# bs.get(file_path)
# time.sleep(2)
# inputs=bs.find_elements_by_tag_name("input")
# for each in inputs:
#     if each.get_attribute('type')=='checkbox':
#         each.click()
# bs.find_element_by_name("1").click()

# ------------------------------------分隔符（键盘练习）------------------------------------------------
# 输入访问的地址
# bs.get("http://www.baidu.com")
# # 智能等待一面秒
# # bs.implicitly_wait(1)
# time.sleep(1)
# bs.find_element_by_id('kw').send_keys('selenium')
# time.sleep(1)
# bs.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# time.sleep(1)
# bs.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# bs.find_element_by_id('kw').send_keys(u'哈哈')
# time.sleep(1)
# bs.find_element_by_id("su").click()
# bs.get("http://www.youdao.com")
# ------------------------------------网页前进后退练习----------------------------------------------------
# 后退的页面
# bs.back()
# bs.implicitly_wait(1)
# time.sleep(1)
# 前进页面
# bs.forward()
# bs.implicitly_wait(1)
# time.sleep(1)
# 打印输入框的大小
# size=bs.find_element_by_id("kw").size
# print (size)
# 关闭浏览器
# bs.quit()


