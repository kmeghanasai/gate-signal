import numpy as np
import matplotlib.pyplot as plt

# Generate some data for demonstration
w = np.logspace(-1, 2, 100)  # Angular frequency values from 0.1 to 100 rad/s
gain = np.ones_like(w) * 8  # Constant gain of 8 dB

# Plotting
plt.figure()
plt.plot([0, np.log10(w[0])], [8, 8], 'k--')  # Plotting line from (0,8) to first point
plt.plot(np.log10(w), gain)
plt.xlabel('log10($\omega$) rad/s')
plt.ylabel('dB')
plt.title('Magnitude')
plt.grid(True)

# Adjust x-axis limit
plt.xlim(0, np.log10(w[-1]))
plt.savefig('gain_plot.png')

plt.show()


