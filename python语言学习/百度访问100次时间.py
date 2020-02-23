import time

import requests

def getHtml(url):
    
    try:
    
        r = requests.get(url)

        r.raise_for_status()

        r.encoding = r.apparent.encoding

        return url.text
    
    except:

        return("The requests get url found unkonw-mistakes.")

def main():

    url = "https://baidu.com"

    time1 = time.time()

    i = 0

    while(i<100):

        start = time.time()

        getHtml(url)

        end = time.time()

        i += 1

        print('第{}次爬取耗时{}s'.format(i+1,end-start))

    time2 = time.time()

    print(time2-time1)

if __name__ =='__main__':

    main()

    

