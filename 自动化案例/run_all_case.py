# coding = utf-8
import unittest,HTMLTestRunner

def run_all():
    #执行测试用例的目录
    case_dir=r"D:\Desktop\case"

    #添加一个运行的容器
    testcase=unittest.TestSuite()
    #通过discover方法遍历以test开头的文件
    print(case_dir)
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='test_*.py',top_level_dir=None)

    for test_Suit in discover:
        testcase.addTest(test_Suit)
    #返回一个集合
    return testcase

if __name__ =="__main__":
    report_path=r"D:\abc\result.html"
    fp=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'这是测试',
                                         description=u"用例执行情况")
    runner.run(run_all())
    fp.close()
