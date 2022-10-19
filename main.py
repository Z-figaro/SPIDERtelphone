# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests
import time
import json


def get_links():
    url_header = 'http://www.ccgp-sichuan.gov.cn/'



def getHTMLText(url,params,type):
    '''
    封装网页返回信息方式
    :param url: 基础网址
    :param params: 四川政府采购网需要的参数
    :return: 返回一个json格式，和中间的html需要的网页内容
    '''
    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'www.ccgp-sichuan.gov.cn',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=0B5A5B9105D3AF64747B557A7CAFF1A1'
    }
    try:
        r = requests.get(url,params,timeout=30,headers=headers, data=payload)
        r.raise_for_status()  #如果状态不是200，引发HTTPError异常
        # r.encoding = r.apparent_encoding  #因为apparent更准确
        return r.text

    except:
        return "产生异常"


# 获取网页
def connect():
    # 四川政府采购网
    url = 'http://www.ccgp-sichuan.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do'
    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'www.ccgp-sichuan.gov.cn',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=0B5A5B9105D3AF64747B557A7CAFF1A1'
    }
    params = {
        'siteId': '94c965cc-c55d-4f92-8469-d5875c68bd04',
        'channel': 'c5bff13f-21ca-4dac-b158-cb40accd3035',
        'currPage': '1',
        'pageSize': '10',
        'noticeType': '00102',
        'selectTimeName': 'noticeTime',
    }
    # text 类型的返回值
    content = getHTMLText(url=url,params=params,type='text')
    # json的返回值
    jsonContent = json.loads(content)
    print(jsonContent['data'][0]['content'])
    # for data in jsonContent['data']:
    #     print(data['content'])

# 获取所有项目的结果网址和其他基本信息

def get_links():
    # 四川政府采购网
    url = 'http://www.ccgp-sichuan.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do'
    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'www.ccgp-sichuan.gov.cn',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=0B5A5B9105D3AF64747B557A7CAFF1A1'
    }
    params = {
        'siteId': '94c965cc-c55d-4f92-8469-d5875c68bd04',
        'channel': 'c5bff13f-21ca-4dac-b158-cb40accd3035',
        'currPage': '1',
        'pageSize': '10',
        'noticeType': '00102',
        'selectTimeName': 'noticeTime',
    }



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
