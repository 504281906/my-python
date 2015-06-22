import re
import urllib
import sys
a = raw_input('input url: ')

s = urllib.urlopen(a)
s1 = s.read()


def getimg(aaa):
	reg = re.compile(r'src="(.*?.[jpg|png])" [pic_ext=|><br><br><img]')
	l = re.findall(reg, aaa)
	tem = 0
	for x in l:
		tem += 1
		print x
		urllib.urlretrieve(x,'%s.jpg' % tem)

getimg(s1)