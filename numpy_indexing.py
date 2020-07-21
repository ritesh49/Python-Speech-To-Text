# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:18:31 2020

@author: ritesh_ramchandani
"""
import numpy as np

arr=np.arange(0,11);
arr[3]
arr[1:5]

arr[:6]
arr[5:]
arr[0:5]=100 #broadcasting array is only in mumpy
arr=np.arange(0,11)
slice_of_arr=arr[0:6]
slice_of_arr[:]=100 #also change the orignal arr
arr_copy=arr.copy()
arr_copy[:]=100

arr_2d=np.array([[1,2,3],[34,45,65],[65,23,53]])
arr_2d[0][0]
arr_2d[0] #index entire row

#NUMPY OPERATIONS
arr=np.arange(0,11)
arr + arr
arr*arr
arr+100
arr/100
arr*100
arr/arr #--> 0/0 gives nan
1/arr #--> 1/0 gives infinite
arr **2
np.sqrt(arr)#takes square root of every ele in array
#unicersal function in numpy array
np.exp(arr)
np.max(arr)
np.sin(arr)
np.log(arr)


#PANDAS
import pandas as pd
labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}
pd.Series(data=my_data)
pd.Series(data=my_data,index=labels)

pd.Series(my_data,labels)

pd.Series(arr)
pd.Series(d)
pd.Series(data=labels)

#also holds built- in function
pd.Series(data=[sum,print,len,'ritesh'])

ser1=pd.Series([1,2,3,4],['IND','USA','BIHAR','JAPAN'])
ser2=pd.Series([1,2,5,4],['IND','USA','ITAY','JAPAN'])

ser1['USA']
ser1 + ser2

#DATA FRAMES
from numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

df['W']

df.W
df[['W','Z']]
df.['new'] = fd['W']+df['Y']
df.drop('new',axis=1,inplace=True) #axis used for referring columns
df.drop('E',axis=0)
df.shape
#ROWS
df.loc['A']
df.iloc[2]
df.loc['B','Y']
df.loc[['A','B'],['X','Y']]