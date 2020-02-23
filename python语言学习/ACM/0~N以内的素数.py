#求0~N之间的素数
N = eval(input())
for i in range(2,N+1):
    if(i==2):
        print(i)
        continue
    if(i==3):
        print(i)
        continue
    I = (int)(i/2)+1
    for j in range(2,I):
        if(i%j==0):
            break
        if(i%j!=0 and j==I-1):
            print(i)
            break
