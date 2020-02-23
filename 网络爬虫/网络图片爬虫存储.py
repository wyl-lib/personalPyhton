import os
import requests

root = "F:/基于树莓派的家庭监控系统/网络爬虫/pics/"
url = "https://cdn.liaoxuefeng.com/cdn/files/attachments/00138676512923004999ceca5614eb2afc5c0efdd2e4640000/0.png"
path = root + url.split('/')[-1]#存取数据的原始文件名
try:
	if not os.path.exists(root):#根目录是否存在，否则创建
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		print("【链接到url获取文件】")
		with open(path,'wb') as f:#打开文件dongying.png并将其定义为文件标识符f
			f.write(r.content)#将返回内容写入文件dongying.png中
				#r.content：返回内容的二进制形式
			f.close()
			print("【文件保存成功】")
	else:
		print("【文件已存在】")
except:
	print("爬取失败！！")
