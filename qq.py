# -*- coding: utf-8 -*-
import re
import os


def start_find_chinese(dir):
	global find_count
	# print(dir)
	files=os.listdir(dir)
	with open('record.txt', 'a') as outfile:
		for fileName in files:
			# print(fileName)
			goName = dir + "/" + fileName;
			# print(goName)
			if(os.path.isdir(goName)):
				start_find_chinese(goName)
				# break
			extName=os.path.splitext(fileName)[1]
			
			if (extName == ".xaml"):
				print(goName)
				with open(goName, 'rb') as infile:
					while True:
						content = infile.readline()
						if re.match(r'(.*"[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)', content.decode('utf-8')):
							outfile.write(content)
							find_count += 1;
						if not content:
							break
	return find_count					

# start to find
if __name__ == '__main__':
	find_count = 0
	dir = input(r"Input U PathDir:").strip()
	# dir = "E:\SVN\AiTeacher\Aiteacher.AddIns\AiTeacher.Courseware\View"
	# dir = "E:\SVN\AiTeacher\Aiteacher.AddIns\AiTeacher.Courseware"
	count = start_find_chinese(dir)
	print("find complete! count =", count)