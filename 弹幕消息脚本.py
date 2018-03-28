# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import sys

if __name__=='__main__':
	url=raw_input()
	driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
	driver.implicitly_wait(20)
	driver.get(url)
	# driver.get('https://www.baidu.com/')
	try:
		driver.find_element_by_class_name("sendMsg")
		a = True
	except:
		a = False
	if a == True:
		i = 1
		while(1):
			driver.find_element_by_class_name("sendMsg").send_keys(i)
			driver.find_element_by_class_name("send").click()
			i+=1
	else:
		print 'no'