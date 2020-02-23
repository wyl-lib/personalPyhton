import requests
import bs4
from bs4 import BeautifulSoup

#提交ip的url链接接口

url = "http://m.ip138.com/ip.asp?ip="#解析出来的接口

#http://ip38.com/ip.php?ip=192.168.43.114
def gethtml(url):
	try:
		r = r.requests.get(url + '202.204.80.112')
		return r.text
	except:
		return "Error"

def intoList(demo,ulist):
	soup = BeautifulSoup(demo,"html.parser")
	for tr in soup.find('body').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('font')
			ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])

def printaddr(ulist,num):
	space = "{0:^10}\t{1:{5}^8}\t{2:^8}\t{3:^8}\t{4:^8}"
	print(space.format("【ip地址查询】","您查询的IP：","ipaddr","IP详细地址：","addr"))
	for i in range(num):
		u = ulist[i]
		print(space.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))

def main():
	num = 5
	ulist = []
	url = "http://m.ip138.com/ip.asp?ip="
	demo = gethtml(url)
	intoList(demo,ulist)
	printaddr(ulist,num)

main()