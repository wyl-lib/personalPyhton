#yanTai PengLai
import socket
import requests
from lxml import html
from lxml import etree

def getHtml(url):
	try:
		r = requests.Session().get(url)
		print("get了，继续\n")
		print("raise_stsus = ",r.raise_for_status())
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "获取中遇到问题"

def selectText(demo,Weather_list):
	tree = etree.HTML(demo)
	Fix_tree = html.fromstring(demo)

	ul = Fix_tree.xpath('//div[@class="w-forecast mb10"]//ul')[0]
	result = ul.xpath("string(.)")
	#print("{}\n".format(type(result)))
	#print(ul)
	#content = result.replace(' ','')
	for i in result:
		Weather_list.append(i)
		#print(i)
	print(Weather_list)

def socket():
	try:
		print("It Doesn't Matter")

	except socket.timeout as e:
		print("3",e)
		time.sleep(random.choice(range(8,15)))

def main():
	socket()
	Weather_list = []
	url = 'https://tianqi.8684.cn/shandong_penglai'
	demo = getHtml(url)
	#print(demo)
	selectText(demo,Weather_list)

main()