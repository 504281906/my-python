# -*- coding=utf-8 -*-
import math
import os
import win32clipboard as w
import win32con
import string
import sys
import pyHook
import pythoncom
import time
import socket
from PIL import ImageGrab
import os,sys
import win32api, win32con
import os
import zipfile
import codecs
import base64

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d
 
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def reverse(a):
    b=''
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    return b;

def go():
    a=getText()
    c=unicode(a,'gb2312');
    b=reverse(c)
    b=b.encode('gbk')
    setText(b)
    a=getText();
    print a

def onKeyboardEvent(event):
    if (event.Ascii==96):
        #time.sleep(3)
        go()
        return True
    else:
        return True

if __name__=='__main__':
    hk=pyHook.HookManager()
    hk.KeyDown=onKeyboardEvent
    hk.HookKeyboard()
    pythoncom.PumpMessages()
    os.system("pause")