# -*- coding:utf-8 -*-

# 导入webdriver API对象，可以调用浏览器和操作页面
from selenium import webdriver
# 导入Keys，可以使用操作键盘，标签，鼠标
from selenium.webdriver.common.keys import Keys

# phantamJS浏览器对象
driver = webdriver.PhantomJS()

driver.get("https://www.douban.com/")
# send_keys()填写
driver.find_element_by_name("form_email").send_keys("963766613@qq.com")
driver.find_element_by_name("form_password").send_keys("kaoyan2017")
#driver.find_element_by_name("captcha_field").send_keys("")
# click()点击
driver.find_element_by_class_name("bn-submit").click()

driver.save_screenshot("douban.png")



phantom.exit()
