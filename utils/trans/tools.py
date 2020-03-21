#coding=utf-8
from datetime import datetime
import random
def get_trans_id(date=None):
    """
    根据当前的时间返回一个唯一的流水    
    """
    #如果当前的时间为空，获取当前的时间
    if date ==None:
        date=datetime.now()
    #将当前的时间转换成字符串+六位随机数
    return date.strftime('%Y%m%d%H%M%S%f')+str(random.randint(100000,999999))

    
