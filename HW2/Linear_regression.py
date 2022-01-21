#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import scipy.stats as stats

def LinearRegression(X,Y):
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)

    X_train = np.array(X_train)
    Y_train = np.array(y_train)
    Y_train = Y_train.reshape(-1,1)

    #prediction of y with the linear function
    mult = np.linalg.inv(np.matmul(np.transpose(X_train), X_train))
    beta = np.linalg.multi_dot([mult, np.transpose(X_train), Y_train])
    y_pred=np.matmul(X_train, beta)

    n=len(X_train)
    k=len(X_train[0])

    #error and sigma calculation
    error=Y_train-y_pred

    var1=np.matmul(error.transpose(),error)/(n-k-1)
    var2=np.diag(np.multiply(var1,np.linalg.inv(np.matmul(np.transpose(X),X))))

    sigma = np.sqrt(var2).reshape(-1,1)

    # t-critical value and CI
    alfa = 0.05
    t_critical = stats.t.ppf(q = 1-alfa/2, df= n-k-2)  

    MOE = t_critical * sigma

    confidence_interval = (np.subtract(beta , MOE),
                            np.add(beta , MOE)) 
    
    return beta, sigma, confidence_interval,MOE

