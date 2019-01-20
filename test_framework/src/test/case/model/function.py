#发送邮件
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def insert_img(driver, filename):
    #获取当前文件所在路径
    func_path = os.path.dirname(__file__)
    print(func_path)
    #获取上一级目录
    base_dir = os.path.dirname(func_path)

    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')

    base = base_dir.split("/Website")[0]

    filepath = base + '/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)

#获取最新报告
def latest_report(filepath):
    # report_dir = r'C:\Users\Yuexl\Documents\GitHub\SeleniumLesson\trunk\unittestlihh\testreport'
    report_dir = filepath
    #返回指定的文件夹中的文件列表
    lists = os.listdir(report_dir)
    #按时间顺序对文件排序
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'))
    print(lists)
    print("latest report is:"+lists[-2])

    #输出最新报告路径
    file = os.path.join(report_dir,lists[-2])
    return file

#发送邮件
def send_mail(latest_report):
    print("最新报告"+latest_report)
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    #发送邮箱服务器
    smtpserver='smtp.163.com'

    #发送邮箱及授权密码
    user='lihh0727@163.com'
    password='mxr870828'

    #发送邮箱和接收邮箱
    sender='lihh0727@163.com'
    receives=['463836190@qq.com']

    #邮件主题和内容
    subject='Web Selenium 自动化测试报告'
    # content='<html><h1 style="color:red">我要自学网，自学成才</h1></html>'
    #邮件正文
    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject'] = subject
    msg['From']=sender
    msg['To']=','.join(receives)

    #SSL协议端口号,不同邮箱端口不同
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    #向服务器标识用户身份
    smtp.helo(smtpserver)
    #服务器返回结果确认
    smtp.ehlo(smtpserver)
    #登录邮箱服务器用户名密码
    smtp.login(user,password)

    print("Start send Email...")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send success")


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://baidu.com")
    # insert_img(driver, "baidu.png")
