from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
#三种方法
driver.find_element_by_id("kw").click()

driver.find_element(By.ID,"kw").click()

driver.find_element("id","kw").click()