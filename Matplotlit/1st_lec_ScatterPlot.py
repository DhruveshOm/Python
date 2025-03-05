
import matplotlib.pyplot as plt

#sample data
x = [1,2,3,4,5]
y = [10,20,15,25,35]
# create a plot
plt.plot(x,y,marker="*",linestyle= '-',color='tan',label='Line 1')

#Create a Scatter plot 
plt.scatter(x,y,color='red',marker='*',s = 100) 
# s sets the marker size

#Add labels and title
plt.xlabel("X-axis")
plt.xlabel("Y-axis")
plt.title("Scatter Plot Diagram")

#Diagram the plot
plt.show()