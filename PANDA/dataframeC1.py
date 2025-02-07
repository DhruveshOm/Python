import pandas as pd
import numpy as np
# a = pd.Series([1,2,3,4])
# print(a)
# b = pd.DataFrame()
# print(b)
# c = pd.DataFrame([1,2,3,4])
# print(c)


c = {
    'name' :['adi' , 'rounak' , 'parth'],
    'roll no.':[30 ,32,34],
    'Marks':[99,98,100]
}
print(pd.DataFrame(c,index=['a','b','c']))


# print(d.loc['a.'])
# print(d.iloc[1])
# d = pd.DataFrame([[1,20,'Adi'],[2,34,'parth'],[3,60,'rounak'],[4,70,'dhruv']],columns=['Roll no.', 'MARKS','name'],index=['a.','b.','c.','d.'])
# print(d)