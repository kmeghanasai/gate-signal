import matplotlib.pyplot as plt

# Read data from the file
with open('data1.txt', 'r') as file:
    x_values = [float(line.strip()) for line in file]

# Define the range of n values
n_values = range(-1, 4)

# Plot the graph
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Graph of x(n)')
plt.grid(True)
plt.show()
