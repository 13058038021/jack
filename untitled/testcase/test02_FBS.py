import time
import unittest
from selenium.webdriver.common.keys import Keys #键盘事件
from common import login
from common import mysql

class test2_bank_no(unittest.TestCase):
    def testLogin(self):
       # login.login.login_go(self)
        self.dir.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/span/input[1]").send_keys("SC-店铺组设置")  # 输入店铺组设置
        time.sleep(1)
        self.dir.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/span/input[1]").send_keys(Keys.ENTER)  # 回车
        time.sleep(2)