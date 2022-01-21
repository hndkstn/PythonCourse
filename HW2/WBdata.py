#!/usr/bin/env python
# coding: utf-8

# In[66]:


get_ipython().system('pip install wbdata')
get_ipython().system('pip install world_bank_data')

import wbdata
import world_bank_data as wb
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import scipy.stats as stats
import Linear_regression
import statsmodels.api as sm

#wb.get_topics()
#wb.get_indicators(topic=19).iloc[26:,:]

#indicator data selection
import wbgapi as wb
wb.series.info(q='GDP')
import wbdata
wbdata.search_indicators('GDP')


ind = {"NY.GDP.MKTP.CD": "GDP",
       "NY.GDP.DEFL.KD.ZG" : "Inflation, GDP deflator (annual %)",
              "BX.KLT.DINV.WD.GD.ZS": "Foreign direct investment, net inflows (% of GDP)",
              "AG.LND.AGRI.ZS": "Agricultural land",
              "NE.EXP.GNFS.ZS": "Exports of goods and services (% of GDP)",
              "NE.IMP.GNFS.ZS": "Imports of goods and services (% of GDP)",
              "GFDD.DI.02": "Deposit money banks'' assets to GDP (%)" 
      }

data_dates = (datetime.datetime(1900, 1, 1), datetime.datetime(2020, 1, 1))

data = wbdata.get_dataframe(indicators=ind, 
                            country=('GBR'), 
                            data_date=data_dates, 
                            convert_date=False, keep_levels=True)

data=data.loc[data.index[data.isna().any(axis=1)==False]]

data.to_csv('wbdata.csv')

#Dependent variable
Y = data['GDP']
#Independent variable
X = data.iloc[:,1:]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)

beta, sigma, CI, y_pred = Linear_regression.LinearRegression(X_train,y_train)

#figure target vs variables

plt.figure(figsize=(60,30))
plt.subplot(3,2,1)
sns.regplot(x=data.columns[1], y="GDP", data=data)
sns.set_style("whitegrid")

plt.subplot(3,2,2)
sns.regplot(x=data.columns[2], y="GDP", data=data)
sns.set_style("whitegrid")

plt.subplot(3,2,3)
sns.regplot(x=data.columns[3], y="GDP", data=data)
sns.set_style("whitegrid")

plt.subplot(3,2,4)
sns.regplot(x=data.columns[4], y="GDP", data=data)
sns.set_style("whitegrid")

plt.subplot(3,2,5)
sns.regplot(x=data.columns[5], y="GDP", data=data)
sns.set_style("whitegrid")

plt.subplot(3,2,6)
sns.regplot(x=data.columns[6], y="GDP", data=data)
#sns.set_style("whitegrid")

plt.show()



X = sm.add_constant(X)
OLS_benchmark = sm.OLS(Y,X).fit()
print(OLS_benchmark.summary())


# In[ ]:




