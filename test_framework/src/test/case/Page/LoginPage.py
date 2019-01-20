from BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    #首页登录
    url = ''
    #封装定位器
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    submit_loc = (By.CLASS_NAME, 'loginbtn')

    #用户名输入框元素
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #密码输入框元素
    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def login_action(self, username, password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    # loginPass_loc = (By.LINK_TEXT, '我的空间')
    # loginFail_loc = (By.NAME, 'username')
    #
    # def type_login_pass_hint(self):
    #      return self.find_element(*self.loginPass_loc).text
    #
    # def type_login_fail_hint(self):
    #      return self.find_element(*self.loginFail_loc).text


