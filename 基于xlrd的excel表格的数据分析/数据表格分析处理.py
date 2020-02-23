import xlrd

'''
常用单元格中的数据类型

    0. empty（空的）,1 string（text）, 2 number,
    3 date, 4 boolean, 5 error， 6 blank(空白表格)
'''
filename = "D:\WriteCode\PyhtonCode\测试表格Test1.xlsx"

data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。

names = data.sheet_names()    #返回book中所有工作表的名字

print("names : {}".format(names))


table = data.sheet_by_name("test1") #返回所有工作簿

nrows = table.nrows #返回列数

print(nrows)

print(table.cell(1,0))  #Rows，Line

print(table.row(1)) #返回由该“行”中所有的单元格对象组成的列表

print(table.col_slice(1, start_rowx=0, end_rowx=None))  #返回由该列中所有的单元格对象组成的列表


