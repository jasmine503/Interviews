#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:35:38 2019

@author: meixiangui
"""

import numpy as np 

#######Problem B#######

# 7
K1 = 11
K2 = 10
S0 = 10
sigma = 0.7
rf = 0.02
T = 1
paths = 10000
steps = 1000

def StockPrices(S0,rf,sigma,T,paths,steps):
    dt = T/steps
    # Generate stochastic process and its antithetic paths
    Z = np.random.normal(0,1,paths * steps).reshape((paths, steps))   
    dWt = np.sqrt(dt) * Z
    # bind the normal and antithetic Wt
    St = np.zeros((paths, steps + 1))
    St[:, 0] = S0  
    for i in range (1, steps + 1):
        St[:,i] = St[:,i-1]*np.exp((rf-1/2*np.power(sigma, 2))*dt + sigma*dWt[:,i-1])
    return St

def warrant(K1,K2,rf,sigma,S0,T,paths,steps):
    warrant = np.zeros(paths)
    
    s = StockPrices(S0,rf,sigma,T,paths,steps)
    s_half = s[:,int(steps/2)]
    s_mat=s[:,int(steps)]
    
    for i in range (paths):
        if ((s_half[i] >= 12) or (s_mat[i] >= 14)):
           warrant[i] = max(s_mat[i] - K1,0)
        else: 
           warrant[i] = max(s_mat[i] - K2,0)           
    return warrant

warrant_mat = warrant(K1,K2,rf,sigma,S0,T,paths,steps)
price = np.exp(-rf)*(1/paths)*np.sum(warrant_mat)
print ("the price of the warrant is:", price)

2.5392


    
    
