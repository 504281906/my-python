<<<<<<< HEAD
# -*- coding:utf-8 -*-
import pywintypes
import xlrd
import xlwt
import copy
import sys
import re
import xlutils.copy
import os
import xml.dom.minidom
from xml.dom.minidom import Document
import sys
import re

reload(sys)
sys.setdefaultencoding("gbk")

def read_excel():
	data = xlrd.open_workbook("e:/bg.xlsx")
	files=os.listdir("e:/pc")
	print len(files)  #
	for table in data.sheets():    
		name = table.name    #表格名字
		tempName = name.replace(u'PC ',u'')
		tempName = tempName.replace(u' ',u'')
		# isFind = False
		for fileName in files:
			if (tempName in fileName):
				files1=os.listdir("e:/pc/" + fileName)
				files2=os.listdir("e:/pc/" + fileName + "/" + files1[0])  #language
				for xmlName in files2:  #en_us.xml
					if (xmlName == "en_US.xaml"):
						dom = xml.dom.minidom.parse("e:/pc/" + fileName + "/" + files1[0] + "/" + xmlName)
						root = dom.documentElement
						for row in range(table.nrows):
							keys = table.cell(row,0).value
							if ("x:Key" in keys):
								values = table.cell(row,3).value
							else:
								keys = table.cell(row,1).value
								if ("x:Key" in keys):
									values = table.cell(row,4).value
								else: 
									continue
							pattern = re.compile('"(.*)"')              			#用正则表达式筛选出双引号里的内容
							keys = pattern.findall(keys)[0]
							
							# print keys
							
							
							for node in root.getElementsByTagName('sys:String'):
								# print node.getAttribute("x:Key")               	#x:Key 的值
								# print node.firstChild.data                 		#内容
								if (node.getAttribute("x:Key") == keys):
									node.firstChild.data = values
									break
								
							doc = Document()
							doc.appendChild(root)
							# print help(doc)
							with open("e:/pc/" + fileName + "/" + files1[0] + "/" + "bg_BG.xaml", 'w') as f:
								f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
				# print fileName + ":" + name
				# isFind = True
				
		# if (isFind == False):
			# print "###" + name
		
	# table = data.sheet_by_name(u'')
	# print table.row_values(9)
	rows = table.nrows
	ans = []
	h = re.compile(r'\d') 
	for i in range(rows):
		ans.append(table.cell(i,0).value)
		# ans[i]=ans[i].replace(u'\xa0',u'')
		# ans[i]=ans[i].replace(u' ',u'')
		# ans[i]=ans[i].replace(u'、',u'')
		# ans[i]=h.sub('',ans[i])  
		# table.put_cell(0, i, 1, ans[i], 0)
		# print table.cell(i,0).value
		# print ans[i]  
	wb = xlutils.copy.copy(data)
	wb.save("d:/5.xls")
if __name__ == '__main__':
=======
# -*- coding:utf-8 -*-
import pywintypes
import xlrd
import xlwt
import copy
import sys
import re
import xlutils.copy
import os
import xml.dom.minidom
from xml.dom.minidom import Document
import sys
import re

reload(sys)
sys.setdefaultencoding("gbk")

def read_excel():
	data = xlrd.open_workbook("e:/bg.xlsx")
	files=os.listdir("e:/pc")
	print len(files)  #
	for table in data.sheets():    
		name = table.name    #表格名字
		tempName = name.replace(u'PC ',u'')
		tempName = tempName.replace(u' ',u'')
		# isFind = False
		for fileName in files:
			if (tempName in fileName):
				files1=os.listdir("e:/pc/" + fileName)
				files2=os.listdir("e:/pc/" + fileName + "/" + files1[0])  #language
				for xmlName in files2:  #en_us.xml
					if (xmlName == "en_US.xaml"):
						dom = xml.dom.minidom.parse("e:/pc/" + fileName + "/" + files1[0] + "/" + xmlName)
						root = dom.documentElement
						for row in range(table.nrows):
							keys = table.cell(row,0).value
							if ("x:Key" in keys):
								values = table.cell(row,3).value
							else:
								keys = table.cell(row,1).value
								if ("x:Key" in keys):
									values = table.cell(row,4).value
								else: 
									continue
							pattern = re.compile('"(.*)"')              			#用正则表达式筛选出双引号里的内容
							keys = pattern.findall(keys)[0]
							
							# print keys
							
							
							for node in root.getElementsByTagName('sys:String'):
								# print node.getAttribute("x:Key")               	#x:Key 的值
								# print node.firstChild.data                 		#内容
								if (node.getAttribute("x:Key") == keys):
									node.firstChild.data = values
									break
								
							doc = Document()
							doc.appendChild(root)
							# print help(doc)
							with open("e:/pc/" + fileName + "/" + files1[0] + "/" + "bg_BG.xaml", 'w') as f:
								f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
				# print fileName + ":" + name
				# isFind = True
				
		# if (isFind == False):
			# print "###" + name
		
	# table = data.sheet_by_name(u'')
	# print table.row_values(9)
	rows = table.nrows
	ans = []
	h = re.compile(r'\d') 
	for i in range(rows):
		ans.append(table.cell(i,0).value)
		# ans[i]=ans[i].replace(u'\xa0',u'')
		# ans[i]=ans[i].replace(u' ',u'')
		# ans[i]=ans[i].replace(u'、',u'')
		# ans[i]=h.sub('',ans[i])  
		# table.put_cell(0, i, 1, ans[i], 0)
		# print table.cell(i,0).value
		# print ans[i]  
	wb = xlutils.copy.copy(data)
	wb.save("d:/5.xls")
if __name__ == '__main__':
>>>>>>> origin/master
     read_excel()