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
from selenium.common.exceptions import TimeoutException

reload(sys)
sys.setdefaultencoding( "utf-8" )

num = 1
socket.setdefaulttimeout(15)
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
				
def save_img(num,imgUrl):
	document = fileName
	exists = os.path.exists(document)
	if not exists:
		os.makedirs(document)
	pic_name = document + '/' + str(num) + '.jpg'
	exists = os.path.exists(pic_name)
	if exists:
		return
	
	downloadPic(imgUrl,pic_name)
	# urllib.urlretrieve(imgUrl,pic_name)
	# try:
		# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		# headers = { 'User-Agent' : user_agent }

		# req = urllib.request.Request(img_url, headers=headers)
		# response = urllib.request.urlopen(req, timeout=30)


		# data = response.read()


		# if response.info().get('Content-Encoding') == 'gzip':
			# data = zlib.decompress(data, 16 + zlib.MAX_WBITS)


		# fp = open(pic_name, "wb")
		# fp.write(data)
		# fp.close
		# print('save image finished:' + pic_name)
		# num = num + 1
	# except Exception as e:
		# print('save image error.')

# user_agent ='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'  
# headers = { 'User-Agent' : user_agent }
# 'http://www.chuixue.net/manhua/26798/'  
url = raw_input(u'输入吹雪漫画主页地址:'.encode('gbk'))
fileName = raw_input(u'输入存放本地文件夹地址:'.encode('gbk'))
req = urllib2.Request(url)
response = urllib2.urlopen(req)
content = response.read();
soup = BeautifulSoup(content, "html5lib")
a = soup.find_all('a',attrs={'title':True,'target':False},href=re.compile("html"))
chapterList = []
s = 'http://www.chuixue.net'
print a.__len__()
for i in range(a.__len__()-1,0,-1):
	url = a[i].get('href')
	if (url!=None):
		chapterList.append(s+url)
# http://www.chuixue.net/manhua/26798/309636.html

f = open (r'c:\out.txt','a+')
if (f.readlines()):
	cont = int(f.readlines()[-1])
else:
	cont = 0;
print cont
f.close()
f = open(r'c:\out.txt','w+')
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(30)
for url in chapterList:
	try:
		driver.get(url)
	except (TimeoutException,socket.timeout):
		driver.execute_script('window.stop()')
	content = driver.page_source.decode('utf-8', 'ignore').replace(u'\xa9', u'')
	# request = urllib2.Request(url,headers = send_headers) 
	# response = urllib2.urlopen(request)
	# content = response.read();
	soup = BeautifulSoup(content, "html5lib")
	# print>>f,content
	optionList = soup.find_all('option')
	count = 0
	for option in optionList:
		value = int(option.get('value'))
		if (count<value):
			count = value
	print count
	if (num+count<cont):
		num += count
		print "---%d"%num
		continue
	
	if (num>cont):
		img = soup.find('img',id = 'viewimg')
		if img == None:
			print r'can"t find ViewImg'
			break
		imgUrl = img.get('src')
		# print imgUrl
	
		save_img(num,imgUrl)
		print>>f,num
		num = num + 1
	else:
		num+=1
	if (count >= 2):
		for index in range(2,count+1,1):
			if (num>cont):
				nextUrl = url + '?page=%d'%index
				print nextUrl
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
				save_img(num,imgUrl)
				print>>f,num
				num = num + 1
			else:
				num = num + 1
			# print>>f,imgUrl
driver.quit()
# f.close()