#获取经纬度信息
import requests

key = 'f1324502c2ebcdd2a332a9e71b5a17a6'
#parameter = {'address':geo,'key':key}def Address(address):
def Address(adress):
    url = 'https://restapi.amap.com/v3/geocode/geo?address=%s&address=%s'%(key,address)
    data = requests.get(url)
    contest = data.json()
    contest = contest['gecodes'][0]['location']
    return contest

if __name__ == 'main':
    print(Address("济南大学泉城学院"))