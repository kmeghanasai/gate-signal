import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("data.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the 8 terms of the data
x_n = data[:8]
highlighted_index = 1
# plot the graph
plt.stem(range(1, len(data) + 1), x_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.stem([highlighted_index], [data[highlighted_index - 1]], linefmt='r-', markerfmt='ro', basefmt=' ')# Set labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(range(1, len(data) + 1))
# Add legend
plt.legend()
plt.grid(True)
plt.savefig("fig4.png")
