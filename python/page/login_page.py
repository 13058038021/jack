#coding：utf-8
from common.base import Base


belle_url = ("https://sso-test.belle.net.cn/")

class LoginPage(Base):

    username_loc = ("id", "username")
    password_loc = ("id", "password")
    submit_button = ("id", "submit_name_password")
    tsretail_loc=("id","ts-retail_binding")
    reload_page_loc=("xpath","//*[@id='reload-button']")
    top_text=("xpath","//*[@id='accountLoginDiv']/h4")
    excel_path = "C:\\Users\\jack\\Desktop\\test.xlsx"
    def input_username(self,user):
        self.send_keys(self.username_loc,user)

    def input_password(self,password):
        self.send_keys(self.password_loc,password)

    def click_login_button(self):
        self.click(self.submit_button)

    def click_tsretail(self):
        self.click(self.tsretail_loc)

    def click_reload_page(self):
        self.click(self.reload_page_loc)

    def get_top_text(self):
        a=self.get_text(self.top_text)
        return a

    def read_excel(self):
        a=self.read_excel_values(self.excel_path,1,1)
        return a



if __name__=="__main__":
    from selenium import  webdriver
    driver=webdriver.Chrome()
    login_driver=LoginPage(driver)
    driver.get(belle_url)
    login_driver.input_username("liu.yqty")
    a=login_driver.get_top_text()
    print(a)




