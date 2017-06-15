# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def insert_one(data,qq):
	if (data["shuos"].strip()!=''):
		f = open("%s.txt"%qq,'ab+')
		string = "%s 说说:%s\r\n"%(data["time"].encode('gb18030'),data["shuos"].encode('gb18030'))
		f.write(string)
		f.close()

def go(qq):
	driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
	driver.implicitly_wait(10)
	driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
	try:
		driver.find_element_by_id("login_div")
		a = True
	except:
		a=False
		print "主页打开失败"
	if a == True:
		# 选择登录框，自动填写账号登陆
		driver.switch_to.frame("login_frame")
		driver.find_element_by_id('switcher_plogin').click()
		driver.find_element_by_id('u').clear()
		driver.find_element_by_id('u').send_keys(504281906)
		driver.find_element_by_id('p').clear()
		driver.find_element_by_id('p').send_keys("hh&&zhouzhuo")
		driver.find_element_by_id('login_button').click()
	try:
		WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,"QM_OwnerInfo_Icon")))
		# driver.find_element_by_id("QM_OwnerInfo_Icon")
		b = True
	except:
		b = False
		print "没有权限"
	if b == True:
		driver.switch_to.frame('app_canvas_frame')
		content = driver.find_elements_by_css_selector('.content')
		stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
		for con,sti in zip(content,stime):
			# gbkTypeStr = unicodeTypeStr.encode(“GBK“, ‘ignore’);
			# print con.text,sti.text
			data = {
					'qq':qq,
					'time':sti.text,
					'shuos':con.text
				}
			# print(data)
			insert_one(data,qq)
	f = True
	k = 0;
	while(f):
		try:
			s = "pager_next_%s"%k
			driver.find_element_by_id(s).click()
			k += 1
		except:
			f = False
			print "没有下一页了"
		if f == True:
			time.sleep(3)
			# WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".content")))
			# WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"content")))
			# WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CLASS_NAME,'c_tx.c_tx3.goDetail')))
			content = driver.find_elements_by_css_selector('.content')
			stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
			for con,sti in zip(content,stime):
				# print con.text,sti.text
				data = {
						'qq':qq,
						'time':sti.text,
						'shuos':con.text
					}
				# print(data)
				insert_one(data,qq)
		print k
if __name__=='__main__':
	print r"请输入QQ号~:"
	qq=raw_input()
	go(qq)
	os.system("pause")