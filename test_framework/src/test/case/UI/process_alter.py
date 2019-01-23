
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
from selenium.webdriver.support import select
from LoginPage import *
import myunit
import os

current_path = os.path.dirname(__file__)#使用不同py文件保证引文的文件路径固定

class Process(myunit.StartEnd):
    def updateNormItem():
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
        # 登录
        po = LoginPage(self.driver)
        po.login_action('admin', '1')
        #选择专业
        # 元素显式等待
        locator = (By.CLASS_NAME, 'm-xs')
        element = WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.presence_of_element_located(locator))
        element.click()
        proselect = select.Select(self.driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        #选择目录树第一个节点
        sleep(3)
        self.driver.find_element_by_css_selector("#treeDemo_4_span").click()
        #选择节点下的子目
        normtable = self.driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[1:2]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(self.driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            sleep(2)
            Process.del_worker_process(self)
            # Process.del_material_process(self)
            # Process.del_machine_process(self)



    def te1st_002_add_process(self):
        # 登录
        po = LoginPage(self.driver)
        po.login_action('admin', '1')
        # 元素显式等待
        locator = (By.CLASS_NAME, 'm-xs')
        print(type(locator))
        element = WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.presence_of_element_located(locator))
        print(type(element))
        element.click()
        # # 选择专业
        proselect = select.Select(self.driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        # # 选择目录树第一个节点//*[@id="treeDemo_4_span"]
        # locator1 = (By.XPATH,'//*[@id="treeDemo_4_span"]')
        # print(type(locator1))
        # # locator1 = (By.CLASS_NAME,'treeDemo_4_span')
        #
        # element = WebDriverWait(self.driver, 10, 2).until(expected_conditions.presence_of_element_located(locator1))
        # print(type(element))
        # element.click()
        #同一串代码firefox执行通过，但是chrome必须sleep/显式等待等不到
        sleep(3)
        self.driver.find_element_by_css_selector("#treeDemo_4_span").click()
        # 选择节点下的子目
        normtable = self.driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[1:2]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(self.driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            # Process.add_worker_process(self,'人工')
            #添加材料的语句firefox运行失败，提示客户端中断连接10053，google运行没问题
            # Process.add_material_process(self,'材料')
            Process.add_machine_process(self,'机械')


    def t1est_003_upmove_process(self):
        # 登录
        po = LoginPage(self.driver)
        po.login_action('admin', '1')
        # 元素显式等待
        locator = (By.CLASS_NAME, 'm-xs')
        element = WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.presence_of_element_located(locator))
        element.click()
        # # 选择专业

        proselect = select.Select(self.driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        # # 选择目录树第一个节点
        self.driver.find_element_by_css_selector("#treeDemo_4_span").click()
        # # 选择节点下的子目
        normtable = self.driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[1:2]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(self.driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            self.driver.find_element_by_link_text("人工").click()
            table = self.driver.find_element_by_css_selector("#wordproce")
            # 通过标签名获取表格中的所有行对象
            sleep(1)
            trlist = table.find_elements_by_tag_name("tr")
            ele = trlist[len(trlist)-1].find_elements_by_tag_name("td")[1]
            name = ele.text
            print(name)
            ele.click()

            self.driver.find_element_by_link_text("上移").click()

            newtable = self.driver.find_element_by_css_selector("#wordproce")
            newtrlist = newtable.find_elements_by_tag_name("tr")
            ele1 = newtrlist[len(newtrlist) - 2].find_elements_by_tag_name("td")[1]
            name1 = ele1.text
            print(name1)
            # assert name == name1

    def add_worker_process(self,worker):
        self.driver.find_element_by_link_text(worker).click()
        for i in range(4):
            self.driver.find_element_by_partial_link_text("新增工序").click()
            # 跳转到弹出的frame框架
            iframe = self.driver.find_element_by_xpath("//iframe")
            self.driver._switch_to.frame(iframe)
            self.driver.find_element_by_xpath("//input[@name=\"procedurename\"]").send_keys(worker + "名称" + str(i))
            self.driver.find_element_by_xpath("//input[@name=\"procedureunit\"]").send_keys(worker + "单位" + str(i))
            self.driver.find_element_by_xpath("//input[@name=\"remark\"]").send_keys(worker + "备注" + str(i))
            self.driver._switch_to.parent_frame()
            self.driver.find_element_by_link_text('添加').click()
            sleep(1)

    def add_material_process(self,material):
        self.driver.find_element_by_link_text("材料").click()
        for i in range(4):
            sleep(5)
            try:
                self.driver.find_element_by_xpath('//*[@id="tab-2"]/div/div[1]/a[1]').click()
            except(ConnectionAbortedError):
                print("ds")

            # self.driver.find_element_by_partial_link_text("新增材料").click()
            # locator = self.driver.find_element_by_xpath('//*[@id="tab-2"]/div/div[1]/a[1]')
            # element = WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.presence_of_element_located(locator))
            # element.click()
            # 跳转到弹出的frame框架
            iframe = self.driver.find_element_by_xpath("//iframe")
            self.driver._switch_to.frame(iframe)
            self.driver.find_element_by_xpath("//input[@name=\"description\"]").send_keys(material + "名称" + str(i))
            self.driver.find_element_by_xpath("//input[@name=\"unit\"]").send_keys(material + "单位" + str(i))
            self.driver.find_element_by_xpath("//input[@name=\"remark\"]").send_keys(material + "备注" + str(i))
            self.driver._switch_to.parent_frame()
            self.driver.find_element_by_link_text('添加').click()

    def add_machine_process(self,machine):
        sleep(3)
        self.driver.find_element_by_link_text('机械').click()
        for i in range(4):
            self.driver.find_element_by_partial_link_text("新增机械").click()
            # 跳转到弹出的frame框架
            iframe = self.driver.find_element_by_xpath("//iframe")
            self.driver._switch_to.frame(iframe)
            self.driver.find_element_by_xpath("//input[@name=\"description\"]").send_keys(machine + "名称" + str(i))
            self.driver.find_element_by_xpath("//input[@name=\"unit\"]").send_keys(machine + "单位" + str(i))
            self.driver.find_element_by_xpath("//input[@name=\"remark\"]").send_keys(machine + "备注" + str(i))
            self.driver._switch_to.parent_frame()
            self.driver.find_element_by_link_text('添加').click()
            sleep(1)

    def del_worker_process(self):
        self.driver.find_element_by_link_text("人工").click()
        table = self.driver.find_element_by_css_selector("#wordproce")
        # 通过标签名获取表格中的所有行对象
        trlist = table.find_elements_by_tag_name("tr")
        t = len(trlist)
        # 遍历表格行对象
        if t > 0:

            for i in range(t - 1, -1, -1):
                # 在获取table的行时，总是会遇到StaleElementReferenceException异常，有解决方案如下：
                # 捕捉异常StaleElementReferenceException，然后重新获取元素，此方法比较靠谱
                sleep(3)
                trlist = table.find_elements_by_tag_name("tr")
                sleep(3)
                trlist[i].find_elements_by_tag_name("td")[1].click()
                sleep(3)
                self.driver.find_element_by_link_text("删除工序").click()
                sleep(3)
                self.driver.find_element_by_css_selector(".layui-layer-btn0").click()
    # driver.quit() 使用driver.quit()时，调用下一个方法时报错目标计算机积极拒绝，二者区别还没弄明白

    def del_material_process(self):
        self.driver.find_element_by_link_text("材料").click()
        table = self.driver.find_element_by_css_selector("#materiallist")
        # 通过标签名获取表格中的所有行对象
        trlist = table.find_elements_by_tag_name("tr")
        t = len(trlist)
        # 遍历表格行对象
        if t > 0:
            for i in range(t - 1, -1, -1):
                # 在获取table的行时，总是会遇到StaleElementReferenceException异常，有解决方案如下：
                # 捕捉异常StaleElementReferenceException，然后重新获取元素，此方法比较靠谱
                sleep(3)
                trlist = table.find_elements_by_tag_name("tr")
                sleep(3)
                trlist[i].find_elements_by_tag_name("td")[0].click()
                sleep(3)
                self.driver.find_element_by_link_text("删除材料").click()
                sleep(3)
                self.driver.find_element_by_css_selector(".layui-layer-btn0").click()
    def del_machine_process(self):
        self.driver.find_element_by_link_text("机械").click()
        table = self.driver.find_element_by_css_selector("#mechanicallist")
        # 通过标签名获取表格中的所有行对象
        trlist = table.find_elements_by_tag_name("tr")
        t = len(trlist)
        # 遍历表格行对象
        if t > 0:
            for i in range(t - 1, -1, -1):
                # 在获取table的行时，总是会遇到StaleElementReferenceException异常，有解决方案如下：
                # 捕捉异常StaleElementReferenceException，然后重新获取元素，此方法比较靠谱
                sleep(3)
                trlist = table.find_elements_by_tag_name("tr")
                sleep(3)
                trlist[i].find_elements_by_tag_name("td")[0].click()
                sleep(3)
                self.driver.find_element_by_link_text("删除机械").click()
                sleep(3)
                self.driver.find_element_by_css_selector(".layui-layer-btn0").click()

if __name__ == '__main__':
    # updateNormItem()
    Process().test_001_del_process()
    # Process().test_002_add_process()
    # Process().test_003_upmove_process()