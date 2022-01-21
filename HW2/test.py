#!/usr/bin/env python
# coding: utf-8

# In[7]:


import scipy.stats as stats
import wbdata
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import Linear_regression
import statsmodels.api as sm


x=np.array([1,2,np.nan,3,4,5,np.nan,np.nan,np.nan,6,7,8,9,10])
x=x.reshape((7,2))
x = pd.DataFrame(x)
y = np.array([2,1,4,5,1,3,3])


a,b,c,d = Linear_regression.LinearRegression(x,y)


# In[8]:


x = sm.add_constant(x)
OLS_benchmark = sm.OLS(y,x).fit()
print(OLS_benchmark.summary())


# In[ ]:




