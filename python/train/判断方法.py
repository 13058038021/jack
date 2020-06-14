#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

title=EC.title_is("百度")#判断title

def is_alert_exsist(self):
    try:
        alert= WebDriverWait(self,driver,10).until(EC.alert_is_present())
        return alert
    except:
        print("不存在alert弹出框")
        return False
#判断页面是否有这个字
def is_text_in_element(self,locator):
    text="百度"
    try:
        self.result=WebDriverWait(self,driver,10).until(EC.text_to_be_present_in_element(locator,text))
        return self.result
    except:
        print("不存在alert弹出框")
        return False
if __name__=="__main__":
    is_text_in_element()
