tem = input ("请输入带有符号的温度值：")
if tem [-1] in ["F","f"]:
    C = (eval(tem[0:-1]) - 32)/1.8
    print("转换后的摄氏度温度为{:.2f}C".format(C))
elif tem [-1] in ["C","c"]:
    F = 1.8*eval(tem[0:-1]) + 32
    print("转换后的华氏度为{:.2f}F".format(F))
else :
    print("您的输入有误")
