# -*- coding:utf-8 -*-
import pywintypes
import xlrd
import xlwt
import copy
import sys
import re
import xlutils.copy
# reload(sys)
# sys.setdefaultencoding("utf-8")

def read_excel():
	data = xlrd.open_workbook("d:/1.xls")
	
	table = data.sheet_by_name(u'Sheet1')
	# print table.row_values(9)
	rows = table.nrows
	ans = []
	h = re.compile(r'\d')
	for i in range(rows):
		ans.append(table.cell(i,0).value)
		ans[i]=ans[i].replace(u'\xa0',u'')
		ans[i]=ans[i].replace(u' ',u'')
		ans[i]=ans[i].replace(u'、',u'')
		ans[i]=h.sub('',ans[i])   #去掉字符串中的数字
		table.put_cell(0, i, 1, ans[i], 0)
		# print table.cell(i,0).value
		# print ans[i]
	wb = xlutils.copy.copy(data)
	wb.save("d:/3.xls")
if __name__ == '__main__':
     read_excel()