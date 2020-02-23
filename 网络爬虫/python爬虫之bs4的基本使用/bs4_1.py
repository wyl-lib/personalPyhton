import requests
import bs4
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
r = requests.get(url)#获取网址
r.encoding = r.apparent_encoding#编译显示中文
r.raise_for_status#返回网址状态

demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())#输出按照标准格式

#####################
import re
soup.title#输出标签
soup.find_all('a')#查询a标签
soup.find_all('p',"course")#查询带有course字符串属性的p标签
soup.find_all(id = re.compile('link1'))#查询搜索id为link1的内容
soup.a.next_sibling#标签 a 的下一个标签

for tag in soup.find_all(True):
	print(tag.name)#输出所有的标签名

for zisun in soup.findAll('body',recursive=False):
    print(zisun)#是否对子孙标签全部检索ex：false(不包含)


soup.find_all(string = re.compile("Python is"))
##输出整个页面中带有这个字符串的所有信息检索出来。
