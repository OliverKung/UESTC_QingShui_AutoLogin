from selenium import webdriver
from time import sleep
import ping3
from win10toast import ToastNotifier
TN = ToastNotifier()
num = 0
for i in range(3):
    pingTime=ping3.ping("www.baidu.com",timeout=1,unit="ms")
    if not pingTime:
        num = num+1
if num >= 3:
    while( not ping3.ping("www.baidu.com",timeout=1,unit="ms")):
        TN.show_toast("ERROR!","CERNET Disconnected!")
        options = webdriver.ChromeOptions()
        options.add_argument("-ignore-certificate-errors")
        options.add_argument("-ignore-ssl-errors")
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        browser.get("http://aaa.uestc.edu.cn")
        sleep(10)
        browser.find_element("id","username").send_keys("username")#type your student number here#
        browser.find_element("id","password").send_keys("password")#type your password here#
        sleep(5)
        browser.find_element("id","school-login").click()
        sleep(5)
    TN.show_toast("FIXED","CERNET Connected")