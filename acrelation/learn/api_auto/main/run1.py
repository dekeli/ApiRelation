import unittest
from test_case import register
from test_case import register
import time
import HTMLTestRunner

time = time.strftime('%Y-%m-%d', time.localtime(time.time()))# 获取系统当前时间
report_path = "E:\\api_auto-master\\api_new\\api_auto\\report\\" + time + ".html"# 测试报告存放路径
suite = unittest.TestSuite()# 创建用例收集容器
ts = unittest.TestLoader()# 创建用例加载器

suite.addTests(ts.loadTestsFromModule(register))# 传入模块名（也可以传入模块名和类名，以测试用例的类为单位执行测试用例）
# suite.addTests(ts.loadTestsFromModule())
# suite.addTests(ts.loadTestsFromModule())
# suite.addTests(ts.loadTestsFromModule())
# suite.addTests(ts.loadTestsFromModule())








# runner = unittest.TextTestRunner()
with open(report_path, 'wb')as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title=u'自动化测试报告',
                                           description='测试者：syq'
                                           )
    runner.run(suite)
    print(report_path)
