# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:26:21 2019

@author: Angel
"""

# write a number smaller than 8192
n = 1234
# print (n," is")
a = str(n)+" is"
# count down from 13
i = 13
while n != 0:
# find out the biggesr power of 2 within n
    if i >= 0:
        if n < 2 ** i:
            i = i - 1
        else:
            n = n - 2 ** i
            a = a + " 2**"+ str(i)
            if n!= 0:
                a = a + " +"
           # print("+2**",i)
            i = i - 1            
 # if the combination equals n then stop and print
print(a)