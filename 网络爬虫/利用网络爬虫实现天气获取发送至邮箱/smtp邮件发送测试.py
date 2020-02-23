#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.sohu.com"  #设置服务器
mail_user="wyl1346788525@sohu.com"    #用户名
mail_pass="cxlgWYL1"   #口令  

sender = 'wyl1346788525@sohu.com'
##搜狐向QQ发送邮件
receivers = ['1346788525@qq.com','2436632009@qq.com','wyl1346788525@sohu.com','wyl1346788525@yeah.net','wyl1346788525@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

##邮件的来去地址
message = MIMEText('Here is email_text.Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')
message['To'] =  Header(receivers[0], 'utf-8')

##  邮件内容    经过Header函数编译成utf-8格式的邮件  ##
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
try:
    SmtpObj = smtplib.SMTP()  # 创建 SMTP 对象
    print("SMTP complete")

    SmtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    print("connect complete")		# mail_host服务器 地址

    SmtpObj.login(mail_user,mail_pass)  
    print("login complete")

##  SMTP.sendmail(from_addr, to_addrs, msg)  ##
##  from发送者地址   to接受者地址    msg发送的内容
    SmtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")