#coding=utf-8
#确保安装requests跟pyquery包
import requests
base_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.3',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

def get_page(url):
    headers=dict(base_headers)
    print("Getting",url)
    try:
        r=requests.get(url,headers=headers)
        print('Getting result',url,r.status_code)
        if r.status_code==200:
            return r.text
    except ConnectionError:
        print('Carwling Failed',url)
        return None
#尝试抓取百度
# if(__name__ == '__main__'):
#     rs=get_page('http://www.baidu.com')
#     print('result \r\n',rs)

#试试抓一下代理
# if (__name__ == '__main__'):
#     from pyquery import PyQuery as pq
#     start_url='http://www.proxy360.cn/Region/China'
#     print('Crawling',start_url)
#     html=get_page(start_url)
#     if html:
#         doc=pq(html)
#         lines=doc('div[name="list_proxy_ip"]').items()
#         for line in lines:
#             ip=line.find('.tbBottomLine:nth-child(1)').text()
#             port=line.find('.tbBottomLine:nth-child(2)').text()
#             print(ip+':'+port)

