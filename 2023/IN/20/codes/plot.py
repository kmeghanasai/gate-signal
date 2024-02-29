import numpy as np
import matplotlib.pyplot as plt

# Define the time values (t)
t = np.linspace(-6, 6, 1000)  # You can adjust the range and number of points as needed

# Define the function x(t) = 1
x = np.heaviside(t,0)

# Plot the graph
plt.plot(t, x)
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.title('Graph of x(t) = 1')
plt.grid(True)
plt.savefig('x(t)_vs_t.png')
