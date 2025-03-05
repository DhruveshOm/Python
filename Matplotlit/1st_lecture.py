from cProfile import label
from turtle import color
from matplotlib import markers
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Question :  draw a bar diagram, line diagram.


########## Pie chart ############
# Pie charts are used to represent data as proportional slices of a circle, 
# showing the relative proportions of different categories within a whole. 
# They are simple and easy to understand, best suited for a limited number of categories
#  where the data adds up to 100%. However, they can be difficult for comparing slice 
# sizes and cannot represent negative or zero values.


######### Scatter Plots #########
# Scatter plots are used to display the relationship between two continuous variables. 
# They are excellent for visualizing the type and strength of the relationship, 
# identifying outliers and clusters, and exploring data for predictive modeling.
#  However, they cannot represent categorical variables directly and can suffer from overplotting. 
# Correlation does not imply causation.


########## Bar diagram ########
# Bar diagrams (bar charts) are used to compare the values of different categories using rectangular bars.
#  They are easy to read and understand, and can represent categorical or numerical data, 
# including time series data. However, they are not ideal for showing proportions of a whole,
#  and the scale must be chosen carefully to avoid misleading the viewer. 
# They are also not suitable for showing relationships between variables.




# Create data
x = [1,2,3,4,5]
y = [10,20,25,30,40]

# Create a plot
plt.plot(x,y, marker='X',linestyle=':',color='burlywood',label='Line1')
'''marker :
'o' Circle,'^' Triangle (Up),'v' Triangle (Down)
's' Square,'*' Star,'D' Diamond
'x' Cross,'+' Plus sign,'p' Pentagon
'h' Hexagon,'.' small dot'''

#Add labels and title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Basic Line Plot")

#Show legend
plt.legend()

#Display 
plt.show()






