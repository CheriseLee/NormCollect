from selenium import webdriver
from time import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
from selenium.webdriver.support import select
import selenium.webdriver.support.expected_conditions as EC

class Process:

    def updateNormItem():

        sleep(2)
        driver = webdriver.Firefox()
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

    def test_001_del_process(self):
        #登录
        driver = webdriver.Firefox()
        driver.get("http://47.98.217.90:9010/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_class_name("loginbtn").click()
        #选择专业
        driver.find_element_by_class_name("m-xs").click()
        proselect = select.Select(driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        #选择目录树第一个节点
        driver.find_element_by_css_selector("#treeDemo_4_span").click()
        #选择节点下的子目
        normtable = driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[1:2]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            sleep(2)
        # driver.find_element_by_link_text("材料").click()
            driver.find_element_by_link_text("人工").click()

            table = driver.find_element_by_css_selector("#wordproce")
            # table = driver.find_element_by_css_selector("#materiallist")
            # 通过标签名获取表格中的所有行对象
            trlist = table.find_elements_by_tag_name("tr")
            t = len(trlist)
            print("t" + str(t))
            # 遍历表格行对象
            if t > 0:

                for i in range(t - 1, -1, -1):
                    #在获取table的行数时，总是会遇到StaleElementReferenceException异常，有解决方案如下：
                    # 捕捉异常StaleElementReferenceException，然后重新获取元素，此方法比较靠谱
                    trlist = table.find_elements_by_tag_name("tr")
                    trlist[i].find_elements_by_tag_name("td")[0].click()
                    driver.find_element_by_link_text("删除工序").click()
                    driver.find_element_by_css_selector(".layui-layer-btn0").click()
        driver.close()
        # driver.quit() 使用driver.quit()时，调用下一个方法时报错目标计算机积极拒绝，二者区别还没弄明白

    def test_002_add_process(self):
        # 登录
        driver = webdriver.Firefox()
        driver.get("http://47.98.217.90:9010/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_class_name("loginbtn").click()
        # 选择专业
        driver.find_element_by_class_name("m-xs").click()
        proselect = select.Select(driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        # 选择目录树第一个节点
        driver.find_element_by_css_selector("#treeDemo_4_span").click()
        # 选择节点下的子目
        normtable = driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[1:2]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            driver.find_element_by_link_text("人工").click()

            for i in range(4):
                driver.find_element_by_link_text("新增工序").click()
                # 跳转到弹出的frame框架
                iframe = driver.find_element_by_xpath("//iframe")
                driver._switch_to.frame(iframe)
                driver.find_element_by_xpath("//input[@name=\"procedurename\"]").send_keys("人工名称" + str(i))
                driver.find_element_by_xpath("//input[@name=\"procedureunit\"]").send_keys("人工单位" + str(i))
                driver.find_element_by_xpath("//input[@name=\"remark\"]").send_keys("人工备注" + str(i))
                driver._switch_to.parent_frame()
                driver.find_element_by_link_text('添加').click()
                sleep(1)
            driver.close()

    def test_003_upmove_process(self):
        # 登录
        driver = webdriver.Firefox()
        driver.get("http://47.98.217.90:9010/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_class_name("loginbtn").click()
        # 选择专业
        driver.find_element_by_class_name("m-xs").click()
        proselect = select.Select(driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        # 选择目录树第一个节点
        driver.find_element_by_css_selector("#treeDemo_4_span").click()
        # 选择节点下的子目
        normtable = driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[1:2]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            driver.find_element_by_link_text("人工").click()
            table = driver.find_element_by_css_selector("#wordproce")
            # 通过标签名获取表格中的所有行对象
            sleep(1)
            trlist = table.find_elements_by_tag_name("tr")
            ele = trlist[len(trlist)-1].find_elements_by_tag_name("td")[1]
            name = ele.text
            print(name)
            ele.click()

            driver.find_element_by_link_text("上移").click()
            #
            newtable = driver.find_element_by_css_selector("#wordproce")
            newtrlist = newtable.find_elements_by_tag_name("tr")
            ele1 = newtrlist[len(newtrlist) - 2].find_elements_by_tag_name("td")[1]
            name1 = ele1.text
            print(name1)
            assert name == name1
            driver.close()

if __name__ == '__main__':
    # updateNormItem()
    # Process().test_001_del_process()
    # sleep(100)
    # Process().test_002_add_process()
    Process().test_003_upmove_process()