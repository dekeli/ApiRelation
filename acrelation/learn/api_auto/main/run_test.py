import unittest
import os
import sys
import time
import HTMLTestRunner

now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
case_path = os.path.abspath("../test_case")
report_path = "E:\\api_auto\\report\\result.html"
print('1111'+report_path)

def run_case():
    discover = unittest.defaultTestLoader.discover(case_path)
    print(discover)

    return discover



if __name__ == '__main__':
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告模板'
                                           )
    run = unittest.TextTestRunner()
    # run.run(run_case())
    runner.run(run_case())
    fp.close()
