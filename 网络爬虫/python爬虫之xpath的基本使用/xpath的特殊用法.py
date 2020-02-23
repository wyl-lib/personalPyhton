#xpath特殊用法
from lxml import etree
#(1)starts-with解决标签相同开头的属性值
html="""
    <body>
        <div id="aa">aa</div>
        <div id="ab">ab</div>
        <div id="ac">ac</div>
    </body>
"""
example = etree.HTML(html)
content = example.xpath("//div[starts-with(@id,'a')]/text()")
for each in content:
	print(each)
print("(1) is over.\n")

#(2)string(.)标签套标签
html1="""
    <div id="a">
    left
        <span id="b">
        right
            <ul>
            up
                <li>down</li>
            </ul>
        east
        </span>
        west
    </div>
"""
pil = etree.HTML(html1)
data = pil.xpath("//div[@id = 'a']")[0]
#print("data's type is {}".format(type(data)))
#print("data {}\n".format(data))
info = data.xpath("string(.)")

#replace是将新的字符串替换旧字符串，第三个参数是max，替换不超过max次；
content = info.replace('\n','').replace(' ','')
for i in content:
	print(i)
print("(2) is over\n")

html2 = '''
<li>
<em>南风</em>
<b>5-6级</b>
</li>
'''
for h in html2:
    tds = h('li')
    print(tds)
print(html2)