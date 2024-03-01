import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(t):
    return (2*t + t**2/2) * (t >= 0) \
        - (2*(t-4) + ((t-4)**2)/2) * (t >= 4) \
        - (2*(t-2) + ((t-2)**2)/2) * (t >= 2) \
        + (2*(t-6) + ((t-6)**2)/2) * (t >= 6)

# Generate t values
t_values = np.linspace(0, 10, 1000)

# Calculate the function values
y_values = f(t_values)

# Find maximum value and its index
max_value = np.max(y_values)
max_index = np.argmax(y_values)

# Plot the function
plt.plot(t_values, y_values, label=r'$z(t)$')

# Mark the maximum value
plt.scatter(t_values[max_index], max_value, color='red', label=f'Maximum: ({t_values[max_index]:.2f}, {max_value:.2f})')

# Draw a vertical line at t=4
plt.axvline(x=4, color='green', linestyle='--', label='t=4')

plt.xlabel('t')
plt.ylabel('z(t)')
plt.title('Plot of the function')
plt.legend()
plt.grid(False)
plt.show()

