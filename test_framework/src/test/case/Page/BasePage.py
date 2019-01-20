from time import sleep
from selenium import webdriver


class Page():
    #页面基础类
    def __init__(self, driver):
        self.base_url = 'http://47.98.217.90:9010/'
        self.driver = driver
        self.timeout = 10 #设置超时等待

    def _open(self, url):
        url_ = self.base_url + url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        # assert self.driver.current_url == url_, 'Did not land on %s'%url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
