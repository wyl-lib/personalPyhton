#Tempconert.py
TempStr = input("请输入带有符号的温度值:")
            

if TempStr[-1] in ['F','f']:        #为什么是“-1”！！
                                    #去掉后头的“单位”然后通过if语句判断
                                    #数字后的是C or F,执行下面的语句。
    
    C = (eval(TempStr[0:-1]) - 32)/1.8  #这里头的[]意思是从第0位开始到最后
                                    #“-1”位//例如：24c 通过这个最终得到"24"

    print("转换后的温度是{:.2f}C(摄氏度)".format(C))   #“：”输出，“.2f”小
                                                #数后两位，后面的'C'加在后面

elif TempStr[-1] in ['C','c','a']:    #a in b，表示判断a是否在b其中，如果存
                                      #在则返回True，否则返回False。      

   F = 1.8*eval(TempStr[0:-1]) + 32    #eval函数将字符串当成有效Python表达式
                                       #来求值，并返回计算结果       

    print("转换后的温度是{:.2f}F(华氏度)".format(F))  #与上面一样输出结果

else:
  
    print("输入格式错误")
