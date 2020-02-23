#问题 1255: [蓝桥杯][算法提高]能量项链

N = eval(input())

if(N>=4 and N<=1000):
    StrRing = input()
    #print(type(StrRing))
    list1 = StrRing.split(" ")
    SumValue = 0
    list2 = []

    if(list1[0]==''):
        del list1[0]    
    for i in range(0,N,1):
        if(eval(list1[i])>999 or eval(list1[i])<1):
            Flag_Bead = False
            break
        else:
            list1[i] = int(list1[i])
            if(i>=N-1):
                Flag_Bead = True
    
    if(Flag_Bead):
        '''
        for i in range(0,N,1):
            for j in range(0,N-1-i,1):
                if(list1[j]>list1[j+1]):
                    exchange = (list1[j])
                    list1[j] = (list1[j+1])
                    list1[j+1] = exchange                        

        #print("list1 {0},type {1}".format(list1[1],type(list1[1])))
        MaxValue = list1[N-1]
        for i in range(N-1,0,-1):
            list1[i] = list1[i-1]

        list1[0] = MaxValue 
        print("After Sort list1",list1)
'''
        for i in range(0,N,1):
            if(i<N-1):
                list2.append((list1[i],list1[i+1]))
            if(i==N-1):
                list2.append((list1[i],list1[0]))

        for i in range(1,N,1):
            print(SumValue)
            SumValue += list2[0][0]*list2[i][0]*list2[i][1]
        if SumValue<=2.1*10**9:
            print(SumValue)
    
