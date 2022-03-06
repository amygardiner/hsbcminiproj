#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:36:14 2022

@author: amygardiner

ARIMA model for approx. 2 min interval of tape data
"""

import pandas as pd
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt


# Assumed the file was downloaded from S3
df1 = pd.read_csv('Tst2022-01-04tapes.csv',usecols=[2,3],nrows=250,names=['time','value'], header=0)
df=df1.value

# KPSS Test    
result = kpss(df, regression='c', nlags="legacy")
print('\nKPSS Statistic: %f' % result[0])
print('p-value: %f' % result[1])
for key, value in result[3].items():
    print('Critial Values:')
    print(f'   {key}, {value}')
    
# P value < 0.05 hence reject null hypothesis of stationarity

diff=df.diff().dropna()

# KPSS Test on differenced data    
result = kpss(diff, regression='c', nlags="legacy")
print('\nKPSS Statistic of differenced data: %f' % result[0])
print('p-value of differenced data: %f' % result[1])
for key, value in result[3].items():
    print('Critial Values:')
    print(f'   {key}, {value}')
    
# Hence differencing order is 1 (d) 
# Although could be 0 with weak stationarity
    
# Original Series
fig, axes = plt.subplots(2, 2, sharex=True)
axes[0, 0].plot(df); axes[0, 0].set_title('Original Series')
plot_acf(df, ax=axes[0, 1], lags=len(df)-1)

# 1st Differencing
axes[1, 0].plot(diff); axes[1, 0].set_title('1st Order Differencing')
plot_acf(diff.dropna(), ax=axes[1, 1], lags=len(df)-2)

# PACF plot of original and 1st differenced series
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(2, 2, sharex=True)
axes[0, 0].plot(df); axes[0, 0].set_title('Original Series')
axes[1,0].plot(diff); axes[1,0].set_title('1st Differencing')
plot_pacf(df, ax=axes[0,1])
plot_pacf(diff.dropna(), ax=axes[1,1])
plt.show()

# AR term 1 (p) as one lag point majorly above significance line in PACF
# MA term 1 (q) similar in ACF

# ACF plot shows overdifference so increasing MA term could remedy


# 1,1,1 ARIMA Model
arima=ARIMA(df,order=(1, 1, 1))
arima_mod=arima.fit()
print(arima_mod.summary())

# 0,2,2 ARIMA Model
arima_mod_2 = ARIMA(df, order=(0, 2, 2)).fit()
print(arima_mod_2.summary())
# High P>|z| for ma weight shows 1,1,1 model may be best 

# Plot residual errors
residuals = pd.DataFrame(arima_mod.resid)
residuals = residuals[1:]
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])
plt.show()
# 0 mean as required

# Actual vs Fitted
arima_pred=arima_mod.predict(dynamic=False)
arima_pred.pop(0)

#plt.subplot()
plt.figure(4)
plt.plot(df, label="data")
plt.plot(arima_pred, label="predictions")
plt.title("ARIMA(1,1,1) on from t=8.192 to t=138.144s on 04/01/22")
plt.legend()
plt.show()

