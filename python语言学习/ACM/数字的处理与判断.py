#数字的处理与判断
i = 10
count = 1
StrWithThird = ""
number = eval(input())
if(number<100000):
    while(i<100000):
        #print(number,i,number/i)
        if(int(number/i)<=0):
            break
        else:
            count += 1
            i *=10

    print(count)

    for i in range(1,count+1):
        ResultWithSpace = int(number/(10**(count-i)))
        StrWithThird += str(ResultWithSpace)
        if(i==count):
            print(ResultWithSpace,end="\n")
        else:
            print(ResultWithSpace,end=" ")
        number -= ResultWithSpace*(10**(count-i))

    #print(StrWithThird)
    #print(len(StrWithThird),StrWithThird[0])
    for i in range(len(StrWithThird)-1,-1,-1):
        print(StrWithThird[i],end="")
