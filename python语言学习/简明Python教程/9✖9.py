def chengfa():
    for i in range(1,10):
        for j in range(1,i+1):#end = ""输出后不自动换行
                        # print(xyz,end="")
            print("{0} * {1} = {2}  ".format(i,j,(i*j)),end = "")
        print("\n")

def main():
    print(u"9 * 9 乘法表：")
    chengfa()

main()
