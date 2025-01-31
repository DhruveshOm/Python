# Question 1: Data Transformation and Analysis
# You are working as a data analyst for a company that deals with large datasets. Your team receives a 2D NumPy array containing customer transaction data,
#  where each row represents a different customer, and, columns represent transaction amounts in different months. a. np random randint(10,500, 24,5)) Using NumPy functions.
# 1. Find the maximum, minimum, and total transaction amount across all customers.
# 2. Compute the cumulative sum of transactions column-wise.
# 3. Flatten the 2D array into a 1D array and sort the transactions in ascending order.
# 4. Transform the dataset by reshaping it into a different structure.
# Write Python code to achieve these tasks and explain the significance of each function in data transformation.
# #Sample transaction data (4 customers, 5 months)
# 
# 
# Question 2: Matrix Operations and Computation
# A company is working on an Al-based recommendation system and needs to perform several matrix operations. The dataset consists of two matrices:
# Matrix A (User-Product Interaction): Contains ratings given by users to different products.
#Matrix B (Product-Feature Mapping): Contains product attributes that help in recommendations.
# Using NumPy:
# 1. Perform element-wise multiplication of the user-product interaction matrix with another similar matrix,
# 2. Compute the matrix multiplication of A and B using two different NumPy fumubons.
# 3. Find the transpose of matrix A and explain its significance in collaborative filtering.
# 4. Identify the shape, number of dimensions, and data type of matrix B.
# Write Python code to perform these operations and explain how these transformations are used in recommendation systems.
# #Defining matrices
# Anp.array([15, 3, 2), (4, 1, 5), (3, 2, 4]]) # User-Product interaction
# B= np.array([[1, 2], [3, 4], [5, 6]]) # Product-Feature Mapping










############################ ANSWER 1 #####################
import numpy as np
a = np.random.randint(10, 500, (4, 5))
cumulative_sum = np.cumsum(a, axis=0)
print(a)
print("Sum: ",np.sum(a))
print("MAX: ",np.max(a))
print("Min: ",np.min(a))
print("Cumalitive sUm: ", cumulative_sum)
dimChange = a.flatten()
print("2D in 1D :",dimChange)
print("Reshape : ", a.reshape(2,10))



###################### ANSWER 2 ####################

A = np.array([[15, 3, 2], [4, 1, 5], [3, 2, 4]]) 
B = np.array([[1, 2], [3, 4], [5, 6]]) 
print(A*A)
