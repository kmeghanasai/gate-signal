import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Read data from file
data_file = "output_data.txt"
t, x, y = np.loadtxt(data_file, skiprows=1, unpack=True)

# Interpolation for smoother curve
t_smooth = np.linspace(min(t), max(t), 1000)
f_x = interp1d(t, x, kind='cubic')
f_y = interp1d(t, y, kind='cubic')
x_smooth = f_x(t_smooth)
y_smooth = f_y(t_smooth)

# Plotting
plt.plot(t_smooth, x_smooth, label='x(t)', color='blue')
plt.plot(t_smooth, y_smooth, label='y(t)', color='red')
plt.xlabel('t')
plt.ylabel('Function Value')
plt.title('x(t) and y(t) vs t')
plt.legend()
plt.grid(True)
plt.savefig('figr.png')
plt.show()
