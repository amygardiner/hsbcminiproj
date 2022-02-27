#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:32:06 2022

@author: amygardiner

Looking at the csv datafiles from the S3 bucket
"""
import pandas as pd
import matplotlib.pyplot as plt

urls=["https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-04tapes.csv", "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-05tapes.csv", "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-06tapes.csv", "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-07tapes.csv", "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst2022-01-10tapes.csv"]

for i in urls:
    df= pd.read_csv(i, usecols=[2,3], header=None)
    df.columns =['Time', 'Price']

    plt.figure()
    plt.plot(df.Time, df.Price, linewidth=0.1)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title(f'Original Series from {i}')
    plt.show()
    
