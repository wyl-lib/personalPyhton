import bs4
import smtplib
import requests
import csv							#将数据写入到csv文件中
import random				  #取随机数 
import time
import socket			#socket和http.client在这里只用于异常处理 
import http.client
# import urllib.requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

def get_content(url , data = None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'utf-8'
            # req = urllib.request.Request(url, data, header)
            # response = urllib.request.urlopen(req, timeout=timeout)
            # html1 = response.read().decode('UTF-8', errors='ignore')
            # response.close()
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))

        except socket.timeout as e:
            print( '3:', e)#sleep(second)推迟执行的秒数可以使用time.ctime()方法测试当前时间,
            #choice() 方法返回一个列表，元组或字符串的随机项。
            #choice()是不能直接访问的，需要导入  random 模块，然后通过 random 静态对象调用该方法
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print( '4:', e)
            time.sleep(random.choice(range(20, 60)))
            

        except http.client.BadStatusLine as e:
            print( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print( '6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text
    # return html_text

def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    data = body.find('div', {'id': '7d'})  # 找到id为7d的div
    ul = data.find('ul')  # 获取ul部分
    li = ul.find_all('li')  # 获取所有的li

    for day in li: # 对每个li标签中的内容进行遍历
        temp = []
        date = day.find('h1').string  # 找到日期
        temp.append(date)  # 添加到temp中
        inf = day.find_all('p')  # 找到li中的所有p标签
        temp.append(inf[0].string,)  # 第一个p标签中的内容（天气状况）加到temp中
        if inf[1].find('span') is None:
            temperature_highest = None # 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加个判断语句,来输出最低气温
        else:
            temperature_highest = inf[1].find('span').string  # 找到最高温
            temperature_highest = temperature_highest.replace('℃', '')  # 到了晚上网站会变，最高温度后面也有个℃
        temperature_lowest = inf[1].find('i').string  # 找到最低温
        temperature_lowest = temperature_lowest.replace('℃', '')  # 最低温度后面有个℃，去掉这个符号
        temp.append(temperature_highest)   # 将最高温添加到temp中
        temp.append(temperature_lowest)   #将最低温添加到temp中
        final.append(temp)   #将temp加到final中

    return final

def printCode(result,weather_list):
    demo = '{0:{4}^10}\t{1:{4}^6}\t{2:{4}^6}\t{3:{4}^4}'
    print(demo.format("实时日期","天气类型","最高温度~","最低温度",chr(12288)))
    try:
        if result[2] is not None:
            for i in range(7):
                weather_list = result[i]
                w = weather_list
                print(demo.format(w[0],w[1],w[2],w[3],chr(12288)))
    except:
        for i in range(1,7):
            weather_list = result[i]
            w = weather_list
            print(demo.format(w[0],w[1],w[2],w[3],chr(12288)))

        print("\nBe careful!!")#So we delete the record that is today's data.
        print("The temprature_highest isn't exsist when night.")

def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)

def send_email(email):
    '''
    sender = input('From: ')
    password = input('password: ')
    smtp_server = input('SMTP_Server: ')
'''
    ##     FROM    ##
    sender = 'wyl1346788525@sohu.com'
    sent_host = 'smtp.sohu.com'
    sent_user = 'wyl1346788525@sohu.com'
    sent_pass = 'cxlgWYL1'

    ##     TO     ##
    receivers = ['wyl1346788525@yach.net','1346788525@qq.com']

    message = MIMEText("您好，蓬莱天气如下: \n{0}\n".format(result),'plain','utf-8')
    
    ##   JUST USE TO DISPLAY   ##
    message['from'] = Header(sender,'utf-8')
    message['to'] = Header(receivers[1],'utf-8')
    message['subject'] = Header("您的天气预报详情!",'utf-8')
    
    server = smtplib.SMTP(sent_host,25)
    #server.set_debuglevel(1)
    server.login(sender,sent_pass)
    server.sendmail(sender,receivers,message.as_string())

    print("邮件发送成功")
    server.quit()

if __name__ == '__main__':
    url ='http://www.weather.com.cn/weather/101120504.shtml'
    weather_list = []
    html = get_content(url)
    result = get_data(html)

    printCode(result,weather_list)
    result = str(result).replace(']','\n')
    send_email(result)
    #write_data(result, '蓬莱天气.csv')

