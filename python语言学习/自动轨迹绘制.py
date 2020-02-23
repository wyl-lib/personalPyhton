#自动轨迹绘制.py
import turtle as t

t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
'''
300,0,144,1,0,0
300行进距离，
0左转，1右转
144转动角度
1，0，0表示RGB通道颜色
'''

#数据读取
datalist=[]
f = open("data.txt")
for line in f:
	line = line.replace("\n","")
	datalist.append(list(map(eval,line.split(","))))
f.close()

#自动绘制
for i in range(len(datalist)):
	t.pencolor(datalist[i][3],datalist[i][4],datalist[i][5])
	t.fd(datalist[i][0])
	if datalist[i][1]:
		t.right(datalist[i][2])
	else:
		t.left(datalist[i][2])

