# -*- coding:utf-8 -*-
# author by lihh

'''组织测试用例,运行测试程序'''
import smtplib
from email.mime.text import MIMEText
import os
import time
from BSTestRunner import *
import unittest
from function import *
from test_login import LoginTest
from email.header import Header
from process_alter import Process

def test_suite():
    # 存放报告的文件夹
    dir_path = os.path.abspath('.')
    report_dir = dir_path + '\\report'
    test_dir = dir_path + '\\src\\test\\case\\UI\\'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")
    discover.addTest(unittest.makeSuite(Process))
    # 报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告文件完整路径
    report_name = report_dir + '\\' + now + 'result.html'

    # 打开文件在报告文件写入测试结果
    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title="Test Report", description="test case result")
        runner.run(discover)
    f.close()
    latestreport = latest_report(report_dir)
    send_mail(latestreport)

if __name__ == '__main__':
    test_suite()
