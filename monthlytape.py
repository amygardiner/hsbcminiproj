#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:06:47 2022

@author: amygardiner

Combining daily tapes into a monthly csv with simplified structure
"""

import pandas as pd

df= pd.read_csv("https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-04tapes.csv", usecols=[2,3], header=None)
df.columns =['Time', 'Price']

month = [1]*len(df)
day=[4]*len(df)
df.insert(loc = 0,column = 'Month',value = month)
df.insert(loc = 1,column = 'Day',value = day)
df.to_csv('januarytapes.csv')


jan_days=[5,6,7,10,11,12,13,14,17,18,19,20,21,24,25,26,27,28,31]
jan_urls=["https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-05tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-06tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-07tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-10tapes.csv",
          "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-11tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-12tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-13tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-14tapes.csv",
          "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-17tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-18tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-19tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-20tapes.csv",
          "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-21tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-24tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-25tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-26tapes.csv",
          "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-27tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-28tapes.csv","https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-31tapes.csv"]

for i in range(len(jan_urls)):
    df= pd.read_csv(jan_urls[i], usecols=[2,3], header=None)
    df.columns =['Time', 'Price']

    month = [1]*len(df)
    day=jan_days[i]
    df.insert(loc = 0,column = 'Month',value = month)
    df.insert(loc = 1,column = 'Day',value = day)
    df.to_csv('januarytapes.csv', mode='a', header=False)