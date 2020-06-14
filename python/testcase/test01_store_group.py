import time
import unittest
from selenium.webdriver.common.keys import Keys #键盘事件
from common import login
#from common import mysql
import urllib.request

class belle(unittest.TestCase):

    def setUp(self):
        print("开始测试")
    def testStore(self):
        #print(mysql.mysql.sql2)#调用mysql.py文件的sql
        login.login.login_go(self)  #调用login.py文件的登录封装方法
        data = urllib.request.urlopen("https://sso-test.belle.net.cn/")
        print(data.read())
        time.sleep(1)
        a=self.dir.find_element_by_xpath("//*[@id='subSystem']/div[1]/div/a[7]").text
        print(a)
        #self.dir.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/span/input[1]").send_keys("SC-店铺组设置")#输入店铺组设置

    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/span/input[1]").send_keys(Keys.ENTER)#回车
    #     time.sleep(2)
    #     fr=self.dir.find_element_by_xpath("//*[@id='mainTabs']/div[2]/div[2]/div/iframe")#定位框架
    #     time.sleep(1)
    #     self.dir.switch_to.frame(fr)#切换框架
    #     self.dir.find_element_by_xpath("//*[@id='btn-add']/span/span").click()#点击新增按钮
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r4-2-0']/td[2]/div/table/tbody/tr/td/span/input[1]").click()  # 点击店铺名称输入框
    #     time.sleep(2)
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r4-2-0']/td[2]/div/table/tbody/tr/td/span/input[1]").send_keys("深圳南山海德三路海岸城AD二店")  # 点击店铺名称输入框
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r4-2-0']/td[2]/div/table/tbody/tr/td/span/input[1]").send_keys(Keys.ENTER)  # 点击店铺名称输入框
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r4-2-0']/td[4]/div/table/tbody/tr/td/input").click()  # 选择生效日期
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r4-2-0']/td[4]/div/table/tbody/tr/td/input").send_keys(Keys.ENTER)#回车
    #     #self.dir.find_element_by_xpath("//*[@id='dpTodayInput']").click()  # 选择今天
    #     time.sleep(3)
    #     self.dir.find_element_by_xpath(".//*[@id='datagrid-row-r4-2-0']/td[5]/div/table/tbody/tr/td/input").click()  # 选择终止日期
    #
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r4-2-0']/td[5]/div/table/tbody/tr/td/input").send_keys(Keys.ENTER)#回车
    #     self.dir.find_element_by_xpath("//*[@id='div1']/table/tbody/tr[1]/td[2]/span/input[1]").send_keys("K9003")  # 点击公司编码输入框
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r2-1-0']/td/div/input").click()  #勾选K9003公司
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[@id='storeGroupNames']").send_keys("最大的店铺组")  # 输入店铺组名称
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[@id='div1']/table/tbody/tr[2]/td[2]/span/input[1]").send_keys("存现")  # 点击业务类型输入存现
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[@id='div1']/table/tbody/tr[2]/td[2]/span/input[1]").send_keys(Keys.ENTER)  # 点击业务类型输入存现
    #     time.sleep(2)
    #     self.dir.find_element_by_xpath("//*[@id='myFormPanel']/div[2]/a[1]/span/span").click()  # 点击保存
    #     time.sleep(3)
    #     self.dir.switch_to.default_content()#退出iframe 回到顶层html
    #     self.dir.find_element_by_xpath("//*[text()='保存成功!']/../div[4]/a/span/span").click()#点击确定
    #     time.sleep(1)
    #     self.dir.switch_to.frame(fr)  # 切换框架
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[@id='btn-search']/span/span").click()#查询
    #     assert u"最大的店铺组" in self.dir.page_source,u"页面不存在此数据" #断言页面是否有最大的店铺组店铺组名称
    #     time.sleep(2)
    #     self.dir.find_element_by_xpath("//*[@id='btn-export']/span/span").click()  #导出
    #     self.dir.find_element_by_xpath("//*[@id='datagrid-row-r3-2-0']/td[1]/div/input").click()#勾选第一条数据
    #     self.dir.find_element_by_xpath("//*[@id='btn-del']/span/span").click()#点击删除
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath("//*[text()='确定']").click()#点击确定
    #     time.sleep(2)
    #     self.dir.switch_to.default_content()  # 退出iframe 回到顶层html
    #     time.sleep(1)
    #     self.dir.find_element_by_xpath(".//*[text()='删除成功']/../div[4]/a/span/span").click()
    #     time.sleep(2)
    # def tearDown(self):
    #     self.dir.quit()
    #     print("测试完成")


if __name__ == '__main__':
    unittest.main()

