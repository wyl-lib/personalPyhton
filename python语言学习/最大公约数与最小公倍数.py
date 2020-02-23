#最大公约数与最小公倍数
number = input()
m = (number.split(" "))[0]
n = (number.split(" "))[1]
CommonDiv = 0
CommonMul = 0
#m,n = map(int,input().strip('"').split(","))
m = int(m)
n = int(n)
if m>n:
    max = m
    min = n
else:
    max = n
    min = m

another = min
one = max
#公约数
for i in range(1,int(max/2)+1,1):
    if(m%i==0 and n%i==0):
        CommonDiv = i
        
#公倍数
for i in range(1,min+1,1):
    if(CommonMul>=another):
        break
    one = max*i
    for j in range(i,max+1,1):
        another = min*j
        if(one==another):
            CommonMul = one
            break

print(CommonDiv,CommonMul)
