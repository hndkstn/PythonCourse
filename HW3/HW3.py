#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# In[2]:


data = pd.read_csv('cses4_cut.csv')
print(data)


# In[3]:


x = data.iloc[:, :-1]
y = data.iloc[:, -1]


# In[4]:


#One hot encoding

OHE = OneHotEncoder(handle_unknown='ignore')
OHE.fit(x)

#split train and test data

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.70, test_size=0.30)


# In[5]:


model = GaussianNB() 
model.fit(X_train, y_train) 
y_hat = model.predict(X_test)

accuracy_score(y_test, y_hat)


# In[7]:


# Variable selection

k_best = SelectKBest(score_func=chi2, k='all')
kBestScores = k_best.fit(x, y).scores_

dicts={}
dicts = dict(zip(data.columns, kBestScores))
sort_dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)


# In[9]:


print(sort_dicts)
# High scored features: D2026,D2027,D2029,D2021,D2011,D2030,D2022,D2028,D2023,D2015,age,D2016

#most effective features in target prediction
X = data[['D2026', 'D2027', 'D2029', 'D2021', 'D2011', 'D2030', 'D2022', 'D2028', 'D2023','D2015','age','D2016']]

#split train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.70, test_size=0.30)


# In[10]:


#Gaussian Naive Bayes
model1 = GaussianNB() 
model1.fit(X_train, y_train) 
y_hat = model1.predict(X_test)

accuracy_score(y_test, y_hat)


# In[11]:


#Decision Tree
model2 = DecisionTreeClassifier() 
model2.fit(X_train, y_train) 
y_hat = model2.predict(X_test)

accuracy_score(y_test, y_hat)


# In[12]:


#RandomForest
model3 = RandomForestClassifier() 
model3.fit(X_train, y_train) 
y_hat = model3.predict(X_test)

accuracy_score(y_test, y_hat)

