#xpath的基本使用方法

from lxml import etree

web_data = '''
	<div>
		<ul>
			 <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-inactive"><a href="link3.html">second item</a></li>
             <li class="item-1"><a href="link4.html">third item<</a></li>
             <li class="item-0"><a href="link5.html">fourth item</a>
         </ul>
    </div>
'''
#(1)etree.tostring(html)将标签补充齐整,是html的基本写法
html = etree.HTML(web_data.lower())
print("html_1 {}\n".format(html))
print(type(html))
result = etree.tostring(html)
print("\n",type(result))
print('''result.decode("utf-8")_1 \n{}\n\n'''.format(result.decode("utf-8")))

#(2.0)获取标签里的内容,获取a标签的所有内容，a后面就不用再加“/”否则报错
html = etree.HTML(web_data)
print(type(html))
html_data = html.xpath('/html/body/div/ul/li/a')
print("html_2.0 {}".format(html))
for i in html_data:
	print("i.text_2.0 {}\n".format(i.text))
print("\n")

#(2.1)写法二(直接在需要查找的标签后面加一个/text()就行)
html = etree.HTML(web_data)
html_data = html.xpath('/html/body/div/ul/li/a/text()')
print("html_2.1 {}".format(html))
for i in html_data:
	print("i_2.1 {}\n".format(i))
print("\n")

#(3)使用pasrse打开html文件
html = etree.parse("xpath_data.xml")
html_data = etree.tostring(html,pretty_print=True)
res = html_data.decode('utf-8')
print(res)
