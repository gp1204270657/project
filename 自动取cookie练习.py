# coding = utf-8
from selenium import webdriver
import time
bs=webdriver.Chrome()
bs.maximize_window()
url="http://www.yuexing.com"
bs.get(url)
# 删除之前的所有
bs.delete_all_cookies()
# 通过查尔斯抓包工具获取的登陆后cookie的变化来记录并添加到cookie中
bs.add_cookie({"name":'AHSESS','value':'s6vd0kn79c3msh35b09bh4cqv7'})
bs.add_cookie({"name":'pc_bazaar_shortdomain','value':'sh'})
bs.add_cookie({"name":'user_lat','value':'31.24916171'})
bs.add_cookie({"name":'user_lng','value':'121.48789949'})
bs.add_cookie({"name":'tempcookid','value':'a0e7f1e5d168f5c846e1c9f6f324d969'})
bs.add_cookie({"name":'Hm_lvt_0cab8be8d73e44819d9a5782a1ee9fa8','value':'1520240384'})
bs.add_cookie({"name":'Hm_lpvt_0cab8be8d73e44819d9a5782a1ee9fa8','value':'1520240439'})
bs.add_cookie({"name":'qinqin_open','value':'1'})
bs.add_cookie({"name":'im_open','value':'1'})
bs.add_cookie({"name":'behaviourID','value':'3dce4104c7b7dc921735a064d416ab2c'})
bs.add_cookie({"name":'prams','value':'%5B%5D'})
# 重新获取url
bs.get(url)