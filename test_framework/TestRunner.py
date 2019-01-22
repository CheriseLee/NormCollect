# -*- coding:utf-8 -*-
# author by lihh

'''组织测试用例,运行测试程序'''
import smtplib
from email.mime.text import MIMEText
import os
import time
from BSTestRunner import *
import unittest
from test_login import LoginTest
from email.header import Header

def test_suite():
    # 存放报告的文件夹
    dir_path = os.path.abspath('.')
    report_dir = dir_path + '\\report'
    test_dir = dir_path + '\\src\\test\\case\\UI\\'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")
    # 报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告文件完整路径
    report_name = report_dir + '\\' + now + 'result.html'

    # 打开文件在报告文件写入测试结果
    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title="Test Report", description="test case result")
        runner.run(discover)
    f.close()
if __name__ == '__main__':

    unittest.main()
    # latest_report = latest_report(report_dir)
    # send_mail(latest_report)



# def run_all_suite():
#     title = "鑫圣投资"
#     description = 'Web&Android端测试'
#     suite = unittest.TestSuite()
#
#     suite = suite(unittest.makeSuite(XSTZ_Web))
#     suite.addTest(unittest.makeSuite(XSTZ_Android))
#
#     with open(report_path, 'wb') as f:
#         runner = HTMLTestRunner(
#             f, verbosity=2, title=title, description=description)
#         runner.run(suite)
#
#
# def main():
#     run_all_suite()
#     Test_date = time.strftime('%Y-%m-%d %H:%M:%S')
#     Report_data = {"suite": {}}
#     suite_data = Android_data["suite"]
#     s = Web_data["suite"]
#     suite_data.update(s)
#     Report_data["report_url"] = report_url
#     Report_data["Test_date"] = Test_date
#     Report_data["suite"] = suite_data
#
#     send_email(report_path)


# if __name__ == "__main__":
#     main()
