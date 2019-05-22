# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:02:21 2019

@author: Angel
"""
#-----------------------Importing Excel data in Python-----------------------------
import pandas as pd
df = pd.read_excel('Final_Fluview_Practical_dataset.xlsx')



#------------------------------Data exploration---------------------------------
print(df.describe())
for column in df:
    print(column)
    print('')


#-------------------------------Data preparation-------------------------------
df_regress = df[['Virus Strain','Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]
print(df.head(5))
print(df_regress.head(5))
print(df_regress[df_regress.isna().any(axis=1)])
#drop out missing values
df_regress = df_regress.dropna()

#display the set of values that appear across each column
for column in df_regress:
    print(column, df_regress[column].unique())

#replace column with numbers
df_regress['Virus Strain'] = df_regress['Virus Strain'].map({'Influenza A H3N2v':0,'Influenza A H1N1v':0,'Influenza A H1N2v':1,'Influenza A H7N2':0})
df_regress['Age'] = df_regress['Age'].map({'<18 Years': 0,'>=18 Years': 1})
df_regress['Gender'] = df_regress['Gender'].map({'Female': 0,'female':0,'Male': 1,'male':1})
df_regress['Hospitalized?'] = df_regress['Hospitalized?'].map({'no': 0,'No':0,'yes': 1,'Yes':1})
df_regress['Swine Contact?'] = df_regress['Swine Contact?'].map({'no': 0,'No':0,'yes': 1,'Yes':1})
df_regress['Attended Agricultural Event?'] = df_regress['Attended Agricultural Event?'].map({'no': 0,'No':0,'yes': 1,'Yes':1})



#---------------------------Logistic regression---------------------------------
import statsmodels.api as sm
import statsmodels.formula.api as smf

#split the data between endogenous (dependent) and exogenous (independent) variables
endog = df_regress['Virus Strain']
exog = df_regress[['Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]
#to fit a y-intercept parameter, we must add a data column with all values equal to 1.
exog = sm.add_constant(exog)
#logistic regression
logit = smf.Logit(endog, exog)
result = logit.fit()
result.summary()

import numpy as np
print('Odds ratios:')
print(np.exp(result.params))