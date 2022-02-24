#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:36:14 2022

@author: amygardiner

Hypothesis test and differencing for stationarity of tape data using average price over every 500 instances
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import matplotlib.pyplot as plt
import math

# Assumed the file was downloaded from S3
df = pd.read_csv('Tst2022-01-04tapes.csv',usecols=[2,3],names=['time','value'], header=0)
#print(len(df))

num_groups = int(math.ceil(len(df)/500))
#print(num_groups)

means=[]

def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)

for i in nums(1,num_groups):
    if i==1:
        mean=np.sum(df.value[0:(i*500)-1])/500
    elif 1<=i<=(num_groups-1):
        mean=np.sum(df.value[((i-1)*500)-1:(i*500)-1])/500
    means.append(mean)
    
df = pd.DataFrame(data=means)

# KPSS Test    
result = kpss(df, regression='c', nlags="legacy")
print('\nKPSS Statistic: %f' % result[0])
print('p-value: %f' % result[1])
for key, value in result[3].items():
    print('Critial Values:')
    print(f'   {key}, {value}')

diff=df.diff().dropna()

# KPSS Test on differenced data    
result = kpss(diff, regression='c', nlags="legacy")
print('\nKPSS Statistic of differenced data: %f' % result[0])
print('p-value of differenced data: %f' % result[1])
for key, value in result[3].items():
    print('Critial Values:')
    print(f'   {key}, {value}')
    
# Original Series
fig, axes = plt.subplots(2, 2, sharex=True)
axes[0, 0].plot(df); axes[0, 0].set_title('Original Series')
plot_acf(df, ax=axes[0, 1], lags=len(df)-1)

# 1st Differencing
axes[1, 0].plot(diff); axes[1, 0].set_title('1st Order Differencing')
plot_acf(diff.dropna(), ax=axes[1, 1], lags=len(df)-2)

# PACF plot of 1st differenced series
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(diff); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,5))
plot_pacf(diff.dropna(), ax=axes[1])

plt.show()

