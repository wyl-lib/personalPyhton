#找三个数中的最大值
str = input()
a = str.split(" ")

while(a[0]!=None and a[1]!=None):
    x1 = eval(a[0])
    x2 = eval(a[1])
    x3 = eval(a[2])
    max = x3
    if(x1>x2):
        if(x1>x3):
            max = x1
        else:
            max = x3
    else:
        if(x2>x3):
            max = x2
        else:
            max = x3

    print(max)
    
    str = input()
    a = str.split(" ")

