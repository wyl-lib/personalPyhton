#母牛的故事（时间超限50%）
import time

def CaculateCowNumber(year):
    if(year<5):
        return year
    else:
        return CaculateCowNumber(year-1)+CaculateCowNumber(year-3)
    
if __name__ == '__main__':
    while(True):
        Year =eval(input())
        if(Year<1 or Year>54):
            break
        else:
            start = time.perf_counter()
            print(CaculateCowNumber(Year))
            end = time.perf_counter()
            
            print(end-start)
