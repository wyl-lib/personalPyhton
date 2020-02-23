import requests

lists = ['python', 'php', 'Java']

for i in lists:
    url = 'http://www.baidu.com/s?wd=%s' % (str(i))
    r = requests.get(url)
    print(r.url)