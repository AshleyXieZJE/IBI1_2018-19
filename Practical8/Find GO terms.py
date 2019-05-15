# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:44:44 2019

@author: Angel
"""

#from xml.dom.minidom import parse
import xml.dom.minidom

#find childnodes
def Child(id,resultlist):
    for t in terms:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultlist.append(geneid)
                Child(geneid,resultlist)
              
result=[]
#main script
filepath=('please input your filepath of go_obo.xml:')
dom=xml.dom.minidom.parse(filepath)
obo=dom.documentElement
terms=obo.getElementsByTagName('term')
for term in terms:
    defstr=term.getElementsByTagName('defstr')[0]
    
    #find autophagosome
    if 'autophagosome' in defstr.childNodes[0].data:
        GO=[]#a line in excel
        id=term.getElementsByTagName('id')[0].childNodes[0].data
        GO.append(id)
        name=term.getElementsByTagName('name')[0]
        GO.append(name.childNodes[0].data)
        GO.append(defstr.childNodes[0].data)
        resultlist=[]
        Child(id,resultlist)
        GO.append(len(resultlist))
        result.append(GO)
print(result)
        
#excel
import pandas as pd
pd.DataFrame(result).to_excel('autophagosome.xlsx', header=['id','name','defstr','childnodes'], index=False)

