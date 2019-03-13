# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:17:25 2019

@author: Angel
"""

a = 245
b = 245245
c = b / 7
d = c / 11
e = d / 13
if a > e:
    print("a is greater than b")
elif e > a:
    print("b is greater than a")
else:
    print("a is equal to b")

X = True
Y = True
Z = (X and not Y) or (Y and not X)
W = X != Y