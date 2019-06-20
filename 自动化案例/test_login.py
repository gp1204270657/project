from selenium import webdriver
import unittest, time


class YueXing(unittest.TestCase):

    def setUp(self):
       self.driver=webdriver.Chrome()
       self.url="http://www.yuexing.com"
       self.verificationErrors = []
       self.accept_next_alert = True

    def test_phoneLogin(self):
        """手机登录"""
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element_by_link_text("立即进入").click()
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_xpath("//*[@id='txt-phone']").send_keys("13636561554")
        driver.find_element_by_id("get_code_login").click()
        time.sleep(10)
        driver.find_element_by_id("fast_login").click()
        time.sleep(2)

    def test_passLogin(self):
        """密码登录"""
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

    def test_updatePass(self):
        """找回密码"""
        driver=self.driver
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element_by_link_text("立即进入").click()
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_class_name("normal-tab").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='other-link']/a").click()
        driver.find_element_by_id("mobile").send_keys("13636561554")
        time.sleep(4)
        driver.find_element_by_class_name("submit-btn").click()
        time.sleep(15)
        driver.find_element_by_class_name("submit-btn").click()
        driver.find_element_by_id("pass").send_keys("000000")
        driver.find_element_by_id("re_pass").send_keys("000000")
        driver.find_element_by_class_name("submit-btn").click()
        time.sleep(2)
        driver.find_element_by_link_text("预约设计师").click()
        time.sleep(1)
        driver.back()
        driver.find_element_by_link_text("完善个人信息").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
