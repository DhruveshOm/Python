import numpy as np
from matplotlib import category
import matplotlib.pyplot as plt

#Data
categories = ['Nike' , 'Adidas ' , 'Red-chief' , 'comet']
values = [20 , 15 , 19 , 8]

#Create bar chart
plt.bar(categories,values,color='lightblue')

#Add labels and title
plt.xlabel("Company's")
plt.ylabel("Values")
plt.title("Sales Chart")

#Show the plot
plt.show()


