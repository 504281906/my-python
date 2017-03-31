# -*- coding:utf8 -*-
import itchat
import time
import re
import thread
import requests
from itchat.content import *
import sys
import os
import ctypes
reload(sys)
sys.setdefaultencoding("utf-8")
itchat.auto_login(enableCmdQR=True) #是的

KEY = '6735a72149c84bfea8845f4f66e9bf58' #周大宝
flag = 1
def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'    : KEY, 
		'info'   : msg,
		'userid' : 'wechat-robot',
		}
	try:
		r = requests.post(apiUrl,data=data).json()
		if (r.get('url')!=None):
			return r.get('text')+" "+r.get('url') + '\n----自动回复By周大宝'
		else:
			return r.get('text') + '\n----自动回复By周大宝'
	except Exception,e:  
		print Exception,":",e
		return r"哎呀，我可能生病了，告诉我爸爸好吗，嘎~ \n----自动回复By周大宝"
	
	
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
	global flag
	if msg['Type'] == 'Text':
		if msg['Text'] == "上线":
			flag = 1
		elif msg['Text'] == "下线":
			flag = 0
		reply_content = msg['Text']
		reply = get_response(msg['Text'])
	elif msg['Type'] == 'Map':
		x,y,location = re.search('<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*',msg['OriContent']).group(1,2,3)
		if location is None:
			reply_content = r"位置:纬度->" + x.__str__() + "经度->" + y.__str__()
		else:
			reply_content = r"位置:" + location
		reply = get_response(reply_content)
	elif msg['Type'] == 'Card':
		reply_content = " " + msg['RecommendInfo']['NickName'] + r"的名片"
		reply = get_response(reply_content)
	elif msg['Type'] == 'Note':
		reply_content = r"通知"
		reply = get_response(msg['Text'])
	elif msg['Type'] == 'Sharing':
		reply_content = r"分享"
		reply = get_response(msg['Text'])
	else:
		reply_content = r'消息'
		reply = get_response(msg['text'])
	friend = itchat.search_friends(userName = msg['FromUserName'])
	itchat.send(r"盆友:%s -- %s	"
				r"时间:%s	"
				r"消息:%s	" %(friend['NickName'],friend['RemarkName'],time.ctime(),reply_content),toUserName='filehelper')
	if flag == 1:
		itchat.send(reply,toUserName=msg['FromUserName'])
	else:
		itchat.send(reply,toUserName='filehelper')

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
	if msg['Type'] == 'Picture':
		reply = get_response(msg['Text'])
	elif msg['Type'] == 'Recording':
		reply = get_response(msg['Text'])
	elif msg['Type'] == 'Attachment':
		reply = get_response(msg['Text'])
	elif msg['Type'] == 'Video':
		reply = get_response(msg['Text'])
	if flag == 1:
		itchat.send(reply,toUserName=msg['FromUserName'])
	else:
		itchat.send( '@%s@%s' % ({'picture':'img', 'Video':'vid'}.get(msg['Type'],'fil'),msg['FileName']),toUserName='filehelper')

@itchat.msg_register(FRIENDS)
def add_friend(msg):
	itchat.add_friend(**msg['Text'])
	itchat.send_msg(r'很高兴认识你！',msg['RecommendInfo']['UserName'])

if __name__=="__main__":
	itchat.auto_login()
	#隐藏窗口
	whnd = ctypes.windll.kernel32.GetConsoleWindow()
	if whnd != 0:
		ctypes.windll.user32.ShowWindow(whnd, 0)
		ctypes.windll.kernel32.CloseHandle(whnd)
	itchat.run()