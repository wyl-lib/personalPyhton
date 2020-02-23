#coding=utf-8
import requests
from lxml import html

j = 0
url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
page = requests.Session().get(url)
data = html.fromstring(page.text)

result = data.xpath('''//tbody[@class="hidden_zhpm"]//td/text()''')
for i in result:
	j += 1
	if j<100:
		if j%13!=0:
			print(i)
		else:
			print("\n")

