### array funcion ##
import numpy as np
a=np.arange(6).reshape(2,3)
print("\nreshape", a)
b = np.zeros([2,3],dtype=int)
print("\nZeros",b)
c=np.zeros([2,3])
print("\nZeros",c)
d=np.full([2,3],10)
print("\nFull",d)
e=np.empty([3,3])
print("\nempty",e)
f=np.ones([2,3])
print("\nones",f)
g=np.ones([2,3],dtype=int)
print("ones",g)
h=np.eye(2,3)
print("eye",h)
print("max",np.max(a))
print("min",np.min(a))
print("sum",np.sum(a))
print("sort",np.sort(a))
print("abs",np.abs(-1))
print("sqrt",np.sqrt(a))
print("cummulative sum column wise",a.cumsum(axis=0))  # axis = 0 for coloumn. niche ki taraf 
print("cummulative sum row wise",a.cumsum(axis=1))     # axis = 1 for row.     right taraf
print("Flatten function",a.flatten())
print("Transpose function",a.transpose())
