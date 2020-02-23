# coding : UTF-8
from lxml import etree
from lxml import html
from lxml.etree import tostring
import requests

ulist = []
url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
page = requests.Session().get(url)
page.encoidng = page.apparent_encoding
data = html.fromstring(page.text)
getDate = data.xpath("//tbody[@class='hidden_zhpm']//tr/td/text()")
demo = "{0:{2}^10}\t{1:^10}"
print(demo.format("排名","大学名称",chr(12288)))

newlist = []
for i in getDate:

	ulist = [str(a) for a in i]
	newlist.append(ulist)

	
for j in range(20):
	u = newlist[j]
	print(demo.format(u[0],chr(12288)))
	#a = etree.tostring(i,method="text")

	#ulist = append(b)

#for i in getDate:

	#print("type of the getDate is {}\n".format(type(i)))

