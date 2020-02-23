#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
 
mail_host="smtp.sohu.com"  #设置服务器
mail_user="wyl1346788525@sohu.com"    #用户名
mail_pass="cxlgWYL1"   #口令  

sender = 'wyl1346788525@sohu.com'
receivers = ['1346788525@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')	
message['To'] =  Header("测试", 'utf-8')		
subject = 'Python SMTP 邮件测试'			#标题
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText('这是蕴含附件的Python 邮件发送测试……', 'plain', 'utf-8'))
 
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('smtp涵盖附件发送测试 .py', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字

	#内容 处置				# 附 件
att1["Content-Disposition"] = 'attachment; filename="Thetest_file.py"'
message.attach(att1)#attach 连接

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")