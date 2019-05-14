# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:50:22 2019

@author: Angel
"""

import pandas as pd
import re
a=str()

#input
email=input('please use your zju.edu.cn email:')
password=input('password:')
filep_address=input('please input the file pathway of the email address:')
filep_body=input('please input the file pathway of the email body:')
e = re.search(r'(\S+)@(\S+)',email)
colname=['name','EmailAddress','Subjects']

#open information
with open(filep_address,'r') as o_info:
    r_info=pd.read_csv(filep_address,names=colname)
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
        with open(filep_body,'r')as o_body:
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