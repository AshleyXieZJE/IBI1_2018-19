# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:50:22 2019

@author: Angel
"""

import pandas as pd
import re
a=str()
email=input('please use your zju.edu.cn email:')
password=input('password:')
e = re.search(r'(\S+)@(\S+)',email)
colname=['name','EmailAddress','Subjects']
#open information
with open(r'E:\IBI\practical\address_information.csv','r') as o_info:
    r_info=pd.read_csv(r'E:\IBI\practical\address_information.csv',names=colname)
name = r_info.name.tolist()
emailaddress = r_info.EmailAddress.tolist()
subjects = r_info.Subjects.tolist()
#select email address
for i in range (1,5):
    if re.match(r'\S+@\S+com',emailaddress[i]):
        print(emailaddress[i],':Correct Address！')
        #send emails
        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header
 
        sender = email
        receivers = [emailaddress[i]]  
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
            smtpObj = smtplib.SMTP('smtp.zju.edu.cn',25)
            smtpObj.login(e.group(1),password)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("Mail sent successfully!")
            a=str()
            #smtpObj.quit()
        except smtplib.SMTPException:
            print ("Error: Cannot send email!")
            a=str()
    else:
        print(emailaddress[i],':Wrong Address！')