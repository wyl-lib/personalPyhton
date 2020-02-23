import bs4
import requests
from bs4 import BeautifulSoup

def getHTML(http):#获取网页
    try:
        r = requests.get(http)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"
    
def soupBeautiful(Ulist,demo):#煲汤调用bs4库，此函数主要用来存储网页的信息到列表中，然后后续进行索引。
    soup = BeautifulSoup(demo,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")#append()用于在列表末尾添加新的对象
            Ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
           #print(Ulist)
#extend()方法只接受一个列表作为参数，
    #并将该参数的每个元素都添加到原有的列表中。
        
def printResult(Ulist,num):#输出爬取结果
    print("\n\r\t")############｛5｝表示输出模版采用第五位
    space = "{0:^10}\t{1:{5}^16}\t{2:^8}\t{3:^8}\t{4:^8}"#设置一个新的输出模版变量
    print(space.format("排名","大学名称","总分","类别","所属地",chr(12288)))#使用中文字符的空格填充
    
#####################核心程序代码：
    for i in range(num):
        u = Ulist[i]#Ulist[1]就是一整个列表     u0,u1..u4就是一个列表里的元素
        print(space.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))
#[['1', '北京大学', '100', '综合类', '北京'],    ['2', '清华大学', '99.58', '理工类', '北京']]
#   u0     u1        u2      u3         u4  下一个 u0      u1         u2       u3       u4


def main():
    #url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    url = "http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type="
    num = 20
    Univerlist = []
    demo = getHTML(url)
    soupBeautiful(Univerlist,demo)
    printResult(Univerlist,num)

main()
    
