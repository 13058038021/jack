from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element("id","kw").send_keys("刘德华")
js="document.getElementById('su').click();"
driver.execute_script(js)

#----------------js获取元素方法---------------------------------
#删掉js方法
js='document.getElementById("su").removeAttribute("readonly");'
driver.execute_script(js)
# #通过id获取元素
js= "document.getElementById('元素')"
driver.execute_script(js)
# #通过name获取元素,获取的是多个
js= "document.getElementByName('id')[0]"
driver.execute_script(js)
# #通过tagName获取元素,获取的是多个
js= "document.getElementTagName('tag')"
driver.execute_script(js)
# #通过ClassName获取元素,获取的是多个
js="document.getElementClassName('calss')"
driver.execute_script(js)
# #通过css获取元素
js="document.querySelectorAll('cssSelector')"
driver.execute_script(js)


#----------------jquery语法---------------------------------
#定位元素并输入内容
jquery="$('#kw').val('aaa')"
driver.execute_script(jquery)

#定位元素并清空内容
jquery="$('#kw').val('')"
driver.execute_script(jquery)

#定位元素
jquery="$('#kw')"
driver.execute_script(jquery)

#点击元素
jquery="$('#kw').click"
driver.execute_script(jquery)