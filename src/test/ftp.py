'''
Created on 2014年1月24日

@author: Administrator
'''
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
from ftplib import FTP 

prj_path=r'D:\data\workspace\zhzs'#必须是绝对路径
filepath=r'D:\data\workspace\zhzs\target\zhzs.war'
ftp_user='zhzs'
ftp_password='zhzs'


def ftp_up(): 
    ftp=FTP() 
    ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息 
    try:
        ftp.connect('192.168.1.114',21)#连接 
        print('ftp连接成功')
        ftp.login(ftp_user,ftp_password)#登录，如果匿名登录则用空串代替即可 
        print('登陆成功')
        #print ftp.getwelcome()#显示ftp服务器欢迎信息 
        #ftp.cwd('xxx/xxx/') #选择操作目录 
        bufsize = 1024#设置缓冲块大小 
        if os.path.exists(filepath):
            file_handler = open(filepath,'rb')#以读模式在本地打开文件 
            print('read success')
            print(os.path.basename(filepath))
            ftp.storbinary('STOR %s' % os.path.basename(filepath),file_handler,bufsize)#上传文件 
            ftp.set_debuglevel(0) 
            file_handler.close() 
        else:
            print('filepath not exists')
        ftp.quit() 
    except Exception as e:
        print (str(e))
        return False    
    print ("ftp up end") 
 
def ftp_down(): 
    ftp=FTP() 
    ftp.set_debuglevel(2) 
    ftp.connect('192.168.1.114',21) 
    ftp.login('admin','zz412') 
    #print ftp.getwelcome()#显示ftp服务器欢迎信息 
    #ftp.cwd('xxx/xxx/') #选择操作目录 
    bufsize = 1024 
    filename = "testPython.txt" 
    file_handler = open(filename,'wb') #以写模式在本地打开文件 
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler.write,bufsize)#接收服务器上文件并写入本地文件 
    ftp.set_debuglevel(0) 
    file_handler.close() 
    ftp.quit() 
    print ("ftp down end") 


def mvn_pack():
    cmds = [prj_path[0:2],'cd '+prj_path,'mvn clean -o install -Dmaven.test.skip=true']
    os.system('&&'.join(cmds))
    print('mvn pack end')
    ftp_up()

#ftp_down()
mvn_pack()
