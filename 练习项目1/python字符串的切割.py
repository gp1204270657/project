#-*-coding =utf-8 -*-

import re
def go_split(s,symobl):
    #
    #一次性分割字符串
    result=re.split(symobl,s)
    #去除空字符
    return [x for x in result if x]



if __name__ == '__main__':
    #字符串
    s= '12;;7.osjd;.jshdjdknx+'
    #正则表达式 []表示对立面的处理
    symobl='[;.+]'
    result=go_split(s,symobl)
    print(result)