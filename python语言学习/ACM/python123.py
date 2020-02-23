list = ["Hello"]
str = "Hello World"
str1 = str.split("")
count=1
x= eval(input())
print(len(str1))

if(x==0):
    print("Hello World")
if x<0:
    for i in range(0,5):
        print(list[i])
if x>0:
    for i in range (0,len(str1)):
        count+=1
        if count%2==0:
            print()
        else:
            print(str1[i],end="")
    