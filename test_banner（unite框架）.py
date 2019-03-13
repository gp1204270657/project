from selenium import webdriver
import unittest,time

class Bannner(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="http://www.yuexing.com"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_banner(self):
        """首页的banner图片"""
        driver=self.driver
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        driver.find_element_by_link_text("立即进入").click()
        # 清除所有的cookie
        driver.delete_all_cookies()
        # 通过查尔斯抓包工具获取的登陆后cookie的变化来记录并添加到cookie中，来实现登录
        driver.add_cookie({"name": 'AHSESS', 'value': '99d4ghk352hd4mqo7dqvigi095'})
        driver.add_cookie({"name": 'pc_bazaar_shortdomain', 'value': 'sh'})
        driver.add_cookie({"name": 'user_lat', 'value': '31.24916171'})
        driver.add_cookie({"name": 'user_lng', 'value': '121.48789949'})
        driver.add_cookie({"name": 'tempcookid', 'value': '595c5150bebd33533d85d6de34d36a74'})
        driver.add_cookie( {"name": 'Hm_lvt_b80587b2e0c6e8cc2da0183796d6e6e7', 'value': '1520563331, 1522309021, 1522371437'})
        driver.add_cookie({"name": 'Hm_lpvt_0cab8be8d73e44819d9a5782a1ee9fa8', 'value': '1522721748'})
        driver.add_cookie({"name": 'Hm_lvt_0cab8be8d73e44819d9a5782a1ee9fa8', 'value': '1522285569,1522372454,1522631362,1522717574'})
        driver.add_cookie({"name": 'qinqin_open', 'value': '1'})
        driver.add_cookie({"name": 'im_open', 'value': '1'})
        driver.add_cookie({"name": 'behaviourID', 'value': '52de45eb6d0e0c5475806e408702c286'})
        driver.add_cookie({"name": 'prams', 'value': '%7B%22qudao%22%3A%22pcbanner%22%7D'})
        driver.add_cookie({"name": '_adwp', 'value': '245730818.9086087553.1520560682.1521429223.1522200271.4'})
        driver.add_cookie({"name": 'reserve_mobile', 'value': '13636561554'})
        driver.add_cookie({"name": 'region', 'value': 'sh'})
        driver.get(self.url)
        time.sleep(2)
        #获取当前的窗口
        home1=driver.current_window_handle
        time.sleep(0.5)
        #点击第一个bunner
        driver.find_element_by_xpath("//*[@id='banner']/div/div[4]/span[1]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='banner']/div/div[1]/div[2]/a/img").click()
        time.sleep(1)
        #获取所有的浏览器窗口
        allwindows=driver.window_handles
        for banner1 in allwindows:
            if banner1!=home1:
                #切换到banner1的窗口页面
                driver.switch_to_window(banner1)
                time.sleep(0.5)
                js="$(window).scrollTop(500)"
                driver.execute_script(js)
                time.sleep(1)
                js1= "$(window).scrollTop(100000)"
                driver.execute_script(js1)
                time.sleep(1)
                driver.close()
        #切换到首页
        time.sleep(1)
        driver.switch_to_window(home1)
        driver.refresh()
        # 点击第二个bunner
        home2 = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='banner']/div/div[4]/span[2]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='banner']/div/div[1]/div[3]/a/img").click()
        time.sleep(1)
        # 获取所有的浏览器窗口
        allwindows = driver.window_handles
        for banner2 in allwindows:
            if banner2 != home2:
                # 切换到banner1的窗口页面
                driver.switch_to_window(banner2)
                time.sleep(0.5)
                js = "$(window).scrollTop(500)"
                driver.execute_script(js)
                time.sleep(0.5)
                js1 = "$(window).scrollTop(100000)"
                driver.execute_script(js1)
                time.sleep(1)
                driver.close()
        driver.switch_to_window(home2)
        driver.refresh()
        # 点击第三个bunner
        home3 = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='banner']/div/div[4]/span[3]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='banner']/div/div[1]/div[4]/a/img").click()
        time.sleep(1)
        # 获取所有的浏览器窗口
        allwindows = driver.window_handles
        for banner3 in allwindows:
            if banner3 != home3:
                # 切换到banner1的窗口页面
                driver.switch_to_window(banner3)
                time.sleep(0.5)
                js = "$(window).scrollTop(500)"
                driver.execute_script(js)
                time.sleep(0.5)
                js1 = "$(window).scrollTop(100000)"
                driver.execute_script(js1)
                time.sleep(1)
                driver.close()
        # 切换到首页
        driver.switch_to_window(home3)
        driver.refresh()
        time.sleep(1)
        # 点击第四个bunner
        home4=driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='banner']/div/div[4]/span[4]").click()

        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='banner']/div/div[1]/div[5]/a/img").click()
        time.sleep(1)
        # 获取所有的浏览器窗口
        allwindows = driver.window_handles
        for banner4 in allwindows:
            if banner4 != home4:
                # 切换到banner1的窗口页面
                driver.switch_to_window(banner4)
                time.sleep(0.5)
                js = "$(window).scrollTop(500)"
                driver.execute_script(js)
                time.sleep(0.5)
                js1 = "$(window).scrollTop(100000)"
                driver.execute_script(js1)
                time.sleep(1)
                driver.close()
        # 切换到首页
        driver.switch_to_window(home4)
        driver.refresh()
        time.sleep(1)
        # 点击第五个bunner
        home5=driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='banner']/div/div[4]/span[5]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='banner']/div/div[1]/div[6]/a/img").click()
        time.sleep(1)
        # 获取所有的浏览器窗口
        allwindows = driver.window_handles
        for banner5 in allwindows:
            if banner5 != home5:
                # 切换到banner1的窗口页面
                driver.switch_to_window(banner5)
                time.sleep(0.5)
                js = "$(window).scrollTop(500)"
                driver.execute_script(js)
                time.sleep(0.5)
                js1 = "$(window).scrollTop(100000)"
                driver.execute_script(js1)
                time.sleep(1)
                driver.close()
        # 切换到首页
        driver.switch_to_window(home5)
        time.sleep(1)




    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == '__main__':
    unittest.main()