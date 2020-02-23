import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        print("获取url地址:")
        r = requests.get(url)
        print("get了，继续\n")

        print("raise_stsus = ",r.raise_for_status())
        print("获取状态完毕")
        r.encoding = r.apparent_encoding
        print("转换格式utf-8完毕")
        return r.text
    except:
        return "获取中遇到问题"
    

def fileUniverList(ulist,demo):
    soup = BeautifulSoup(demo,"html.parser")#煲汤

    for tr in soup.find("tbody").children:#遍历所有tbody的子孙标签

        if isinstance(tr,bs4.element.Tag): #判断tr标签下的内容是否为标签类型

            tds = tr("td")#将tr中的td标签转换成列表类型tds
            #相当于tds = tr.find_all('td')是一个列表类型存放了所有的td标签
            ulist.append([tds[0].text,tds[1].text,tds[2].text,tds[3].text])
            #print("ulist[0] is {}".format(ulist[0]))
            
        '''
            print("\n\ntype(tds) is {}\n\n".format(type(tds)))#bs4.element.ResultSet'
            print("\n\ntype(tr) is {}\n\n".format(type(tr)))#bs4.element.Tag'
            print("\n\ntype(td) is {}\n\n".format(type('td')))#str'
        '''
        ''' 
            print("\n\ntype(tds[0] is {}\n\n".format(type(tds[0])))#bs4.element.Tag
            print("\n\ntype(tds[0].text is {}\n\n".format(type(tds[0].text)))#str
            print("\n\ntype(tds[0].string) is {}\n\n".format(type(tds[0].string)))#bs4.element.NavigableString'>
        '''
          #  print("tds[0].string.........")

def printUniverList(ulist,num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"#问题所在
    print("进入printfUniverList函数\n")
    print(tplt.format("排名","学校名称","省市","总分",chr(12288)))#问题所在tplt的{4}
    #print("输出标头的四个属性值")
    for i in range(num):
        #print("进入range循环")
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    #url = 'http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type='
    uinfo = []
    demo = getHTMLText(url)
    #print(demo)
    fileUniverList(uinfo,demo)
    printUniverList(uinfo,20)
    
main()
