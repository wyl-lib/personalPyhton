import requests
import re
 
def getHTMLText(url,proxies,kv):
    try:
        r = requests.get(url,proxies=proxies,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))
        
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    kv = {
            'cookie':'miid=8918929161557251612; thw=cn; cna=T4HZEzynCXUCAXuBddmobk0l; t=811619c43d95761850375b4c3a5ab2ac; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=wcf159375; lgc=wcf159375; tg=0; enc=eppzwOIC%2BLAV0EEl3Of8yFgJ7GaVyefjEw6qYxfP2SCP0XOeIIzZCRvQ40ZU99qPCpirGJPPmmeYnMreaanmLA%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; cookie2=11a6657be620862d92b819f8ec7bc6dd; _tb_token_=31307d31eb8e8; unb=2443825648; sg=586; _l_g_=Ug%3D%3D; skt=4526025652a3a548; cookie1=UU6kWzgH7y3jofHY3%2Fyl0rf3%2FruA8KtZnTld0Dw%2FSTg%3D; csg=c84b8036; uc3=vt3=F8dByRjJMgFBFtr9oD4%3D&id2=UUwU2jW5acw49w%3D%3D&nk2=FPqJbRi2lM3n&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU0MDYyNDQzNA%3D%3D; _cc_=URm48syIZQ%3D%3D; dnk=wcf159375; _nk_=wcf159375; cookie17=UUwU2jW5acw49w%3D%3D; mt=ci=54_1; uc1=cookie14=UoTYNkHSgWlZVA%3D%3D&lng=zh_CN&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=URm48syIYB3rzvI4Dim4&tag=8&cookie15=W5iHLLyFOGW7aA%3D%3D&pas=0; isg=BPb2H07tsZWsn0X3BBUenxI_Ryw4v4ZAwyBjAWDf41l0o5Y9yKSTYV5Vvz9qDTJp',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    proxies={'https':'https://128.227.76.129'}
    infoList = []

    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url,proxies,kv)
    
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()
