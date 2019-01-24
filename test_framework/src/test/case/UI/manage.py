import myunit
from LoginPage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException,StaleElementReferenceException


class Manage(myunit.StartEnd):
    def test_002_del_taskInfo(self):
        # 登录
        po = LoginPage(self.driver)
        po.login_action('admin', '1')
        # 元素显式等待
        lst = self.driver.find_elements_by_css_selector('.m-xs')
        lst[1].click()
        # # # 选择专业
        proselect = select.Select(self.driver.find_element_by_css_selector("[id='trade']"))
        proselect.select_by_visible_text("测试")
        # # # 选择目录树第一个节点//*[@id="treeDemo_4_span"]
        # # 同一串代码firefox执行通过，但是chrome必须sleep/显式等待等不到
        sleep(3)
        self.driver.find_element_by_css_selector("#treeDemo_4_span").click()
        normtable = self.driver.find_element_by_css_selector("table#dataTable>tbody")
        normlist = normtable.find_elements_by_tag_name("tr")
        for norm in normlist[2:3]:
            element = norm.find_elements_by_tag_name("td")[0]
            action = ActionChains(self.driver)
            doubclick = action.double_click(element)
            doubclick.perform()
            # Manage.del_taskInfo(self)
            Manage.add_worker_info(self)

    def del_taskInfo(self):
        sleep(3)
        table = self.driver.find_element_by_xpath('//*[@id="chicityid"]')
        tasklist= table.find_elements_by_tag_name("tr")
        t = len(tasklist)
        print('tasklist length = '+str(t))

        for i in range(t):
        # k = tasklist[1]
            table = self.driver.find_element_by_xpath('//*[@id="chicityid"]')
            tasklist = table.find_elements_by_tag_name("tr")
            m = tasklist[i].find_elements_by_tag_name('td')
            print(type(m))
            print('td'+str(len(m)))
            a= m[7].find_elements_by_tag_name("a")
            print(type(a))
            print('a' + str(len(a)))
            a[2].click()
            sleep(2)
            self.driver.find_element_by_link_text('确定').click()

    def add_worker_info(self):
        self.driver.find_element_by_css_selector('button[onclick="tasklist()"]').click()
        sleep(2)
        iframe = self.driver.find_element_by_css_selector('div.layui-layer-content>iframe')
        # iframe = self.driver.find_element_by_xpath('//iframe')
        # iframe = self.driver.find_element_by_css_selector('#layui-layer-iframe5')
        self.driver._switch_to.frame(iframe)
        table = self.driver.find_element_by_css_selector("table>tbody")
        tasklist = table.find_elements_by_tag_name("tr")
        # // *[ @ id = "layui-layer-iframe5"]
        print(len(tasklist))
        a = tasklist[0].find_elements_by_tag_name('td')
        print(len(a))
        a[5].find_element_by_tag_name('a').click()

        self.driver.find_element_by_css_selector('input[name="companyName"]').send_keys("lihh")
        self.driver.find_element_by_css_selector('input[name="projectName"]').send_keys("lihh")
        self.driver.find_element_by_css_selector('input[name="linkPhone"]').send_keys("10086")
        self.driver.find_element_by_css_selector('input[name="answerPerson"]').send_keys("lihh")
        self.driver.find_element_by_css_selector('input[name="answerTime"]').click()
        sleep(3)
        ele = self.driver.find_element_by_css_selector('div>div.datetimepicker-days>table.table-condensed>tfoot>tr>th.today')
        ele.click()
        self.driver.find_element_by_css_selector('input[name="measuredUnit"]').send_keys("1")
        table = self.driver.find_element_by_css_selector('table#dataTable>tbody')
        processlist = table.find_elements_by_tag_name('tr')
        processlist[0].find_element_by_css_selector('td>input.Wdate').click()
        iframe = self.driver.find_elements_by_css_selector('body>div>iframe')
        print(type(iframe))
        print(len(iframe))
        self.driver._switch_to.frame(iframe)
        self.driver.find_element_by_css_selector("input#dpTodayInput").click()
        sleep(3)

if __name__ == '__main__':
    Manage.te1st_002_add_process()