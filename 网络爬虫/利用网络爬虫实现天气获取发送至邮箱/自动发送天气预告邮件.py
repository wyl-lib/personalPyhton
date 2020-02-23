import time
import smtplib
import requests
import random
import socket
import bs4
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

def get_content(url):
	header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding' : 'gzip, deflate',
	'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
	'Cache-Control' : 'max-age=0',
    'Connection' : 'keep-alive',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
	}
	timeout = random.choice(range(80, 180))
	while True:
		try:
			rep = requests.get(url,headers = header,timeout = timeout)
			rep.encoding = 'utf-8'
			break
		except socket.timeout as e:
			print( '3:', e)
			time.sleep(random.choice(range(8,15)))
		except socket.error as e:
			print( '4:', e)
			time.sleep(random.choice(range(20, 60)))
	return rep.text

def get_weather(url,data):
	air_list = []
	weather_list = []
	soup = BeautifulSoup(data,'lxml')
	div = soup.find('div',{'class' : 'forecast clearfix'})
	air_quality = div.find('strong',class_='level_2').string
	date = div.find('a',href='https://tianqi.moji.com/today/china/shandong/penglai').string
	ul = div.find('ul',{'class' : 'clearfix'})
	li = ul.find_all('li')
	
	#return li
	for day in li:
		if not isinstance(day,bs4.element.Tag):
			date = day.find('a',href='https://tianqi.moji.com/today/china/shandong/penglai').string
		#if day is not ' ':
		weather_list.append(day.string)
		wind_direction = day.find_all('em')      #风向
		wind_grade = day.find_all('b')       #风级   
		if not isinstance(day,bs4.element.Tag):
			air_quality = day.find('strong',class_='level_2').string.repalce('\n','').repalce(' ','')
			
		#print("'@data' {0},'@wind_grade' {1},'@wind_direction' {2},'@air_quality' {3}".format(date,wind_grade,wind_direction,air_quality))
	#air_quality = air_quality.repalce('','\n').repalce('',' ')
	Tempreture = weather_list[2]

	print("'wind_grade' {0},'wind_direction' {1}".format(wind_grade,wind_direction))
	print("'air_quality' {0}".format(air_quality))
	print("'data' {0},'Tempreture' {1}".format(date,Tempreture))
	
def send_email(email):
	'''
	sender = input('From: ')
	password = input('password: ')
	smtp_server = input('SMTP_Server: ')
'''

	##     FROM    ##
	sender = 'wyl1346788525@sohu.com'
	sent_host = 'smtp.sohu.com'
	sent_user = 'wyl1346788525@sohu.com'
	sent_pass = 'cxlgWYL1'

	##     TO     ##
	receivers = ['wyl1346788525@yach.net','1346788525@qq.com']

	message = MIMEText("您好，蓬莱天气如下（未经处理的）:{0}\n".format(result),'plain','utf-8')
	
	##   JUST USE TO DISPLAY   ##
	message['from'] = Header(sender,'utf-8')
	message['to'] = Header(receivers[1],'utf-8')
	message['subject'] = Header("您的天气预报详情!",'utf-8')
	
	server = smtplib.SMTP(sent_host,25)
	#server.set_debuglevel(1)
	server.login(sender,sent_pass)
	server.sendmail(sender,receivers,message.as_string())

	print("邮件发送成功")
	server.quit()

if __name__  == '__main__':
	url = 'http://tianqi.moji.com/weather/china/shandong/penglai'
	data = get_content(url)
	result = get_weather(url,data)
	#print(result)
	#send_email(result)
