# -*- coding:utf-8  -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

screenImg = "E:/screenImg.png"
#"https://weibo.com/login.php"
# phantomJs = "D:\Python27\Scripts\phantomjs.exe"
phantomJs = "E:/phantomjs.exe"
i = 0
phoneNum = "" #'13831146969'
userName = "zdzcj1108"
passWord = "zdzcj123321~"
#driver = webdriver.Firefox()

def clover():
	PostUrl = "http://other-callback.shusw.com/register/sendmessage/type/reg"
	driver.get(PostUrl)
	elem_phone = driver.find_element_by_name('phone')
	elem_phone.click()
	elem_phone.send_keys(phoneNum)
	click_push = driver.find_element_by_class_name("getcode")
	# click_push = driver.find_element_by_value("获取验证码")
	click_push.click()

# def renren():
	# PostUrl = "http://reg.renren.com/xn6218.do?ss=10131&rt=1"
	# driver.get(PostUrl)
	# elem_phone = driver.find_element_by_name('regEmail')
	# elem_phone.click()
	# elem_phone.send_keys(phoneNum)
	# elem_phone = driver.find_element_by_name('pwd')

# def baidu():
	# PostUrl = "https://passport.baidu.com/v2/?reg"
	# driver.get(PostUrl)
	
	# elem_userName = driver.find_element_by_name('userName')
	# elem_userName.click()
	# elem_userName.send_keys(userName)
	
	# elem_phone = driver.find_element_by_name('phone')
	# elem_phone.click()
	# elem_phone.send_keys(phoneNum)
	
	# driver.save_screenshot(screenImg)
	
	# elem_password = driver.find_element_by_name('password')
	# elem_password.click()
	# elem_password.send_keys(passWord)
	
	# click_push = driver.find_element_by_class_name("pass-button pass-button-verifyCodeSend")
	# click_push = driver.find_element_by_value("获取验证码")
	# click_push.click()
	
def huhuVr():
	PostUrl = "http://bbs.huhuvr.com/member.php?mod=register"
	driver.get(PostUrl)
	
	click_agree = driver.find_element_by_class_name("pnc")
	click_agree.click()
	
	elem_phone = driver.find_element_by_name('mobile')
	elem_phone.click()
	elem_phone.send_keys(phoneNum)
	
	click_push = driver.find_element_by_id("getverifycode-btn")
	# click_push = driver.find_element_by_value("获取验证码")
	click_push.click()
	driver.save_screenshot(screenImg)
	
if __name__ == '__main__':
	phoneNum = raw_input()
	driver = webdriver.PhantomJS(phantomJs)
	driver.set_window_size(800, 600)
	
	while(True):
		clover()
		huhuVr()
		i = i + 1
		print i
	
# driver.save_screenshot(screenImg)

# 5429269@qq.com 123456789a
# chrisicyman@163.com 19820724  13794016500
# 26589597@qq.com  23845928
