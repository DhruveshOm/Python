import array
from re import I
import numpy as np

### 1d array
# a = input("Enter a number with space :")
# arr= np.array([int(i) for i in  a.split()])
# print(arr)


#### 2d array
n = int(input("Enter number of row : "))
m = int(input("Enter number of column: "))
arr = []
for i in range(n):
    row =input(f"Enter row {i+1} ").split()
    arr.append([int(x) for x in row])
arr=np.array(arr)
print(arr)

#### 3d array
# c = np.arange(18).reshape(3,3,2)
# print(c)




# l = [] //
# for i in range(1,11):
#     l.append(int(input()))

#// a = np.array(1)
# a.shape = (2,5)
# print(a)





 #Adding all the element in an array without using built in function
 #!d array 
# a = np.array([1,2,3])
# s= 0
# for i in a :
#     s=s+i
# print("Sum of all the elements are: ", s )

#2d array 
# a= np.array(([1,2 ,3],[4,5,6]))
# s=0
# for i in range(0,2):
#     for j in range(0,3):
#         s=s+a[i][j]

# print("Sum of all the element are:",s)

