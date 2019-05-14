# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:55:04 2019

@author: Angel
"""

#input
i=1
while i:
    i=0
    data=input("Please input positive intergers to compute 24:(use ',' to divide them)\n")
    numlist=data.split(',')
    for char in numlist:
        if int(char)<=23: 
            continue
        else:
            print('The intergers should be smaller than 24')
            i=1
            break

num=list(map(int,numlist))

count=0

def count_cal(n):
    global count
    count=count+1
    #when complete
    if n==1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #calculate
    for i in range(0,n):
        for j in range(i+1,n):
            a=num[i]
            b=num[j]
            num[j]=num[n-1]
            
            num[i]=a+b
            if(count_cal(n-1)):
                return 1
            
            num[i]=a-b
            if(count_cal(n-1)):
                return 1
            
            num[i]=a*b
            if(count_cal(n-1)):
                return 1
            
            if a:
                num[i]=b/a
                if(count_cal(n-1)):
                    return 1
            if b:
                num[i]=a/b
                if(count_cal(n-1)):
                    return 1
            num[i]=a
            num[j]=b
    return 0

if (count_cal(len(num))):
    print('solution exists!')
else:
    print('no solution')
print('Recursion times:',count)