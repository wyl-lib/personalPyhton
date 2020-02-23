import requests

url = "http://ip38.com/ip.php?ip="
try:
	
	r = requests.get(url + "192.168.43.114")
	demo = r.text
	r.status_code
	r.encoidng = r.apparent_encoding
	print(demo[500:])
except:
	print("爬取失败")