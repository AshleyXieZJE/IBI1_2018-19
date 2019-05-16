# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:08:14 2019

@author: Angel
"""

#*********************question 1 & 2***************************
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("E:\IBI\Git\IBI1_2018-19\Practical13\CopasiSE -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
    
xml_to_cps()   
     
#change working directory
import os
os.chdir('E:\IBI\Git\IBI1_2018-19\Practical13')
os.system("E:\IBI\Git\IBI1_2018-19\Practical13\CopasiSE predator-prey.cps")

#read file and put the data into array
import csv
results = []
with open("modelResults.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

#get numbers
import numpy
results=numpy.array(results)
results_number=results[1:,1:3]
results_number=results_number.astype(numpy.float)

#plot predator-prey course
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(results_number[0:,0],label="prey(b=0.02,d=0.4)")
plt.plot(results_number[0:,1],label="predator(b=0.1,d=0.02)")
plt.xlabel('time')
plt.ylabel('population size')
plt.title('time course')
plt.legend()

#A limit cycle plot
plt.figure(2)
plt.plot(results_number[0:,0],results_number[0:,1])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('A limit cycle plot')










#*********************question 3***************************
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey-copy.xml -s predator-prey-copy.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey-copy.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey-copy.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
#Changing values and running the simulation again
import xml.dom.minidom
import os
os.chdir('E:\IBI\Git\IBI1_2018-19\Practical13')
#open file
dom=xml.dom.minidom.parse("predator-prey-copy.xml")   #document
sbml=dom.documentElement          #the only root element

#get value
parameters=sbml.getElementsByTagName('parameter')
for parameter in parameters:
    v=parameter.getAttribute('value')        
    #change these parameters
    if parameter.getAttribute('id')=='k_predator_breeds':
        parameter.setAttribute('value','0.05')
        print('k_predator_breeds')
        print(parameter.attributes['value'].value)
    if parameter.getAttribute('id')=='k_predator_dies':
        parameter.setAttribute('value','0.6')
        print('k_predator_dies')
        print(parameter.attributes['value'].value)
    if parameter.getAttribute('id')=='k_prey_breeds':
        parameter.setAttribute('value','0.4')
        print('k_prey_breeds')
        print(parameter.attributes['value'].value)
    if parameter.getAttribute('id')=='k_prey_dies':
        parameter.setAttribute('value','0.08')
        print('k_prey_dies')
        print(parameter.attributes['value'].value)

#change xml file and convert the new xml file into cps files using xml_to_cps function
copy = open('predator-prey-copy.xml','w')
dom.writexml(copy)
copy.close()
xml_to_cps()

#use the new cps file to create new modelresults
os.system("CopasiSE.exe predator-prey-copy.cps")
#use the new results to plot
import csv
results = []
with open("modelResults.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

#get numbers
import numpy
results=numpy.array(results)
results_number=results[1:,1:3]
results_number=results_number.astype(numpy.float)

#plot predator-prey course
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(results_number[0:,0],label="prey")
plt.plot(results_number[0:,1],label="predator")
plt.xlabel('time')
plt.ylabel('population size')
plt.title('time course')
plt.legend()












#*********************question 4***************************
#Running many simulations
    
#aim: find out how the death rate of predator affects the population of predator and prey
import xml.dom.minidom
import csv
import numpy
import matplotlib.pyplot as plt
import os
os.chdir('E:\IBI\Git\IBI1_2018-19\Practical13')
#loop 100 or more times
for i in range (5):
    #use the coding for question 3 to find 4 parameters, but only change k_predator_dies into random numbers using numpy.random.sample()
    def xml_to_cps():
        import os
        import xml.dom.minidom
        
        # first, convert xml to cps 
        os.system("CopasiSE.exe -i predator-prey-copy.xml -s predator-prey-copy.cps")
        
        # now comes the painful part. Just copy and paste this ok
        
        cpsTree = xml.dom.minidom.parse("predator-prey-copy.cps")
        cpsCollection = cpsTree.documentElement
        
        reportFile = xml.dom.minidom.parse("report_ref.xml")
        reportLine = reportFile.documentElement
        
        tasks = cpsCollection.getElementsByTagName("Task")
        for task in tasks:
            if task.getAttribute("name")=="Time-Course":
                task.setAttribute("scheduled","true")
                task.insertBefore(reportLine,task.childNodes[0])
                break
            
        
        for taskDetails in task.childNodes:
            if taskDetails.nodeType ==1:
                if taskDetails.nodeName == "Problem":
                    problem = taskDetails
                    
        for param in problem.childNodes:
            if param.nodeType ==1:
                if param.getAttribute("name")=="StepNumber":
                    param.setAttribute("value","200")
                if param.getAttribute("name")=="StepSize":
                    param.setAttribute("value","1")
                if param.getAttribute("name")=="Duration":
                    param.setAttribute("value","200")
               
                
        report18 = xml.dom.minidom.parse("report18.xml")
        report = report18.documentElement
        
        listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
        listOfReports.appendChild(report)
        
        cpsFile = open("predator-prey-copy.cps","w",encoding='utf-8')
        cpsTree.writexml(cpsFile)
        cpsFile.close()
#Changing values and running the simulation again
    
    #open file
    dom=xml.dom.minidom.parse("predator-prey-copy.xml")   #document
    sbml=dom.documentElement          #the only root element
    
    #get value
    parameters=sbml.getElementsByTagName('parameter')
    for parameter in parameters:
        v=parameter.getAttribute('value')        
        #change these parameters
        if parameter.getAttribute('id')=='k_predator_breeds':
            v=numpy.random.sample()
            parameter.setAttribute('value',str(v))
            print('k_predator_breeds')
            print(parameter.attributes['value'].value)
        if parameter.getAttribute('id')=='k_predator_dies':
            v=numpy.random.sample()
            parameter.setAttribute('value',str(v))
            print('k_predator_dies')
            print(parameter.attributes['value'].value)
        if parameter.getAttribute('id')=='k_prey_breeds':
            v=numpy.random.sample()
            parameter.setAttribute('value',str(v))
            print('k_prey_breeds')
            print(parameter.attributes['value'].value)
        if parameter.getAttribute('id')=='k_prey_dies':
            v=numpy.random.sample()
            parameter.setAttribute('value',str(v))
            print('k_prey_dies')
            print(parameter.attributes['value'].value)
    
    #change xml file and convert the new xml file into cps files using xml_to_cps function
    copy = open('predator-prey-copy.xml','w')
    dom.writexml(copy)
    copy.close()
    xml_to_cps()
    
    #use the new cps file to create new modelresults
    os.system("CopasiSE.exe predator-prey-copy.cps")
    #use the new results to plot
    
    results = []
    with open("modelResults.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results.append(row)
    
    #get numbers
    results=numpy.array(results)
    results_number=results[1:,1:3]
    results_number=results_number.astype(numpy.float)
    
    #plot predator-prey course
    plt.figure(i)
    plt.plot(results_number[0:,0],label="prey")
    plt.plot(results_number[0:,1],label="predator")
    plt.xlabel('time')
    plt.ylabel('population size')
    plt.title('time course')
    plt.legend()


#above is the code that can run a number of simulations and produce graphes
#the folowing part is some ideas(pseudocode) on how to expend the code

#find the maximun of predator and prey population from the result csv file and append them to a result list together with k_predator_dies
#plot k_predator_dies against maximum predator and prey population
#this model can explore the importance of predators in the environment