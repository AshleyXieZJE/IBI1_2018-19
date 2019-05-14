# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:23:26 2019

@author: Angel
"""

import re
from fractions import Fraction
re_numtest=re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-9]$)')
i=1
while i:
    i=0
    data=input("Please input positive intergers to compute 24:(use ',' to divide them)\n")
    numlist=data.split(',')
    for char in numlist:
        if re_numtest.match(char):
            continue
        else:
            print('error')
            i=1
            break

num=list(map(int,numlist))

count=0
solution=0

def dfs(n):
    global count
    global solution
    count=count+1
    
    if n==1:
        if(float(num[0])==24):
            solution=solution+1
            return 1
        else:
            return 0
    
    for i in range(0,n):
        for j in range(i+1,n):
            a=num[i]
            b=num[j]
            num[j]=num[n-1]
            
            num[i]=a+b
            if(dfs(n-1)):
                return 1
            
            num[i]=a-b
            if(dfs(n-1)):
                return 1
            
            num[i]=a*b
            if(dfs(n-1)):
                return 1
            
            if a:
                num[i]=Fraction(b,a)
                if(dfs(n-1)):
                    return 1
            if b:
                num[i]=Fraction(a,b)
                if(dfs(n-1)):
                    return 1
            num[i]=a
            num[j]=b
    return 0

if (dfs(len(num))):
    print('yes')
else:
    print('no')
print('Recursion times:',count,',Solution:',solution)
                
            