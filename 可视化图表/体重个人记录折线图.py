import numpy as np 
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from datetime import date, timedelta

d2 = date(2020, 2, 29)
d1 = date(2020, 2, 1)
delta = d2 - d1
month_2=[]

for i in range(delta.days + 1):
    month_2.append(d1 + timedelta(days=i))
    #print(d1 + timedelta(days=i))
    
month_3=[]
d2 = date(2020, 3, 31)
d1 = date(2020, 3, 1)
delta = d2 - d1
for i in range(delta.days + 1):
    month_3.append(d1 + timedelta(days=i))

xs = month_2
'''
    生成横纵坐标信息
    dates = ['2/05','2/06','2/07','2/08','2/09','2/10','2/11',
    '2/12','2/13','2/14','2/15','2/16','2/17','2/18','2/19',
    '2/20','2/21','2/22','2/23','2/24','2/25','2/26','2/27']
    #xs = [datetime.strptime(str(d), '%Y-%m-%d').date() for d in month_2]
    '''


ys = [86.6 ,86.2 ,85.5 ,85.1 ,84.4 ,84.1 ,83.9 ,83.6 ,83.5 ,84.0 ,
    83.5 ,83.7 ,83.1 ,82.9 ,82.3 ,82.1 ,81.5 ,81.8 ,81.9 ,82.1 ,
    81.9 ,81.8 ,81.5 ,81.8 ,81.8 ,81.8 ,81.8 ,81.8 ,81.8 ]

# 配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Plot
plt.plot(xs,ys,'c')#青色
plt.plot(xs, ys,'bo')#b蓝色 m品红色点
plt.gcf().autofmt_xdate()  # 自动旋转日期标记

plt.title("weightRecord")#Weight
plt.xlabel("date")#X轴名称
plt.ylabel("nowWeigth")#Y轴名称

#plt.xlim(5,28)#X轴范围
plt.ylim(80,87)#Y轴范围

plt.show()