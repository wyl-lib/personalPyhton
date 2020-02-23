#利润计算
Profit = eval(input())
if Profit>0:
    if Profit<=100000:
        Profit *= 0.1
        print(int(Profit))
    #Profit %= 10000
    elif Profit<=200000:
        Profit = (Profit-100000)*0.075 + 10000
        print(int(Profit))
    elif Profit<=400000:
        Profit = (Profit-200000)*0.05 + 17500
        print(int(Profit))
    elif Profit<=600000:
        Profit = (Profit-400000)*0.03 + 27500
        print(int(Profit))
    elif Profit<=1000000:
        Profit = (Profit-600000)*0.015 + 33500
        print(int(Profit))
    else:
         Profit = (Profit-600000)*0.01 + 36500
         print(int(Profit))
