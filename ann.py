#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:51:15 2018

@author: renatkhalikov
"""

# In[1]:

# ===========================
# Data Preprocessing
# ===========================

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
Dataset Information:
    Data Set Characteristics: Multivariate
    Attribute Characteristics: Integer, Real
    Number of Attributes: 24
    Number of Instances: 30000
    Source: 
        UCI Machine Learning Repository
        institutions: (1) Department of Information Management, Chung Hua University, Taiwan. (2) Department of Civil Engineering, Tamkang University, Taiwan. 
    

Dataset Attributes:
    This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. 
    This study reviewed the literature and used the following 23 variables as explanatory variables: 
        
    X1: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit. 
    X2: Gender (1 = male; 2 = female). 
    X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others). 
    X4: Marital status (1 = married; 2 = single; 3 = others). 
    X5: Age (year). 
    X6 - X11: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows: X6 = the repayment status in September, 2005; X7 = the repayment status in August, 2005; . . .;X11 = the repayment status in April, 2005. The measurement scale for the repayment status is: -1 = pay duly(paid appropriately); 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above. 
    X12-X17: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005. 
    X18-X23: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005.
'''


# Import the dataset
# Note we have two headers in dataset, skip the extra row
dataset = pd.read_excel('dataset/default-of-credit-card-clients.xls', skiprows=1)

