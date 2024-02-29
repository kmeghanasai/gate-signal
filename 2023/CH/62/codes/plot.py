import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y(t):
    return 1.05 * (1 - np.exp(-(t - 1) / 2)) * (t >= 1)

# Read data from file
with open("linspace.txt", "r") as file:
    t_values = [float(line.strip()) for line in file]

# Calculate y values
y_values = y(np.array(t_values))

# Plot the function
plt.plot(t_values, y_values, label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Plot of y(t)')
plt.grid(True)

# Highlight the point where t = 7.073
highlight_t = 7.073
highlight_y = y(highlight_t)
plt.scatter(highlight_t, highlight_y, color='red', label=f't = {highlight_t}, y = {highlight_y}')
plt.legend()

plt.savefig('fig1.png')
