
# -*- coding=utf-8 -*-
import sys
import os
from platform import system
import re


def getmp3filelist(path):
    filetype = "doc"
    mp3file = ""
    mp3filelist = [mp3file for mp3file in os.listdir(path) \
                   if len(mp3file.split(".")) == 2 and mp3file.split(".")[1] == filetype]
    return mp3filelist


def writemp3filelist(mp3filelist,filename="testPython.txt"):
    with open(filename,"w") as w_file:
        w_file.write("Total:%s%s"%(len(mp3filelist),os.linesep))
        for mp3file in mp3filelist:
            w_file.write("%s%s"%(mp3file,os.linesep))
    return None
#path = os.getcwd()
#path = "C:\\Users\\Administrator\\Desktop"
#writemp3filelist(getmp3filelist(path))
resp = 'asdasdsadsadasadaddasdasd'
pre_login_str = re.match(r'a', resp)
print(pre_login_str)