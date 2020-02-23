import bs4
import requests
from bs4 import BeautifulSoup
from lxml import html

j = 0
tplt = "{0:{1}^10}"
url='https://movie.douban.com/' # 需要爬数据的网址
page=requests.Session().get(url) # 维持一个回话
#print(type(page))
tree=html.fromstring(page.text) 

# 在解析xml格式时，将字符串转换为element对象，解析树的根节点
result=tree.xpath('//td[@class="title"]//a/text()') #获取需要的数据

print(tplt.format("Movie_Name Top 10 of Week:",chr(12288)))
for i in result:
	if j<10:
		print(tplt.format(result[j],chr(12288)))
	j += 1
	#print(result)
