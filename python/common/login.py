from selenium import webdriver
import unittest
import time

class LoginBelle():
    def login_go(self):
        self.dir = webdriver.Chrome()
        self.dir.get("https://sso-test.belle.net.cn/")
        self.dir.find_element_by_id("username").send_keys("liu.yqty")
        self.dir.find_element_by_id("password").send_keys("111111")
        self.dir.find_element_by_id("submit_name_password").click()
        self.dir.find_element_by_id("ts-retail_binding").click()  # 点击体育零售系统
        self.dir.find_element_by_xpath("//*[@id='reload-button']").click() # 重新加载页面
        time.sleep(3)
        a = self.dir.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span[2]").text
        print(a)


if __name__=="__main__":
    a=login()
    a.login_go()