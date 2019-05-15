# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:09:48 2019

@author: Angel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def count(array):
    '''
    count people who become sick or recover
    '''
    import collections
    a=collections.Counter(array)
    return a[0]

for n in range(10):
#define variables
    N=10000     #total number
    V=int(0.1*n*N)     #vaccination
    S=int(9999-V)     #susceptible
    I=1        #infected
    R=0        #recovered
    
    beta=0.3   #contact
    gamma=0.05 #recovery probability
    
    array_S=[S]
    array_I=[I]
    array_R=[R]
    
    #a loop for 1000 times
    for i in range(1000):
      
    #calculate the newly infected number and add to I and minus it from S, possibility=beta*(I/N)
        temp=np.random.choice(range(2),S,p=[beta*(I/N),1-beta*(I/N)])
        newlyI=count(temp)
        I=I+newlyI
        S=S-newlyI
        
    #calculate the recovered number, minus it from I, add it to R
        temp=np.random.choice(range(2),I,p=[gamma,1-gamma])
        newlyR=count(temp)
        I=I-newlyR
        R=R+newlyR    
        
    #record S,I,R
        array_S.append(S)
        array_I.append(I)
        array_R.append(R)
    
    #plot
    plt.plot(array_I,label=("{:.1%}".format(n*0.1)),color=cm.viridis(n*30))
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rate')
plt.legend()

