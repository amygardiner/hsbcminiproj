#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:30:14 2022

@author: amygardiner

ARIMA model showing similar limitation using test-train split and predict method rather than forecasting
"""

import pandas as pd
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Assumed the file was downloaded from S3
df1 = pd.read_csv('Tst2022-01-04tapes.csv',usecols=[2,3],nrows=400,names=['time','value'], header=None)
# Removing duplicate entries at given time by using mean
df1=df1.groupby('time').mean().reset_index()
df=df1.value


# Train-test split
df_train=df[0:230]
df_test=df[231:282]

start = len(df_train)
end = len(df_train) + len(df_test) - 1

# 1,1,1 ARIMA Model
arima=ARIMA(df_train,order=(1, 1, 1))
arima_mod=arima.fit()

# Actual vs Fitted
arima_pred=arima_mod.predict(start, end,
                             typ = 'levels').rename("Predictions")
  
# plot predictions and actual values
arima_pred.plot(legend = True)
df_test.plot(legend = True)