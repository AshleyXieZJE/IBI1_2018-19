# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:45:05 2019

@author: Angel
"""

# decide n
n = 56
# loop
while 1 == 1:
    # if n is even, n = n / 2
    if n % 2 == 0:
        n = n / 2
        print(n)
    # end when n = 1
    elif n == 1:
        break
    #if n is odd, n = n * 3 + 1
    else:
        n = n * 3 + 1
        print(n)

