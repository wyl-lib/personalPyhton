import requests
from bs4 import BeautifulSoup
from lxml import html
import bs4

url = 'https://www.tianqi.com/dongying/7/'
r = requests.Session().get(url)
r.encoding = r.apparent_encoding
r.raise_for_status
demo = r.text
print(demo)

soup = BeautifulSoup(demo,"html.parser")
print(soup)

tab = soup.find_all("h1")
print(tab)
tab1 = soup.find_all("span")
print(tab1)
tab2 = soup.find_all("p")
print(tab2)
#for dl in soup.find("div").chlidren:


##xpath
page = requests.Session().get(url)
tree = html.fromstring(page.text)
result = tree.xpath('''//div[@class="tit_img01"]/p/text()''')
print(result)
