import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        print("获取url地址:")
        r = requests.get(url,timeout=30)
        print("get了，继续\n")

        print("raise_stsus = {}".format(r.raise_for_status()))
        print("获取状态完毕")
        r.encoding = r.apparent_encoding
        print("转换格式utf-8完毕")
        return r.text

    except:
        return "获取中遇到问题"
        
def fileUniverList(ulist,demo):
	#使用html解析器整理demo代码，美化优化；
    soup = BeautifulSoup(demo,"html.parser")#煲汤

 	##所有信息都在tbody标签中，再往下所有信息都在tr标签中，再往下所有信息都在td标签中，所以要一层一层寻找
    for tr in soup.find("tbody").children:#遍历tbody所有的子孙标签
        #print(soup.find("tbody"))
    	#如果tr标签的内容里含有不是标签类型的信息可能是字符串类型舍弃使用isinsatance函数处理；
    	#因为我们需要的信息里查看网页源代码都在td标签内；
    	#标签类型表示为bs4.element.Tag;
        #print(tr)
        if isinstance(tr,bs4.element.Tag):
        	#将所有的td标签存为列表类型tds

            tds = tr("td")
            #print("td标签转换完成tds")
            #添加列表内容至ulist中
            #print("type(tds)=\n\\{}\n".format(type(tds)))

            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string,tds[5].string])
          #  print(ulist)
          #  print("tds[0].string.........")

####程序的核心
def printUniverList(ulist,num):
	#创建一个输出摸板｛6｝表示的是使用chr(12288)中文编码排版
    tplt = "{0:^10}\t{1:{6}^10}\t{2:^7}\t{3:^10}\t{4:{6}^10}\t{5:{6}^16}"
    print("进入printfUniverList函数\n")
    #标题栏目
    #chr(12288)中文空格，在中英文混用时出现排版问题，可用此方法解决。
    print(tplt.format("排 名","学校名称","省 市","总 分","新生高考成绩得分","毕业生就业率      ",chr(12288)))

    #循环遍历大学数，已知num = 20；
    #即遍历20所大学
    for i in range(num):
        #将列表内容简化名称递交给列表"u";
        #依次遍历td标签的每个信息然后依次写入列表"u"
        u = ulist[i]
        #使用tplt模版利用format输出，依次输出列表"u"
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],u[5],chr(12288)))

def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    #url = 'http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type='
    uinfo = []  
    demo = getHTMLText(url)
    #print(demo)
    fileUniverList(uinfo,demo)
    #print(uinfo)
    printUniverList(uinfo,20)
    
main()
    