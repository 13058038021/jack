#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #导入鼠标事件
from selenium.webdriver.support.select import Select#导入select方法
from selenium.webdriver.support import expected_conditions as EC #导入EC判断方法
from selenium.webdriver.support.wait import WebDriverWait# 导入 显示等待
from selenium.common.exceptions import * #导入所有异常类
from selenium.webdriver.common.keys import Keys

import time
import os
import xlrd
top_text=("xpath","//*[@id='accountLoginDiv']/h4")

class Base(object):
    '''基于原生的selenium框架做了二次封装'''

    def __init__(self,driver):
        '''初始化driver'''
        self.driver=driver

    def open(self,url):
        '''输入网址，并页面最大化'''
        driver.get(url)
        driver.maximize_window()

    def find_element(self,locator):
        '''定位元素，参数locator是元祖类型'''
        element=WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator):
        '''定位一组元素，参数locator是元祖类型'''
        elements=WebDriverWait(self.driver,timeout=1).until(EC.presence_of_all_elements_located(locator))

    def send_keys(self,locator,text):
        '''输入文本方法'''
        element=self.find_element(locator)
        element.send_keys(text)

    def keys_enter(self,locator,text):
        '''定位元素输入内容并敲enter回车键'''
        element = self.find_element(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def click(self,locator):
        '''点击方法'''
        element=self.find_element(locator)
        element.click()

    def get_text(self,locator):
        '''获取元素的文本'''
        try:
            a=self.find_element(locator).text
            return a
        except:
            return False

    def read_excel_values(self,path,nrows,ncols):
        '''读取指定excel的某个值'''
        excel=xlrd.open_workbook(path)#打开指定路径excel文件
        sheet=excel.sheet_by_name("Sheet1")#指定sheet
        data=sheet.cell_value(nrows,ncols)#读取指定行列的值
        return data

    def read_excel_nrows(self,path,nrows):
        '''读取指定一行数据'''
        excel=xlrd.open_workbook(path)#打开指定路径excel文件
        sheet=excel.sheet_by_name("Sheet1")#指定sheet
        data = sheet.row_values(nrows)#读取指定某一行数据
        return data

    def js_window_bom(self):
        '''通过执行js脚本方式将页面置顶或者置底,参数左边代表左右移动，右边代表上下'''
        js = "window.scrollTo(0,10000);"
        driver.execute_script(js)

    def js_window_top(self):
        '''通过执行js脚本方式将页面置顶或者置底,参数左边代表左右移动，右边代表上下'''
        js = "window.scrollTo(0,0);"
        driver.execute_script(js)

    def js_element_top(self, locator):
        '''通过js脚本方式将指定元素置顶'''
        try:
            self.target = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", self.target)
        except Exception as msg:
            print("没有定位到该元素，无法置顶：" + str(msg))

if __name__=="__main__":
     driver=webdriver.Chrome()
     my_driver=Base(driver)
     my_driver.open("https://www.baidu.com")
     sousuo=("id","kw")
     my_driver.keys_enter(sousuo,"刘德华")






