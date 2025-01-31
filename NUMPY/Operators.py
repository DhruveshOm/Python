from re import L
import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print(a-b)
print(a**2)
print(a*b)
a = np.arange(6).reshape(2,3)
print(a.ndim)
b = np.arange(10,22,2).reshape(3,2)
print(b.ndim)
print(b@a)
print(a.dot)


# Array Dimensions
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.dtype.name)
print(a.itemsize)   #This returns the size (in bytes) of each element in the array.
                    #Since a has int64 data type (which uses 8 bytes per element)
print(type(a))


