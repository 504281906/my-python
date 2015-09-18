# -*- coding:utf8 -*-
import socket
import win32com.client
import os
import zipfile
import codecs
import base64
import time
import sys
def decode_base64(data):
	missing_padding = 4 - len(data) % 4
	if missing_padding:
		data += b'='* missing_padding
	return base64.decodestring(data)
host='115.29.79.37'
part=6666
timeout=5
dicName="C:\modiz\\"
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	ss.bind((host,part))
	ss.listen(10)
	print "waiting for connect."
	while True:
		try:
			buf_size=6553533
			cs,addr=ss.accept()
			print addr
			#socket.setdefaulttimeout(timeout)
			cs.send("connected!")
			#获取加密数据
			encode_data=cs.recv(buf_size)
			#把数据写到out.zip文件
			tmpfile=open('out.tmp','wb')
			try:
				#print encode_data
				missing_padding = 4 - len(encode_data) % 4
				if missing_padding:
					encode_data += b'='* missing_padding
				tmpfile.write(encode_data)
				tmpfile.close()
			except IOError,e:
				print "IOError!"%e
				tmpfile.close()
			finally:
				tmpfile.close()
			#base64 decode 2进制 解密 decode(infile,outfile)
			tmpfile=open('out.tmp','rb')
			outfile=open('out.zip','wb')
			#raw_input("Press Enter to continue: ")
			base64.decode(tmpfile,outfile)
			tmpfile.close()
			outfile.close()
			#打开zip文件
			zfile=zipfile.ZipFile('out.zip','r')
			#raw_input("Press Enter to continue1: ")
			#创建一个文件夹来存放获取的zip文件
			if not os.path.exists(dicName):
				os.mkdir(dicName)
			for f in zfile.namelist():
				data=zfile.read(f)
				file=open(dicName+os.path.basename(f),'a+b')
				file.write(data)
				file.close()
			print "finished!"
			zfile.close()
			#后续处理，删除临时文件
			os.remove('out.tmp')
			os.remove('out.zip')
			cs.close()
		except socket.error,e:
			print "socket创建失败"
			cs.close()
	ss.close()
except socket.error,e:
	print "socket创建失败1"
	ss.close()