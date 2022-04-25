#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:43:45 2022

@author: amygardiner

Random forest regression with all the combined feature data
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt

dataset=pd.read_csv('allcombined.csv')
x = dataset.drop(['Price'], axis=1)
x = x.dropna(axis=1)

y = dataset['Price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
