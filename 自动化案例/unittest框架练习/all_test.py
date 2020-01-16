#coding=utf-8
import unittest
from test_case import baidu, youdao
import HTMLTestRunner
import time

testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
# 原始方法
# runner = unittest.TextTestRunner()
# runner.run(testunit)
#去当前时间戳
# print(time.time())
#取当前时间
# print(time.localtime())
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
# 运用html来做，加入当前的时间点
filename="D:\\abc\\"+now+'result.html'
fq=open(filename,"wb")
runner=HTMLTestRunner.HTMLTestRunner(
    stream=fq,
    title="测试报告",
    description="用例执行情况"
)
runner.run(testunit)
fq.close()
