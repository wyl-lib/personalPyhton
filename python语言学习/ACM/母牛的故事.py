#母牛的故事
import time

list = [0]*55
list[0] = 1
list[1] = 2
list[2] = 3
list[3] = 4

while(True):
    Year = eval(input())
    if(Year<=0):
        break
    else:
        if(Year<=4):
            CowNum = Year
            print(CowNum)
        else:
            for i in range(4,Year,1):
                start = time.perf_counter()
                list[i] = list[i-1]+list[i-3]

            end = time.perf_counter()
            print(end-start)
            
            print(list[Year-1])
            
