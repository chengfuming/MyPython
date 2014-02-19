#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText

#这是一个测试发送邮件的脚本
mail_to="sxjun1904@qq.com"

def send_mail(to_list,sub,content):
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.qq.com"
    mail_user="49170232"
    mail_pass=""
    mail_postfix="qq.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        print(msg)
        s.connect(mail_host)
        print("连接邮件服务器成功")
        s.login(mail_user,mail_pass)
        print("登陆成功")
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print (str(e))
        return False
if __name__ == '__main__':
    if send_mail(mail_to,"test","好玩的亚比"):
        print ("发送成功")
    else:
        print ("发送失败")
    