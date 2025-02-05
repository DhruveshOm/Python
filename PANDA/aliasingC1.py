from ast import Str
import pandas as pd
import numpy as np
# data = np.array(['a' , 'b' , 'c' , 'd'])
# s = pd.Series(data,index=[100,111,112,113])
# print(s)


###### import the pandas libraby and aliasing as pd
d = {'a' : 0., 'b' : 1., 'c' : 2.}
si = pd.Series(d)
print(si)


### Create series from dictionary using pandas
data1 = {'Ahmed':92 , 'Ali': 55 , 'Omar' : 83}
s1 = pd.Series(data1,index=['Ali' , 'Ahmed','Omar'])
print(s1)


data2 = np.arange(5)
s2 = pd.Series(data2,index=['a' , 'b' , 'c' ,'d' ,'e'])
print(s2)

a = pd.Series(data2,index=['a','b','c','d','e'])
print(a)
print(type(a))