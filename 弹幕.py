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

def kplive():   #ÿ��30s�ظ�����������
	while(1):
		dll.keeplive()
		sleep(30)

def go():
	while(1):
		dll.getmsg.restype=c_char_p  #����������python���ͣ�����c++���������Ӧ�÷���������ʲô��
		s=dll.getmsg()

		ans=""
		#�û���Ļ
		if (s.find("type@=chatmsg")!=-1):
			pattern = re.compile(u'nn@=(.*?)/txt',re.U)
			nick = pattern.search(s)
			pattern = re.compile(u'txt@=(.*?)/cid',re.U)
			txt = pattern.search(s)
			pattern = re.compile(u'level@=(.*?)/',re.U)
			level = pattern.search(s)
			ans += nick.group(1).encode('gb18030')+"(�ȼ�%s):"%level.group(1)+txt.group(1).encode('gb18030')
			#print txt.group(1).encode('gb18030')
			#print nick.group(1)
			print ans
			logger.info(ans)
		elif (s.find("type@=uenter")!=-1):
			pattern = re.compile(u'nn@=(.*?)/level',re.U)
			nick = pattern.search(s)
			pattern = re.compile(u'level@=(.*?)/',re.U)
			level = pattern.search(s)
			ans += "��ӭ " + nick.group(1).encode('gb18030') + "(�ȼ�%s) ���뷿��"%level.group(1)
			print ans
		
if __name__=='__main__':
	log_filename="t1.txt"
	fmt = '%(asctime)s - %(message)s'
	formatter = logging.Formatter(fmt)
	
	logger = logging.getLogger('��Ļ')
	logger.setLevel(logging.DEBUG)

	#cmd��ʾ
	#ch = logging.StreamHandler()
	#ch.setFormatter(formatter)
	#ch.setLevel(logging.DEBUG)

	#log��ʾ
	fh = logging.FileHandler(log_filename)
	fh.setFormatter(formatter)
	fh.setLevel(logging.DEBUG)

	#logger.addHandler(ch)
	logger.addHandler(fh)
	
	#����C++��
	dll = ctypes.WinDLL(os.path.join(path,"h1.dll"))

	#���ӿͻ���
	dll.client()

	#��ʾ���뷿���
	print r"�����뷿���:"
	t=raw_input()
	dll.c_init("%s"%t)

	#������ļ�t1.txt
	#dll.writefile()

	#���̣߳�t1���ֻ���,t2ѭ��ץ��
	threads =[]
	t1=threading.Thread(target=kplive)
	threads.append(t1)
	t2=threading.Thread(target=go)
	threads.append(t2)

	for i in threads:
		"""
			setDaemon(True)���߳�����Ϊ�ػ��̣߳�������start()��������֮ǰ���ã����������Ϊ�ػ��̳߳���ᱻ���޹���
			���߳������󣬸��߳�Ҳ����ִ����ȥ�������߳�ִ�������һ�����os.system("pause")��û�еȴ����̣߳�
			ֱ�Ӿ��˳��ˣ�ͬʱ���߳�Ҳһͬ������
		"""
		#i.setDaemon(True)
		i.start()

#https://www.douyu.com/97376