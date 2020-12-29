"""
author :Rain
Date : 2019/07/14
Description :获取测试报告
"""
import os
import time
import unittest

from constant import BASE_DIR
from tools_fj.HTMLTestRunnerCN import HTMLTestReportCN
from utils_fj.file_utils import FileUtils


# 配置要测试的脚本

def get_report():
    report_file = BASE_DIR + os.sep + 'report'
    case_file = BASE_DIR + os.sep + 'case_api_auto' + os.sep, 'test*'
    FileUtils.clear_file(report_file)
    print(case_file)
    suite = unittest.defaultTestLoader.discover(*case_file)
    timestr = time.strftime('%Y-%m-%d_%H%M%S')
    with open(report_file + os.sep + 'testReport_{}.html'.format(timestr), 'wb') as f:
        runner = HTMLTestReportCN(stream=f, verbosity=2, title='饭角接口测试报告', description='', tester='rain')
        runner.run(suite)


if __name__ == '__main__':
    get_report()
