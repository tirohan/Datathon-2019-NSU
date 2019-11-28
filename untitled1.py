# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:47:40 2019

@author: Tanbin Islam Rohan
"""

import pandas as pd

data1= pd.read_csv('final_data.csv')

train_data1= pd.DataFrame(data1)
print(train_data1.info())
train_data1=train_data1.dropna()
print(train_data1.info())

#create dataframe .
print(train_data1.describe())