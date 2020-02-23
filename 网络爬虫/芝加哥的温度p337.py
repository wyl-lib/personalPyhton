import urllib.request
import lxml.etree
from lxml.cssselect import CSSSelector

url ='https://www.yahoo.com/news/weather/un'+\
     'ited-states/illinois/chicago-2379574/'
response = urllib.request.urlopen(url)
html = response.read()

parer = lxml.etree.HTMLParse(encording = 'utf-8')
doctree = lxml.etree.fromstring(html,parser)

div = CSSelector("div.'day-temp-current temp-c'")
temp = div(doctree)[0].text[0:-1]
print("The temperature in Chicago is",temp)
