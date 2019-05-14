# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:53:03 2019

@author: Angel
"""

import numpy as np
import matplotlib.pyplot as plt

#variables
beta=0.3
gamma=0.05

# make array of all susceptible population
population=np.zeros((100,100))

#outbreak
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

#plot
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

#loop
for n in range(100):
    #find an infected point
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        #find neighbouring dots
        for xNeighbour in range (x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                
                # make sure I don't fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                #if they are susceptible, they may be infected
                    if population[xNeighbour,yNeighbour]==0:
                        temp=np.random.choice(range(2),1,p=[beta,1-beta])
                        if temp[0]==0:
                            population[xNeighbour,yNeighbour]=1
                        
        #look for infected dots, they may recover
        temp=np.random.choice(range(2),1,p=[gamma,1-gamma])
        if temp[0]==0:
            population[x,y]=2
    
    #plot in day0,10,50,99
    if n==10 or 50 or 99:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    