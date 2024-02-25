import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data = np.loadtxt("data.txt")

# Extract time and function values
time = data[:, 0]
x_t = data[:, 1]

# Plot the data
plt.plot(time, x_t, label=r'$39.24 \sin(5t + \frac{\pi}{2})$')
plt.title('Plot of x(t)')
plt.xlabel('Time (t)')
plt.ylabel('x(t) (cm)')
plt.legend()
plt.grid(True)
plt.savefig('xe_71_f2')

