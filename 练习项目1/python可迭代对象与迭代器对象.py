#-*- coding=utf-8 -*-
import requests
import pprint,json
#创建一个迭代器
from collections import Iterable,Iterator
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getWeather(self,city):
        r=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        #通过json来去数据
        # weather=json.loads(r.text)
        #漂亮的打印方式
        # pprint.pprint(weather)
        data=r.json()['data']['forecast'][0]
        return '{0}:{1},{2}'.format(city,data['low'],data['high'])
    def __next__(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index+=1
        return self.getWeather(city)

#生成一个可迭代对象
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities
        #通过调用iter()方法来获得迭代器
    def __iter__(self):
        return WeatherIterator(self.cities)

for w in WeatherIterable(["上海","芜湖","杭州"]):
    print(w)
