import numpy as np 
import time
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib import pyplot as plt

from datetime import date, timedelta

d2 = date(2020, 2, 29)
d1 = date(2020, 2, 1)
delta = d2 - d1
date=[]

for i in range(delta.days + 1):
    print(timedelta(days=i))
    print(d1 + timedelta(days=i))
    date.append(d1 + timedelta(days=i))
    
'''
0:00:00
2020-02-01
1 day, 0:00:00
2020-02-02
2 days, 0:00:00
2020-02-03
3 days, 0:00:00
2020-02-04
4 days, 0:00:00
2020-02-05
5 days, 0:00:00
2020-02-06
'''