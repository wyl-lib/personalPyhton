import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)
        print("raise_stsus = {}".format(r.raise_for_status()))
        print("获取状态完毕")
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("get information with error!")

def movieSoupList(movielist,demo):
    try:
        soup = BeautifulSoup(demo,"html.parser")
        tables = soup.find_all("table")
        #print("tables is {}\n\n".format(tables))
        tab = tables[1]
        #if isinstance(tab,bs4.element.Tag):
        #    print("yaoxi!!!!!!!!")
        #print("tab is {}\n\n".format(tab))    #tags = tab.find("tr")
        #print(type(tags))    #print("tags = {}\n".format(tags))
        tags = tab.contents    #print("tages {} ".format(tab.contents))

    #    *****  .contents  方法   *****

        #print(type(tab.contents)) #//<class'list'>    #i = 0
        for tr in tags:
            #i = i+1     #print("i = {}\n".format(i))
            #print("transfor finished")
            if isinstance(tr,bs4.element.Tag):
                tds = tr("td")

    #   *****   tr("td")这步也很关键    *****
                
                #print("tds {}".format(tds))#print("list is ok")
                movielist.append([tds[0].string,tds[1].string])
                #print("transfor finished")
                #print("movielist is {}".format(movielist))
    except:
        print("transfor error")

def printMovieList(movielist,num):
    model = "{0:^10}\t{1:^20}"
    print(model.format("排名","影片名",chr(12288)))
    try:
        for i in range(num):
            m = movielist[i]
            print(model.format(m[0],m[1],chr(12288)))
    except:
        print("printMovieList error\n")

def main():
    num = 10
    url = 'https://movie.douban.com/'
    movielist = []
    demo = getHtmlText(url)
    movieSoupList(movielist,demo)
    #print("movielist is \n{}\n\n".format(movielist))
    printMovieList(movielist,num)

main()