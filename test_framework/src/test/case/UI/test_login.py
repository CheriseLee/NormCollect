# -*- coding:utf-8 -*-
# author by lihh
import unittest
import os
import yaml
import myunit,drivers,function
from LoginPage import *
from selenium.common.exceptions import NoSuchElementException

current_path = os.path.dirname(__file__)#使用不同py文件保证引文的文件路径固定

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        print('test login1_ normal is start run...')
        po = LoginPage(self.driver)
        dir_path = os.getcwd()
        print(dir_path)
        path1 = os.path.abspath('')
        print(path1)
        path2 = os.path.abspath('login_info.yml')
        print(path2)
        f = open(current_path + "\\login_info.yml", 'r')
        datas = yaml.load(f)
        for key in datas['userlist']:
            po.login_action(key['username'], key['password'])
        sleep(3)
        f.close()
        assert (self.driver.find_element_by_class_name("m-xs").is_displayed() == True)
        print("test_login1_normal is test end!")

    # def test_login2_error(self):
    #     'username is ok,password is error'
    #     print('test login_password Error is start run...')
    #     po = LoginPage(self.driver)
    #     dir_path = os.getcwd()
    #     f = open(dir_path + "\\login_info.yml", 'r')
    #     datas = yaml.load(f)
    #     for key in datas['erroruserlist']:
    #         po.login_action(key['username'], key['password'])
    #     sleep(3)
    #     f.close()
    #
    #     # self.assertEqual(po.type_loginFail_hint(), '')
    #     # function.insert_img(self.driver, "51zxw_login2_fail.png")
    #     assert (self.driver.find_element_by_id("username").is_displayed() == True)
    #     print("test_login2_passwordError is test end!")
    #
    # def test_login_empty(self):
    #     '''username and password is empty'''
    #     print('test login3_empty is start run...')
    #     po = LoginPage(self.driver)
    #     po.login_action('', '')
    #     sleep(3)


        # self.assertEqual(po.type_loginFail_hint(), '')
        # function.insert_img(self.driver, "51zxw_login3_empty.png")
        print("test_login3_empty is test end!")


if __name__ == '__main__':
    unittest.main()








# REPORT_URL = Config().get("report_url")
# now = time.strftime("%Y%m%d%H%M", time.localtime())
# report_name = "report_%s.html" % (now)
# report_path = os.path.join(REPORT_PATH, report_name)
# report_url = REPORT_URL % report_name  # 重新定义report_url
#
#
# def get_func_name():  # 一个辅助函数用来获取当前运行的函数名
#     return inspect.stack()[1][3]
#
#
# @ddt.ddt
# class XSTZ_TEST(unittest.TestCase):
#     result = ["Success", "Fail"]
#     URL = Config().get('URL')
#     USERNAME = Config().get('USERNAME')
#     PWD = Config().get('PWD')
#     Test_date = time.strftime('%Y-%m-%d %H:%M:%S')
#     data = {"suite": {},
#             "Test_date": Test_date,
#             "report_url": report_url
#             }
#
#
#
#     def bypass_auth(self):  # 绕过验证码--添加cookie
#         driver = self.driver
#         driver.add_cookie(
#             {'name': u'logintoken',
#              'value': u'eyJBY2NvdW50Ijo1MjAwMDMxMiwiRXhwIjoxNTE5NTI0ODUwOTEzL\
#              CJMb2dpblR5cGUiOjAsIkFwcGx5IjoicGMiLCJOYW1lIjoi5rWL6K%2BV6a2P5bC\
#              P5LicIn0%3D.ZWFrZjRMcTh0alRxdjB5US9qTTB0dm5mL2h5eVRZdnduWFpDa0s0\
#              bkdVd1ZCUm5oRjJlcHZSRExrNkd4a2lGR0czY0JKWkVhWUM4OVd3eFEwMzI2eGpq\
#              WXlnWFp4aGdSR1FEc0JpbWZNVm9yY0l0ajMwQ2w1UExEeW5NMzhuYVlTSWZHVWl0\
#              Z2pKYUtxYm9OeHpUMjVWb2hSanB1NFBnZi9NRlZpOXpOUDFZPQ%3D%3D'}
#         )
#         driver.add_cookie({'name': 'XSMCFX_UC_ACCOUNT',
#                            'value': '=%2052000312%20'})
#         return driver
#
#     def test_xsmcfx_login(self):
#         """ XSTZ登录"""
#         test_action = get_func_name()  # 获取当前测试行为，以测试函数命名规范获取
#         LoginPage = XSTZLoginPage(self.driver)  # 登录页面
#         Website = LoginPage.page_title  # 解析服务器地址
#
#         LoginPage.login(self.USERNAME, self.PWD)  # 输入登录用户名，密码,登录
#         LoginPage.sleep(2)  # 等待页面加载
#         msg_account = LoginPage.get_msg_accout  # 获得欢迎信息，账户信息
#
#         # LoginPage.logout  # 账户退出
#         # logger.info("Account logout!")
#
#         try:
#             assert msg_account[0] == '欢迎您！'
#             result = self.result[0]
#             ReturnCode = 0
#             print("Test Success")
#             logger.info("测试成功！")
#             format_logger = ' ' * 43
#             logger.info(
#                 "{4}！\n{0}- 测试账户：{1}\n{2}- 服务器地址:{3}".format(format_logger, msg_account[1], format_logger, Website,
#                                                              result))
#         except Exception as e:
#             print("Test fail.{}".format(str(e)))
#             result = self.result[1]
#             ReturnCode = 1
#             logger.error("Test Fail！Reason:{}".format(str(e)))
#
#         finally:
#             data = {test_action: {"Website": Website,
#                                   "login_account": msg_account[1],
#                                   "Test_date": self.Test_date,
#                                   "result": result,
#                                   "ReturnCode": ReturnCode
#                                   }
#                     }
#             self.data["suite"].update(data)
#
#     def test_injection_page(self):
#         '''注资页面跳转'''
#         test_action = get_func_name()
#         try:
#             JPage = InjectionPage(self.driver)  # 网上存款页面类
#             JPage.click_injection_button
#             JPage.into_bank_page
#             n = JPage.get_payway_number
#             bank_detail = JPage. get_payway_detail1
#
#             assert n
#             result = self.result[0]
#             ReturnCode = 0
#             print("Test Success!\n ")
#             print("当前可用支付通道数目：{}\n".format(n))
#             print("通道明细：{}".format(bank_detail))
#
#         except Exception as e:
#             print(str(e))
#             result = self.result[1]
#             ReturnCode = 1
#             logger.error("Test Fail! Reason:{}".format(e))
#         finally:
#             data = {test_action: {"result": result,
#                                   "ReturnCode": ReturnCode
#                                   }
#                     }
#             self.data["suite"].update(data)
#
#     def test_payment_channel1(self):
#         '''支付通道1跳转'''
#         money = Config().get("money")
#         test_action = get_func_name()
#         try:
#             CS = ChannelSelect(self.driver).select
#             DPage = CS(self.driver)
#             PaywayName = DPage.get_payway_name(cn=1)  # 选择第一个支付通道，获取
#             DPage.sumbit(money)  # 提交
#             bank_handle = DPage.exchange_bank_page
#             element = DPage.is_element_exist
#             DPage.close_bank_page(bank_handle)
#             DPage.return_payment_page
#
#             assert element
#
#             print("Test Success! ")
#             print("Test PayWay:{}".format(PaywayName))
#             result = self.result[0]
#             ReturnCode = 0
#             logger.info("第三方支付跳转成功")
#         except Exception as e:
#             print(str(e))
#             result = self.result[1]
#             ReturnCode = 1
#             logger.error("Test Fail! Reason:{}".format(e))
#         finally:
#             time.sleep(1)
#             data = {test_action: {"result": result,
#                                   "ReturnCode": ReturnCode
#                                   }
#                     }
#             self.data["suite"].update(data)
#
#     def test_payment_channel2(self):
#         '''支付通道2测试'''
#         test_action = get_func_name()
#         money = Config().get("money")
#         try:
#             CS = ChannelSelect(self.driver).select
#             DPage2 = CS(self.driver)
#
#             PaywayName = DPage2.get_payway_name(cn=0)
#             Banklist, Bank_dic, Test_bank = DPage2.get_bank_detail
#             DPage2.sumbit(money)
#             bank_handle = DPage2.exchange_bank_page
#             DPage2.close_bank_page(bank_handle)
#             DPage2.return_payment_page
#
#             assert bank_handle
#             print("Test Success! ")
#             print("Test PayWay:{}".format(PaywayName))
#             print("Test BankName:{}".format(Test_bank))
#             print("Available banks:{}".format(Banklist))
#             print(Bank_dic)
#             result = self.result[0]
#             ReturnCode = 0
#             logger.info("第三方支付跳转成功")
#         except Exception as e:
#             result = self.result[1]
#             ReturnCode = 1
#             logger.error("Test Fail! Reason:{}".format(e))
#         finally:
#             time.sleep(1)
#             data = {test_action: {"result": result,
#                                   "ReturnCode": ReturnCode
#                                   }
#                     }
#             self.data["suite"].update(data)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         data = cls.data
#         insert_influxdb(data)
#         ding_report(**data)
#
#
# if __name__ == '__main__':
#     # unittest.main()
#     title = "鑫圣投资"
#     description = 'Web端测试'
#     test_suite = unittest.TestSuite()
#
#     test_suite.addTest(unittest.makeSuite(XSTZ_TEST, "test_xsmcfx_login"))
#     test_suite.addTest(unittest.makeSuite(XSTZ_TEST, "test_injection_page"))
# #     test_suite.addTest(unittest.makeSuite(XSTZ_TEST, "test_payment_channel1"))
# #     test_suite.addTest(unittest.makeSuite(XSTZ_TEST, "test_payment_channel2"))
#
#     with open(report_path, 'wb') as f:
#         runner = HTMLTestRunner(
#             f, verbosity=2, title=title, description=description)
#         runner.run(test_suite)
