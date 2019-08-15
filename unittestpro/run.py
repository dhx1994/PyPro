# 引入包
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 实例化类
testcases = unittest.defaultTestLoader.discover('cases','test_*.py')

# 实例化testsuite方法，并将测试用例加载到测试用例集中
testsuits = unittest.TestSuite()
testsuits.addTests(testcases)

# 运行测试用例，并生成测试报告
title  = "测试报告"
descr = '猫宁生鲜的测试报告'
file_path = "./reports/morning.reports.html"

with open(file_path,'wb') as f:
    runner = HTMLTestRunner(stream = f,title = title,description = descr)
    runner.run(testsuits)