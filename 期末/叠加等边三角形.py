# 叠加等边三角形

import turtle as t

'''
t.speed(2)
#t.setup()
#内等边三角形
t.forward(60)
t.right(120)
t.forward(60)
t.right(120)
t.forward(60)

#外边等边三角形
t.right(60)
t.forward(60)
t.right(120)
t.forward(120)
t.right(120)
t.forward(120)
t.right(120)
t.forward(60)
t.right(60)
'''
for i in range(1,8):
    if(i<=4):
        t.forward(60)
    else:
        t.forward(120)
    if(i!=3):
        t.right(120)
    else:
        t.right(60)
    
    
