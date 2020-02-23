#分段函数求值
x = eval(input())
if(x<1):
    y = x
if(x<10 and x>=1):
    y = 2*x-1
if(x>=10):
    y = 3*x-11

print(y)
