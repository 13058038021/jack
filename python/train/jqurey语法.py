

from selenium import webdriver
driver=webdriver.Chrome()

#定位元素并输入值
jquery="$('#kw').val('aaa')"
driver.execute_script(jquery)
#定位元素
jquery="$('#kw')"
driver.execute_script(jquery)

#点击元素
jquery="$('#kw').click"
driver.execute_script(jquery)
