from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest

class goods(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="http://www.yuexing.com"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_goods(self):
        driver=self.driver
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element_by_link_text("立即进入").click()
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_class_name("normal-tab").click()
        time.sleep(1)
        driver.find_element_by_name("user_name").send_keys("13636561554")
        time.sleep(1)
        driver.find_element_by_id("user_pas").send_keys("000000")
        time.sleep(1)
        driver.find_element_by_id("login").click()
        time.sleep(2)
        js1="$(window).scrollTop(2500)"
        driver.execute_script(js1)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='product']/div[2]/div[2]/div[1]/div/div/a[2]/span").click()
        time.sleep(1)
        driver.switch_to_alert().accept()
        time.sleep(1)
        #获取当前的浏览器窗口句柄
        now=driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='product']/div[2]/div[2]/div[1]/div/div/a[1]/span").click()
        time.sleep(2)
        #获取所有窗口
        allwindow=driver.window_handles
        for kf in allwindow:
            if kf !=now:
                driver.switch_to_window(kf)
                time.sleep(2)
                driver.close()
        driver.switch_to_window(now)

        now2 = driver.current_window_handle
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='product']/div[2]/div[2]/div[1]/div/a").click()
        time.sleep(2)
        allwindow2 = driver.window_handles
        for goodtest in allwindow2:
            if goodtest!=now2:
                #切换到商品详情页
                driver.switch_to_window(goodtest)
                time.sleep(1)
                # 点击咨询客服
                driver.find_element_by_link_text("咨询客服").click()
                time.sleep(1)
                allwindow3=driver.window_handles
                for zx in allwindow3:
                    if zx !=now2 and zx !=goodtest:
                        driver.switch_to_window(zx)
                        time.sleep(1)
                        driver.close()
                driver.switch_to_window(goodtest)
                time.sleep(1)
                driver.close()
        # time.sleep()
        driver.switch_to_window(now2)
        time.sleep(1)






    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)


if __name__ == '__main__':
    unittest.main()