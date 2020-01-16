#-*- coding=utf-8 -*-
import unittest,HTMLTestRunner
import time


def run_all():
    cace_dir = "D:\Desktop\case"
    testsuite=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(
        cace_dir,
        pattern="test_*.py",
        top_level_dir=None
    )

    for case in discover:
        # for test_Case in case:
        testsuite.addTest(case)

    return testsuite
if __name__ == '__main__':

    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    filename=r"D:\\abc\\"+now+'result.html'
    fq=open(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fq,
        title="用力报告",
        description="用例执行情况"
    )
    runner.run(run_all())
    fq.close()

# listaa=r'D:\Desktop\case'
# def creatsuitel():
#     testunit=unittest.TestSuite()
#     discover=unittest.defaultTestLoader.discover(listaa,
#                                                 pattern ='test_*.py',
#                                                 top_level_dir=None)
# #discover 方法筛选出来的用例，循环添加到测试套件中
#     print(discover)
#     for test_suite in discover:
#         for test_case in test_suite:
#             testunit.addTests(test_case)
#             print(testunit)
#     return testunit
# alltestnames = creatsuitel()
# now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
# filename = 'D:\\abc\\'+now+'result.html'
# fp = open(filename, 'wb')
# runner =HTMLTestRunner.HTMLTestRunner(
#                                         stream=fp,
#                                         title=u'百度搜索测试报告',
#                                         description=u'用例执行情况：')
# #执行测试用例
# runner.run(alltestnames)