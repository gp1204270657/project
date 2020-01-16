#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#通过新的zmail来发送
import zmail
mail_content ={
    'subject': '泄喽喽喽喽喽喽喽!',  # 邮件标题写在这
    'content_text':'来自大佬的一封邮件，看到请扣1!'  # 邮件正文写在这
}

# 使用你的邮件账户名和密码登录服务器
server = zmail.server("13636561554@139.com", "gaopeng0312")
# 发送邮件指令
server.send_mail(["15216703243@139.com"], mail_content)

#发送邮箱，大多数会发送拒收失败可用上面的zmail
# sender='13636561554@139.com'
# #接受邮箱
# receiver='gao.peng@mwee.cn'
# #发送邮件主题
# subject='python emall test!'
# #发送邮箱服务器
# smtpserver='smtp.139.com'
# #发送邮箱账号密码
# username='13636561554'
# password='gaopeng0312'
#
# #中文参数设置utf-8
# msg=MIMEText('你好,这个是一个测试哈哈哈','plain','utf-8')
# msg['Subject']=Header(subject,'utf-8')
#
# smtp=smtplib.SMTP()
# smtp.connect('smtp.139.com')
# smtp.login(username,password)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()