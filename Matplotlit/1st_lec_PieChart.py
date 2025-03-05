from cProfile import label
from pickle import TRUE
import matplotlib.pyplot as plt
from numpy import size

#dAta
models = ['Volvo', 'Suzuki', 'Ford','BMW']
share = [15,35,30,20]
myexplode = [0.2, 0, 0, 0]
mycolors = ["silver", "hotpink", "b", "#4CAF50"]
colorr = ["b",""]
#create pie chart
plt.pie(share ,labels=models ,explode=myexplode,colors=mycolors,autopct='%1.1f%%',shadow=True)

#autopct: The format string defines hwo the percentage appear

#Add title
plt.title("Car's in indian market")

# Show the plot
plt.show()
