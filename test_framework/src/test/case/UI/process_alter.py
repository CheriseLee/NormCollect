from selenium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
from selenium.webdriver.support import select
driver = webdriver.Firefox()
class Process:

    def updateNormItem():

        sleep(2)
        driver.get("http://47.98.217.90:9010/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_class_name("loginbtn").click()

        driver.find_element_by_class_name("m-xs").click()
        proSelect = select.Select(driver.find_element_by_css_selector("[id='trade']"))
        proSelect.select_by_visible_text("测试")
        # driver.find_element_by_css_selector("[class='btn btn-primary btn-sm '],[text='更新子目']").click()
        # driver.find_element_by_css_selector("[class='layui-layer-btn0'],[text='确定']").click()

        driver.find_element_by_id("treeDemo_4_span").click()
        # driver.find_element_by_class_name("trbg").
        # driver.find_element_by_css_selector("[data-index=1]").is_selected()
        # startTime = time()
        #等待进度条消失

        # WebDriverWait(driver, 2000, 5, NoSuchElementException).until_not(aa())
        # print(driver.find_element_by_css_selector("[class='btn btn-primary btn-sm '],[text='更新子目']"))
        # #WebDriverWait(driver, 2000, 5, NoSuchElementException).until(expected_conditions.element_to_be_clickable("[class='btn btn-primary btn-sm '],[text='更新子目']"))
        #
        # endTime = time()
        # totalTime=endTime-startTime
        # print(totalTime)

    def test_1del_process(self):
        driver.get("http://47.98.217.90:9010/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_class_name("loginbtn").click()

        driver.find_element_by_class_name("m-xs").click()
        proSelect = select.Select(driver.find_element_by_css_selector("[id='trade']"))
        proSelect.select_by_visible_text("测试")

        driver.find_element_by_css_selector("#treeDemo_4_span").click()
        driver.find_element_by_link_text("材料").click()
        # driver.find_element_by_link_text("人工").click()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[2]').click()
        table = driver.find_element_by_css_selector("#materiallist")
        # 通过标签名获取表格中的所有行对象
        trList = table.find_elements_by_tag_name("tr")
        #assert len(trList) == 2, "表格行数不符！"
        # 遍历表格行对象

            # 获取每一行中所有列对象
        for key in trList:
             key.find_elements_by_tag_name("td")[0].click()
            # 遍历表格列对象
        # 断言获取的表格行数是否等于预期
        sleep(2)

        driver.quit()





if __name__ == '__main__':
    # updateNormItem()
    Process().test_1del_process()