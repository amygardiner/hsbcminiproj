#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:11:42 2022

@author: amy and brooke
Neural Prophet for small section of tape data
"""
# importing file 
import pandas as pd
import datetime
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt

#data_path = 'Tst2022-01-04tapes.csv'
data_path = '/Users/brookegrantham/Documents/Tst2022-01-04tapes.csv'

raw_data = pd.read_csv(data_path, header=None, usecols=[2,3], na_filter=False, nrows=400, names=('Time','value'))
raw_data.Time=round(raw_data.Time)

raw_data.insert(0,'date_time', '04-01-2022 ')


# Converting milliseconds into time format
for i in range(len(raw_data.Time)):
    raw_data['Time'][i] = str(datetime.timedelta(seconds=raw_data['Time'][i]))
raw_data.head()

# combining the date and time columns 
raw_data['final_date'] = raw_data.date_time.str.cat(raw_data.Time)
raw_data.head()

# creating the data frame --- neural phrophet needs the columns labelled ds and y for date and the data
data2 = pd.DataFrame({'ds': raw_data.final_date, 'y':raw_data.value.astype(int)})
data2

data2=data2.groupby('ds').mean().reset_index()

# attempting the apply neural prophet to the data 
#clf = NeuralProphet(n_changepoints=15, n_lags=1, n_forecasts=1)
#model = clf.fit(data2)

#forecast = clf.predict(data2)
#fig_forecast = clf.plot(forecast)
#fig_components = clf.plot_components(forecast)
#fig_model = clf.plot_parameters()

# forecast prediction -short range
clf = NeuralProphet(n_lags=1, n_forecasts=4)
model = clf.fit(data2, freq='S')
forecast = clf.predict(data2)
future = clf.make_future_dataframe(data2, n_historic_predictions=True,periods=4)
future_forecast = clf.predict(future)


#full forecast
plt.plot(future_forecast['ds'],future_forecast['y'],label='data')
plt.plot(forecast['ds'],forecast['yhat1'], label='predictions')
plt.plot(future_forecast['ds'].tail(5),future_forecast['yhat1'].tail(5), label='forecast')
plt.title('NeuralProphet from t=8.192 to t=138.144 on 04/01/22')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()