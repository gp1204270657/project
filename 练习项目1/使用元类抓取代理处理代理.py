#coding=utf-8
from .getpage import get_page
from pyquery import PyQuery as pq

#道生一
class ProxyMetaclass(type):
    """
        元类，在FreeProxyMetaclass类中加入
        _CrawlFunc_和_CrawlFuncCount_
        二个参数，分别表示爬虫的函数跟函数的数量
    """
    def __new__(cls, name, bases,attrs):
        count=0
        attrs['_CrawlFunc_']=[]
        attrs['_CrawlFuncCount_']=[]
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['_CrawlName_'].append(k)
                attrs['_CrawlFunc_'].append(v)
                count+=1
        for k in attrs['_CrawlName_']:
            attrs.pop(k)
        attrs['_CrawlFuncCount_']=count
        return type.__new__(cls, name, bases,attrs)

#一生二，创建代理获取类
class ProxyGetter(object,metaclass=ProxyMetaclass):
    def get_raw_proxies(self,site):
        proxies=[]
        print('Site',site)
        for func in self._CrwaFunc_:
            this_page_proxies=func(self)
            for proxy in this_page_proxies:
                print('Getting',proxy,'from',site)
                proxies.append(proxy)
        return proxies

    def carw_daili66(self,page_count=4):
        start_url= 'http://www.66ip.cn/{}.html'
        urls=[start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            html=get_page(url)
            if html:
                doc=pq(html)
                trs=doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip,port])