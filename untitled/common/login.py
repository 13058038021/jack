from selenium import webdriver
import unittest

class login():
    def login_go(self):
        self.dir = webdriver.Chrome()
        self.dir.get("https://sso-test.belle.net.cn/")
        self.dir.find_element_by_id("username").send_keys("liu.yqty")
        self.dir.find_element_by_id("password").send_keys("111111")
        self.dir.find_element_by_id("submit_name_password").click()
        self.dir.find_element_by_id("ts-retail_binding").click()  # 点击体育零售系统
        self.dir.find_element_by_xpath("//*[@id='reload-button']").click() # 重新加载页面
    def refresh (self):
        self.dir.refresh()


