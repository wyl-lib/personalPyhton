str=input("请输入带有单位的温度数值:")

if str[-1] in ["C","c"]:
    F = 1.8*eval(str[0:-1]) + 32
    print('转换后的温度{:.2f}F'.format(F))
elif str[-1] in ['F','f']:
    C =(eval(str[0:-1]) - 36)/1.8
    print('转换后的温度{:.2f]}C'.format(C))
else:
    print("请按格式输入")
