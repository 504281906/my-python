# -*-coding:utf:8 -*-
from socket import *
import os.path
import sys
target = ("113.247.182.14",6002)
#target = ("127.0.0.1",6666)
s=socket(AF_INET,SOCK_STREAM)
s.connect(target)
name='D:/monitor.txt'
text=open(name).read()
s.send(text)
gg='66 is great'
s.send(gg)
ss=s.recv(4096)
s.close()
print ss
s.close()