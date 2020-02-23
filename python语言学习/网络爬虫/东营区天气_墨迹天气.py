import requests
from bs4 import BeautifulSoup

url = 'https://www.tianqi.com/dongying/15'
r = requests.get(url)
r.encoding = r.apparent_encoding
r.raise_for_status
demo = r.text

soup = BeautifulSoup(demo,"html.parser")
print(soup.title)
