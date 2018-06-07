# -*- coding:utf-8  -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

PostUrl = "https://weibo.com/login.php"
driver = webdriver.Firefox()
driver.get(PostUrl)

#time.sleep(10)
#driver.implicitly_wait(20)
locator = (By.NAME, 'username')
try:
	#显性等待
	WebDriverWait(driver, 50, 0.5).until(EC.presence_of_element_located(locator))

	#账号信息
	elem_user = driver.find_element_by_name('username')
	elem_psw = driver.find_element_by_name('password')

	#输入账号信息
	elem_user.click()
	elem_user.send_keys('36525845@qq.com')
	elem_psw.send_keys('passwordZsd6718263')
	
	#点击登录
	click_login = driver.find_element_by_xpath("//div[@class='info_list login_btn']")
	click_login.click()
	
	locator = (By.NAME, 'pic_upload')
	WebDriverWait(driver, 50, 0.5).until(EC.presence_of_element_located(locator))
	
	elem_msg = driver.find_element_by_css_selector("textarea[title=\"微博输入框\"]")
	elem_msg.send_keys(u'		 ☆☆   ☆☆\n		☆☆☆ ☆☆☆')
	
	click_push = driver.find_element_by_css_selector("a[title=\"发布微博按钮\"]")
	click_push.click()
finally:
	#driver.close()