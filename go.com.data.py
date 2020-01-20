#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:12:54 2020

@author: meixiangui
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# load data 
sales = pd.read_excel("Go.com_Assignment_Data.xlsx", header = 4,usecols = [1,2,3])
revenue = pd.read_excel("Go.com_Assignment_Data.xlsx", "Historical Data", 
                        header = 5, skipfooter = 7, 
                        usecols = [1,2,3,4,5,6], index_col = 0)
revenue = revenue.drop(revenue.index[0])

profit = pd.read_excel("Go.com_Assignment_Data.xlsx", "Historical Data", 
                        header = 13,
                        usecols = [1,2,3,4,5,6], index_col = 0)
profit.columns = revenue.columns

# calculate the revenue for different firm in 2015 Q1
rev_q1 = sales.groupby('Product Line').Revenue.sum()
revenue['Q1 2015'] = rev_q1
revenue.loc['Total','Q1 2015'] = sum(revenue['Q1 2015'][0:3])

# calculate the profit for different firm in 2015 Q1
mul = revenue['Q1 2014'] / profit['Q1 2014']

profit['Q1 2015'] = None
profit['Q1 2015'].iloc[0] = revenue['Q1 2015'].iloc[0]/mul.iloc[0]
profit['Q1 2015'].iloc[1] = revenue['Q1 2015'].iloc[1]/mul.iloc[1]
profit['Q1 2015'].iloc[2] = revenue['Q1 2015'].iloc[2]/mul.iloc[2]
profit.loc['Total','Q1 2015'] = sum(profit['Q1 2015'][0:3])

growth = profit.loc['Total','Q1 2015'] / profit.loc['Total','Q4 2014'] - 1

# plot the trend 
for i in range(4):
    plt.plot(profit['Q4 2013'].iloc[i],profit['Q1 2014'].iloc[i],profit['Q2 2014'].iloc[i],   
             profit['Q3 2014'].iloc[i], linestyle='--')
    







