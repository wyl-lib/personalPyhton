#Tempconert.py
TempStr = input("请输入带有符号的温度值:")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C(摄氏度)".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F(华氏度)".format(F))
else:
    print("输入格式错误")
