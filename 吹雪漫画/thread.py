#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import socket
import requests
import cStringIO
import re
from selenium import webdriver
import sys
import os
import threading
import time
from selenium.common.exceptions import TimeoutException

reload(sys)
sys.setdefaultencoding( "utf-8" )

num = 1
socket.setdefaulttimeout(15)
chapterList = []
FinishList = []

class myThread (threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		driver = webdriver.PhantomJS()
		driver.set_page_load_timeout(30)
		global FinishList
		for url in chapterList:
			if url in FinishList:
				continue
			FinishList.append(url)
			try:
				driver.get(url)
			except (TimeoutException,socket.timeout):
				driver.execute_script('window.stop()')
			content = driver.page_source.decode('utf-8', 'ignore').replace(u'\xa9', u'')

			soup = BeautifulSoup(content, "html5lib")
			optionList = soup.find_all('option')
			count = 0
			for option in optionList:
				value = int(option.get('value'))
				if (count<value):
					count = value
			pa = re.compile("^.*/(.*?).html")
			names = pa.findall(url)
			for index in range(1,count+1,1):
				nextUrl = url + '?page=%d'%index
				print self.name+" "+nextUrl
				try:
					driver.get(nextUrl)
				except (TimeoutException,socket.timeout):
					driver.execute_script('window.stop()')
				
				content = driver.page_source.decode('utf-8', 'ignore').replace(u'\xa9', u'')
				soup = BeautifulSoup(content, "html5lib")
				img = soup.find('img',id = 'viewimg')
				if img == None:
					print r'can"t find ViewImg'
					break
				imgUrl = img.get('src')
				save_img(index,imgUrl,names)
			print>>f,url
		driver.quit()
			
def downloadPic(imgUrl,pic_name):
	#解决下载不完全问题且避免陷入死循环
	try:
		urllib.urlretrieve(imgUrl,pic_name)
	except socket.timeout:
		count = 1
		while count<=5:
			try:
				urllib.urlretrieve(imgUrl,pic_name)
				break
			except socket.timeout:
				err_info = u'重试次数%d'%count
				print err_info
				count += 1
		if count>5:
			print u'下载失败'
				
def save_img(num,imgUrl,name):
	document = fileName
	exists = os.path.exists(document)
	if not exists:
		os.makedirs(document)
	pic_name = document + '/' + str(name[0]) + '_' + str(num) + '.jpg'
	exists = os.path.exists(pic_name)
	if exists:
		return
	downloadPic(imgUrl,pic_name)
	
def GetAllChapter(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	content = response.read();
	soup = BeautifulSoup(content, "html5lib")
	a = soup.find_all('a',attrs={'title':True,'target':False},href=re.compile("html"))
	global chapterList
	s = 'http://www.chuixue.net'
	print a.__len__()
	for i in range(a.__len__()-1,0,-1):
		url = a[i].get('href')
		if (url!=None):
			chapterList.append(s+url)
	# http://www.chuixue.net/manhua/26798/309636.html

	f = open (r'c:\finishiList.txt','a+')
	FinishList = f.readlines()
	f.close()
	
# 'http://www.chuixue.net/manhua/26798/'
# 'http://www.chuixue.net/manhua/886/'
# 'http://www.chuixue.net/manhua/2458/'
if __name__ == "__main__":
	url = raw_input(u'输入吹雪漫画主页地址:'.encode('gbk'))
	fileName = raw_input(u'输入存放本地文件夹地址:'.encode('gbk'))
	threadNum = raw_input(u'输入线程个数:'.encode('gbk'))
	GetAllChapter(url)
	
	# lock=threading.Lock()
	f = open(r'c:\finishiList.txt','w+')
	threadList = []
	for i in range(int(threadNum)):
		threadList.append(myThread(i,"Thread-%d"%i))
	
	for i in range(int(threadNum)):
		threadList[i].start()
		time.sleep(1)
	
	for i in range(int(threadNum)):
		threadList[i].join()
	f.close()
	# driver.quit()
