# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:49:02 2019

@author: Angel
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pandas as pd
a=str()
colname=['name','EmailAddress','Subjects']
#open information
with open(r'E:\IBI\practical\address_information.csv','r') as o_info:
    r_info=pd.read_csv(r'E:\IBI\practical\address_information.csv',names=colname)
name = r_info.name.tolist()
emailaddress = r_info.EmailAddress.tolist()
subjects = r_info.Subjects.tolist()
print(name[1::])
print(emailaddress[1::])
print(subjects[1::])
#find correct email address
import re
for i in range (1,5):
    if re.match(r'.+@.+com',emailaddress[i]):
        sender = 'Hanqi.18@intl.zju.edu.cn'
        receivers = [emailaddress[i]]  
        #open body
        with open(r'E:\IBI\practical\body.txt','r')as o_body:
#change user
            for line in o_body:
                if re.search('User',line):
                    a=a+"Dear "+name[i]+","+"\n"
                else:
                    a=a+str(line)
        message = MIMEText(a, 'plain', 'utf-8')
        subject = subjects[i]
        message['Subject'] = Header(subject, 'utf-8') 
        try:
            server = smtplib.SMTP('smtp.zju.edu.cn',25)
            server.login('Hanqi.18','Fuga@7858')
            server.sendmail(sender, receivers, message.as_string())
            print ("邮件发送成功")
        except server.SMTPException:
                print ("Error: 无法发送邮件")
        a=str()
#send email
#import smtplib
#FROM = 'Hanqi.18@intl.zju.edu.cn'
#TO = ["2518117532@qq.com"]
#SUBJECT = "Hello!"
#TEXT = "This message was sent with Python's smtplib."
#message = """\
    #From: %s
    #To: %s
    #Subject: %s
    #%s
#""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
#server = smtplib.SMTP('smtp.zju.edu.cn',25)
#server.sendmail(FROM, TO, message)
#server.quit()




#import smtplib
#from email.mime.text import MIMEText
#from email.header import Header
 
#sender = '2518117532@qq.com'
#receivers = ['hanqi.18@intl.zju.edu.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
#message['From'] = Header("菜鸟教程", 'utf-8')   # 发送者
#message['To'] =  Header("测试", 'utf-8')        # 接收者
 
#subject = 'Python SMTP 邮件测试'
#message['Subject'] = Header(subject, 'utf-8')
 
 
#try:
    #smtpObj = smtplib.SMTP('localhost')
    #smtpObj.sendmail(sender, receivers, message.as_string())
    #print ("邮件发送成功")
#except smtplib.SMTPException:
    #print ("Error: 无法发送邮件")