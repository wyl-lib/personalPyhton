from lxml import etree

html = '''
<table border='1'>
<tr>
	<td>Month</td>
</tr>
<tr>
	<td>January</td>
	<td>Febuary</td>
</tr>	
</table>
'''
tree = etree.HTML(html)
print(type(tree))# <class 'lxml.etree._Element'>
page = etree.tostring(tree)
print("{}\n".format(type(page)))# <class 'bytes'>

hey = page.decode("utf-8")
print(hey)#it has been decode with 'utf-8'
print(type(hey))# <class 'str'>

result = tree.xpath("//table[@border = '1']/tr/td/text()")
result1 = tree.xpath('//tabel[@border = "1"]//td/text()')
#for i in result:/
	#print("\n{}".format(i))
for j in result1:
	print("\n{}".format(j))
