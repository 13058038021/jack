from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
#30秒内定位元素，直到定位到为止,lambda是隐式函数
element=WebDriverWait(driver,30).until(lambda x:x.find_element_by_id("kw"))
print(element)