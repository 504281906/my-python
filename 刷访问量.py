# -*- coding:utf-8  -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

screenImg = "E:/screenImg.png"
PostUrl = "https://blog.csdn.net/modiz/article/details/81981300" #"https://blog.csdn.net/modiz/article/details/81261594" #"https://weibo.com/login.php"
# phantomJs = "D:\Python27\Scripts\phantomjs.exe"
phantomJs = "E:/phantomjs.exe"

#driver = webdriver.Firefox()
driver = webdriver.PhantomJS(phantomJs)
i = 0

while (True):
	driver.get(PostUrl)
	time.sleep(60)
	i = i + 1
	print i