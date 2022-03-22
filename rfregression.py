#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:43:45 2022

@author: amygardiner

Random forest regression with the combined feature data for 04/01/22
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt

dataset=pd.read_csv('040122CombinedFeatures.csv')
x = dataset.drop(['Price','index','EMA10Days','EMA16Days','EMA22Days'], axis=1)
y = dataset['Price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

"""
# Plot first decision tree, very slow to run and image is totally saturated

fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(regressor.estimators_[0],
               feature_names = x.columns, 
               class_names='Price',
               filled = True);
fig.savefig('rf_individualtree.png')
"""