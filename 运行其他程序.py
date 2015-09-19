# -*-coding:utf:8 -*-
import shutil
import os
dir=os.getcwd()
print dir
path='D:\jietu'
p="D:\\Notepad++\\readme.txt"
print p
if os.path.isfile('n1.py'):
	print "Y"
	shutil.copy('n1.py',path)
	os.system("start %s"%p)
else:
	#shutil.copy('n1.py',path)
	print "N"