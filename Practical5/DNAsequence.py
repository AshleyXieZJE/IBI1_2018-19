# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:03:34 2019

@author: Angel
"""
#get a sequence
B=input("give me a sequence of DNA:\n")
S=list(B)
#count 
a=0
t=0
c=0
g=0
for i in S:
    if i == "A":
        a=a+1
        #a+=1
    elif i == "T":
        t=t+1
    elif i == "C":
        c=c+1
    elif i == "G":
        g=g+1
    else:
        print("The sequence is wrong.")
#print
print("{","'A'",":",a,",","'T'",":",t,",","'C'",":",c,",","'G'",":",g,"}")
#draw pie
import matplotlib.pyplot as plt
labels='A','T','C','G'
size=[a,t,c,g]
plt.pie(size,labels=labels,autopct='%1.1f%%')
plt.axis('equal')
plt.title("Pie of the four DNA nucleotide")