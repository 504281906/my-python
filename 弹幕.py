# -*- coding:utf-8 -*-
import os 
import ctypes
import string
from time import ctime,sleep
from ctypes import *
import threading
import logging
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')
path=os.path.dirname(__file__)

def kplive():   #每隔30s重复发送心跳包
	while(1):
		dll.keeplive()
		sleep(30)

def go():
	while(1):
		dll.getmsg.restype=c_char_p  #这里用来向python解释，调用c++的这个函数应该返回类型是什么。
		s=dll.getmsg()

		ans=""
		#用户弹幕
		if (s.find("type@=chatmsg")!=-1):
			pattern = re.compile(u'nn@=(.*?)/txt',re.U)
			nick = pattern.search(s)
			pattern = re.compile(u'txt@=(.*?)/cid',re.U)
			txt = pattern.search(s)
			pattern = re.compile(u'level@=(.*?)/',re.U)
			level = pattern.search(s)
			ans += nick.group(1).encode('gb18030')+"(等级%s):"%level.group(1)+txt.group(1).encode('gb18030')
			#print txt.group(1).encode('gb18030')
			#print nick.group(1)
			print ans
			logger.info(ans)
		elif (s.find("type@=uenter")!=-1):
			pattern = re.compile(u'nn@=(.*?)/level',re.U)
			nick = pattern.search(s)
			pattern = re.compile(u'level@=(.*?)/',re.U)
			level = pattern.search(s)
			ans += "欢迎 " + nick.group(1).encode('gb18030') + "(等级%s) 加入房间"%level.group(1)
			print ans
		
if __name__=='__main__':
	log_filename="t1.txt"
	fmt = '%(asctime)s - %(message)s'
	formatter = logging.Formatter(fmt)
	
	logger = logging.getLogger('弹幕')
	logger.setLevel(logging.DEBUG)

	#cmd显示
	#ch = logging.StreamHandler()
	#ch.setFormatter(formatter)
	#ch.setLevel(logging.DEBUG)

	#log显示
	fh = logging.FileHandler(log_filename)
	fh.setFormatter(formatter)
	fh.setLevel(logging.DEBUG)

	#logger.addHandler(ch)
	logger.addHandler(fh)
	
	#引用C++库
	dll = ctypes.WinDLL(os.path.join(path,"h1.dll"))

	#连接客户端
	dll.client()

	#提示输入房间号
	print r"请输入房间号:"
	t=raw_input()
	dll.c_init("%s"%t)

	#输出到文件t1.txt
	#dll.writefile()

	#多线程，t1保持活性,t2循环抓包
	threads =[]
	t1=threading.Thread(target=kplive)
	threads.append(t1)
	t2=threading.Thread(target=go)
	threads.append(t2)

	for i in threads:
		"""
			setDaemon(True)将线程声明为守护线程，必须在start()方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
			子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句os.system("pause")后，没有等待子线程，
			直接就退出了，同时子线程也一同结束。
		"""
		#i.setDaemon(True)
		i.start()

#https://www.douyu.com/97376