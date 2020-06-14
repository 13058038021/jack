#conding:utf-8
import unittest
from selenium import webdriver
from page.login_page import belle_url,LoginPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
excel_path = "C:\\Users\\jack\\Desktop\\test.xlsx"
class login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.login_driver=LoginPage(self.driver)
        self.driver.get(belle_url)
    def test_login(self):
        self.a = self.login_driver.get_top_text()
        print(self.a)
        self.assertEqual("账户登录",self.a)
        self.login_driver.input_username("liu.yqty")
        self.login_driver.input_password("111111")
        self.login_driver.click_login_button()
        self.login_driver.click_tsretail()
        self.login_driver.click_reload_page()
        self.a=self.login_driver.read_excel_values(excel_path,1,1)
        print(self.a)
        self.driver.implicitly_wait(30)

if __name__=="__main__":
    unittest.TestCase