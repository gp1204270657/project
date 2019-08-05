# -*- coding=utf-8-*-
import HTMLTestRunner,unittest,time
from selenium import webdriver

class BaiDu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="https://www.baidu.com"
        self.verificationErrors=[]
        self.accept_next_alert=True
    def test_baidu_search(self):
        driver=self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys("nihao")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

'''
无法生成HTML解决方法
方法一：
在main()方法下方以unittest运行就无法生成测试报告,需要在上方以
文件名运行科生成报告（这步操作需要在Edit Config..添加Python目录下的路径，而不是python test）
方法二：
alt+Shift+F10 快捷键运行此文件即可
'''
if __name__ == '__main__':
    #定义一个测试容器
    suite=unittest.TestSuite()
    suite.addTest(BaiDu("test_baidu_search"))
    #定义一个报告存放路径位置
    filename="D:\\abc\\result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索报告',
        description=u'用例执行情况'
    )
    runner.run(suite)
    fp.close()