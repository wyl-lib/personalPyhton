import requests
keyword = "Python"

try:
    url = "http://www.baidu.com/s"
    kv = {'wd':keyword}
    r = requests.get(url,params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("≈¿»• ß∞‹")
import requests
keyword = "Python"

try:
    url = "http://www.baidu.com/s"
    kv = {'wd':keyword}
    r = requests.get(url,params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("≈¿»• ß∞‹")
