import json
import requests
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from HtmlTestRunner import HTMLTestRunner


# 返回实例
#runner = unittest.TextTestRunner()
# 指定测试报的路径
# 自动搜索项目根目录下的所有case，构造测试集；返回TestSuite对象
test_dir=os.path.join(os.getcwd())
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_sendMessage.py')
report_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'testData','data', "test-report.html")
fp = open(report_path, "wb")
runner = HTMLTestRunner(stream=fp,verbosity=2)
# 执行所有的用例
runner.run(discover)
# 关闭报告文件
fp.close()