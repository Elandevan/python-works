# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:09:30 2021

@author: saras
"""
import pandas as pd
from scipy.stats import *
import matplotlib.pyplot as plt

df = pd.read_csv('E:/New folder/2021 - 2022/Lab/Age&height.csv')
print(df.head(3))

x = df['Weight']
y = df['Index']
slope, intercept, r, p, std_err = linregress(x, y)
print('slope = ',slope)
print('Intercept = ', intercept)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print('Regression = ', r)
#Predict the index of a person whose weight is 110:
index = myfunc(110)
print('Predicted value of index of a person whose weight is 110:',round(index))




