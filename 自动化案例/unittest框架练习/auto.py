#coding=utf-8
from widget import Widget
import unittest#
#执行测试类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget=Widget()
    def testSize(self):

        self.assertEqual(self.widget.getsize(),(40,40))



    def tearDown(self):
        self.widget=None

if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(WidgetTestCase("testSize"))
    #
    # #执行测试
    # runner=unittest.TextTestRunner()
    # runner.run(suite)



