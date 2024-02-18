import matplotlib.pyplot as plt

# Read data from the file
with open('data2.txt', 'r') as file:
    x_p_values = [float(line.strip()) for line in file]

# Define the period and number of cycles
period = 5
num_cycles = 2

# Define the range of n values for the plotted data
n_values = range(0, period * num_cycles)

# Plot the graph
plt.stem(n_values, x_p_values)
plt.xlabel('n')
plt.ylabel('x_p(n)')
plt.title('Graph of x_p(n)')
plt.grid(True)
plt.show()
