# coding=utf-8
import requests,json
# help(requests)
#post请求
# payload={
#     "name":"zhangsan",
#     "age":23
# }
#data
# test=requests.post("http://httpbin.org/post",data=payload)
# print(test.text)

#调用json
# data_json=json.dumps(payload)
# test=requests.post("http://httpbin.org/post",json=data_json)
# print(test.text)

#登录月星参考代码
host="http://www.yuexing.com"
def login(s,user,psw):
    url=host+"/?mod=user&act=do_login&callback=jQuery3110014379370091921029_1573020680788"
    h={
        # "User - Agent":"Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.70Safari / 537.36",
        # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # "Accept-Language":"zh-CN,zh;q=0.9",
        # "Accept-Encoding":"gzip, deflate",
        # # "Cookie":" tempcookid=94e4f00f024864911e7ff74bf46db837; AHSESS=ij1qhvh40dtp651j2kgmvgu7p2; pc_bazaar_shortdomain=sh; user_lat=31.24916171; user_lng=121.48789949; Hm_lvt_0cab8be8d73e44819d9a5782a1ee9fa8=1572958213; region=sh; behaviourID=bd5cc577d588383cff1328e776c27109; prams=%5B%5D; Hm_lpvt_0cab8be8d73e44819d9a5782a1ee9fa8=1573020681",
        # "Referer":"http://www.yuexing.com/?mod=user&act=login&ret_url=",
        # "Connection":"keep-alive",
        # "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
    body1={
        "user_name":user,
        "password":psw,
        "formhash":"WKlsWSWA",
        "ret_url":"http%3A%2F%2Fwww.yuexing.com%2F"
    }
    r1=s.post(url,data=body1,headers=h)
    print(r1.text)
    return r1.content.decode("utf-8")

def  is_login_sucess(res):
    if "用户名或密码错误" in res:
        return False
    elif "我的订单" in res:
        return True
    else:
        return False
if __name__ == '__main__':
    s=requests.session()
    a=login(s,"13636561554","123123")
    result=is_login_sucess(a)
    print("测试结果：%s" %result)










