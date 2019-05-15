# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:49:37 2019

@author: Angel
"""
"""
#this dictionary is typed manually and has some mistakes 

BLOSUM={
'A':{'A':4,'R':-1,'N':-2,'D':-2,'C':0,'Q':-1,'E':-1,'G':0,'H':-2,'I':-1,'L':-1,'K':-1,'M':-1,'F':-2,'P':-1,'S':1,'T':0,'W':-3,'Y':-2,'V':0,'B':-2,'Z':-1,'X':0},
'R':{'A':-1,'R':5,'N':0,'D':-2,'C':-3,'Q':1,'E':0,'G':-2,'H':0,'I':-3,'L':-2,'K':2,'M':-1,'F':-3,'P':-2,'S':-1,'T':-1,'W':-3,'Y':-2,'V':-3,'B':-1,'Z':0,'X':-1},
'N':{'A':-2,'R':0,'N':6,'D':1,'C':-3,'Q':0,'E':0,'G':0,'H':1,'I':-3,'L':-3,'K':0,'M':-2,'F':-3,'P':-2,'S':1,'T':0,'W':-4,'Y':-2,'V':-3,'B':3,'Z':0,'X':-1},
'D':{'A':-2,'R':-2,'N':1,'D':6,'C':-3,'Q':0,'E':2,'G':-1,'H':-1,'I':-3,'L':-4,'K':-1,'M':-3,'F':-3,'P':-1,'S':0,'T':-1,'W':-4,'Y':-3,'V':-3,'B':4,'Z':1,'X':-1},
'C':{'A':0,'R':-3,'N':-3,'D':-3,'C':9,'Q':-3,'E':-4,'G':-3,'H':-3,'I':-1,'L':-1,'K':-3,'M':-1,'F':-2,'P':-3,'S':-1,'T':-1,'W':-2,'Y':-2,'V':-1,'B':-3,'Z':-3,'X':-2},
'Q':{'A':-1,'R':1,'N':0,'D':0,'C':-3,'Q':5,'E':2,'G':-2,'H':0,'I':-3,'L':-2,'K':1,'M':0,'F':-3,'P':-1,'S':0,'T':-1,'W':-2,'Y':-1,'V':-2,'B':0,'Z':3,'X':-1},
'E':{'A':-1,'R':0,'N':0,'D':2,'C':-4,'Q':2,'E':5,'G':-2,'H':0,'I':-3,'L':-3,'K':1,'M':-2,'F':-3,'P':-1,'S':0,'T':-1,'W':-3,'Y':-2,'V':-2,'B':1,'Z':4,'X':-1},
'G':{'A':0,'R':-2,'N':0,'D':-1,'C':-3,'Q':-2,'E':-2,'G':6,'H':-2,'I':-4,'L':-4,'K':-2,'M':-3,'F':-3,'P':-2,'S':0,'T':-2,'W':-2,'Y':-3,'V':-3,'B':-1,'Z':-2,'X':-1},
'H':{'A':-2,'R':0,'N':1,'D':-1,'C':-3,'Q':0,'E':0,'G':-2,'H':8,'I':-3,'L':-3,'K':-1,'M':-2,'F':-1,'P':-2,'S':-1,'T':-2,'W':-2,'Y':2,'V':-3,'B':0,'Z':0,'X':-1},
'I':{'A':-1,'R':-3,'N':-3,'D':-3,'C':-1,'Q':-3,'E':-3,'G':-4,'H':-3,'I':4,'L':2,'K':-3,'M':1,'F':0,'P':-3,'S':-2,'T':-1,'W':-3,'Y':-1,'V':3,'B':-3,'Z':-3,'X':-1},
'L':{'A':-1,'R':-2,'N':-3,'D':-4,'C':-1,'Q':-2,'E':-3,'G':-4,'H':-3,'I':2,'L':4,'K':-2,'M':2,'F':0,'P':-3,'S':-2,'T':-1,'W':-2,'Y':-1,'V':1,'B':-4,'Z':-3,'X':-1},
'K':{'A':-1,'R':2,'N':0,'D':-1,'C':-3,'Q':1,'E':1,'G':-2,'H':-1,'I':-3,'L':-2,'K':5,'M':-1,'F':-3,'P':-1,'S':0,'T':-1,'W':-3,'Y':-2,'V':-2,'B':0,'Z':1,'X':-1},
'M':{'A':-1,'R':-1,'N':-2,'D':-3,'C':-1,'Q':0,'E':-2,'G':-3,'H':-2,'I':1,'L':2,'K':-1,'M':5,'F':0,'P':-2,'S':-1,'T':-1,'W':-1,'Y':-1,'V':1,'B':-3,'Z':-1,'X':-1},
'F':{'A':-2,'R':-3,'N':-3,'D':-3,'C':-2,'Q':-3,'E':-3,'G':-3,'H':-1,'I':0,'L':0,'K':-3,'M':0,'F':6,'P':-4,'S':-2,'T':-2,'W':1,'Y':3,'V':-1,'B':-3,'Z':-3,'X':-1},
'P':{'A':-1,'R':-2,'N':-2,'D':-1,'C':-3,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-3,'L':-3,'K':-1,'M':-2,'F':-4,'P':7,'S':-1,'T':-1,'W':-4,'Y':-3,'V':-2,'B':-2,'Z':-1,'X':-2},
'S':{'A':1,'R':-1,'N':1,'D':0,'C':-1,'Q':0,'E':0,'G':0,'H':-1,'I':-2,'L':-2,'K':0,'M':-1,'F':-2,'P':-1,'S':4,'T':1,'W':-3,'Y':-2,'V':-2,'B':0,'Z':0,'X':0},
'T':{'A':0,'R':-1,'N':0,'D':-1,'C':-1,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-1,'L':-1,'K':-1,'M':-1,'F':-2,'P':-1,'S':1,'T':5,'W':-2,'Y':-2,'V':0,'B':-1,'Z':-1,'X':0},
'W':{'A':-3,'R':-3,'N':-4,'D':-4,'C':-2,'Q':-2,'E':-3,'G':-2,'H':-2,'I':-3,'L':-2,'K':-3,'M':-1,'F':1,'P':-4,'S':-3,'T':-2,'W':11,'Y':-2,'V':-3,'B':-4,'Z':-3,'X':-2},
'Y':{'A':-2,'R':-2,'N':-2,'D':-3,'C':-2,'Q':-1,'E':-2,'G':-3,'H':2,'I':-1,'L':-1,'K':-2,'M':-1,'F':3,'P':-3,'S':-2,'T':-2,'W':2,'Y':7,'V':-1,'B':-3,'Z':-2,'X':-1},
'V':{'A':0,'R':-3,'N':-3,'D':-3,'C':-1,'Q':-2,'E':-2,'G':-3,'H':-3,'I':3,'L':1,'K':-2,'M':1,'F':-1,'P':-2,'S':-2,'T':0,'W':-3,'Y':-1,'V':4,'B':-3,'Z':-2,'X':-1},
'B':{'A':-2,'R':-1,'N':3,'D':4,'C':-3,'Q':0,'E':1,'G':-1,'H':0,'I':-3,'L':-4,'K':0,'M':-3,'F':-3,'P':-2,'S':0,'T':-1,'W':-4,'Y':-3,'V':-3,'B':4,'Z':1,'X':-1},
'Z':{'A':-1,'R':0,'N':0,'D':1,'C':-3,'Q':3,'E':4,'G':-2,'H':0,'I':-3,'L':-3,'K':1,'M':-1,'F':-3,'P':-1,'S':0,'T':-1,'W':-3,'Y':-2,'V':-2,'B':1,'Z':4,'X':-1},
'X':{'A':0,'R':-1,'N':-1,'D':-1,'C':-2,'Q':-1,'E':-1,'G':-1,'H':-1,'I':-1,'L':-1,'K':-1,'M':-1,'F':-1,'P':-2,'S':0,'T':0,'W':-2,'Y':-1,'V':-1,'B':-1,'Z':-1,'X':-1},
}
"""
#read blosum
import pandas as pd
blosum=input('please input the filepath of the blosum you want to use (txt):')
data=pd.read_csv(blosum,sep=r' +',engine='python')
BLOSUM=data.to_dict()

#input sequence from file
import re
file1=input('please put the file pathway of your first sequence here')
file2=input('please put the file pathway of your second sequence here')
try:
    open(file1,'r')
except:
    print('the file pathway of your first sequence is wrong')
try:
    open(file2,'r')
except:
    print('the file pathway of your second sequence is wrong')
    
fhand1=open(file1)
fhand2=open(file2)

read1=fhand1.read()
read2=fhand2.read()

list1=re.findall(r'[A-Z]+[A-Z]+[A-Z]+[A-Z]+',read1)
list2=re.findall(r'[A-Z]+[A-Z]+[A-Z]+[A-Z]+',read2)

seq1=list1[0]
seq2=list2[0]

#calculate score
score=0
for i in range(len(seq1)):
    score=score+BLOSUM[seq1[i]][seq2[i]]

#count
count1=len(seq1)
count2=len(seq2)
if count1!=count2:
    print('the length of the two sequences are different')
if count1==count2:
    count=count1

#calculate percentage
same=0
for i in range (count):
    if seq1[i]==seq2[i]:
        same=same+1
percentage=(same/count)*100

#alignment
align=''
for i in range(count):
    if seq1[i]==seq2[i]:
        align=align+seq1[i]
    else:
        if BLOSUM[seq1[i]][seq2[i]]>0:
            align=align+'+'
        else:
            align=align+'-'

print('*************result***************')
print('score:',score)
print('total animo acid',count)
print('normalised score',score/count)
print('percentage identity',"%.2f" % round(percentage,2),'%','\n')
print('sequence1',seq1,'\n')
print('alignment:','\n',align,'\n')  #graphical alignment
print('sequence2:',seq2,'\n')
