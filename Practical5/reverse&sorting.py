# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:30:09 2019

@author: Angel
"""


A=input("give me a string of words\n")
A=A[::-1]
B=A.split(" ")
print(B)
C=sorted(B,reverse=True)
print(C)