import pandas as pd
import numpy as np
# a = pd.Series([1,2,3,4])
# print(a)
# b = pd.DataFrame()
# print(b)
# c = pd.DataFrame([1,2,3,4])
# print(c)
d = pd.DataFrame([[1,20,'Adi'],[2,34,'parth'],[3,60,'rounak'],[4,70,'dhruv']],columns=['Roll no.', 'id','name'],index=['a.','b.','c.','d.'])
print(d)
# print(d.loc['a.'])
# print(d.iloc[1])