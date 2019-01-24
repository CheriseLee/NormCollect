from selenium import webdriver
#启动浏览器驱动


def browser():
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Ie()
    # driver = webdriver.PhantomJS()
    return driver


if __name__ == '__main__':
    browser()
