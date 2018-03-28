# -*- coding: utf-8 -*-
import re
import os

def start_find_chinese(dir):
	global find_count
	# print(dir)
	files=os.listdir(dir)
	
	for fileName in files:
		# print(fileName)
		goName = dir + "/" + fileName;
		# print(goName)
		if(os.path.isdir(goName) & (fileName != "Styles") & (fileName != "AiTeacherUI")):
			start_find_chinese(goName)
			# break
		extName=os.path.splitext(fileName)[1]
		
		if ((extName == ".xaml") & (os.path.splitext(fileName)[0] != "zh_CN") & (os.path.splitext(fileName)[0] != "en_US")):
			# print(goName)
			flag = True
			with open(goName, 'rb') as infile:
				while True:
					content = infile.readline()
					if re.match(r'(.*"[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)', content.decode('utf-8')):
						if (flag):
							flag = False
							outfile.write("\r\n".encode(encoding = 'utf-8'));
							outfile.write(goName.encode(encoding = 'utf-8'))
							outfile.write(":\r\n   ".encode(encoding = 'utf-8'));
						outfile.write(content)
						find_count += 1;
					if not content:
						break
	return find_count					

# start to find
if __name__ == '__main__':
	find_count = 0
	outfile = open('record.txt', 'wb+')
	dir = input(r"Input U PathDir:").strip()

	count = start_find_chinese(dir)
	print("find complete! count =", count)