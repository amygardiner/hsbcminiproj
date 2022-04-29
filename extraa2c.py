#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:55:13 2022

@author: amygardiner

Creating daily features for A2C with datasets 2 (and 3)
"""

import pandas as pd
import numpy as np

urls=["https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-04tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-05tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-06tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-07tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-10tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-11tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-12tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-13tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-14tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-17tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-18tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-19tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-20tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-21tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-24tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-25tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-26tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-27tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-28tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-01-31tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-01tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-02tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-03tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-04tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-07tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-08tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-09tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-10tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-11tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-14tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-15tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-16tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-17tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-18tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-21tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-22tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-23tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-24tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-25tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-02-28tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-01tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-02tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-03tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-04tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-07tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-08tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-09tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-10tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-11tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-14tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-15tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-16tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-17tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-18tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-21tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-22tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-23tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-24tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-25tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-28tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-29tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-30tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-03-31tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-01tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-04tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-05tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-06tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-07tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-08tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-11tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-12tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-13tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-14tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-19tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-20tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-21tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-22tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-25tapes.csv",
      "https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-26tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-27tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-28tapes.csv","https://dsc-mp2022-opt.s3.amazonaws.com/proj-b/dataset-b02/TstB02_2022-04-29tapes.csv"]

Open=[]
High=[]
Low=[]
Close=[]
Volume=[]

for i in urls:
    df= pd.read_csv(i, usecols=[3,8], header=None)
    df.columns =['Price', 'Quantity']
    df['Quantity']=df['Quantity'].str[8:]
    df['Quantity'] = df['Quantity'].astype(int) 
    Open.append(df['Price'][0])
    High.append(df['Price'].max())
    Low.append(df['Price'].min())
    Close.append(df['Price'][len(df)-1])
    Volume.append(df['Quantity'].sum())
    
    
data = pd.DataFrame(list(zip(Open,High,Low,Close,Volume)))    
data.to_csv('b02_a2c_data.csv')