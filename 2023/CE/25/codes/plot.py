import numpy as np
import matplotlib.pyplot as plt

# Load data with tab delimiter
data = np.genfromtxt("data.dat", delimiter='\t')

plt.plot(data[:, 0], data[:, 1], label="$f(x)=px^4+qx^5$")
plt.plot(data[:, 0], data[:, 2], label="Fourier Series approximation")
plt.grid(True)
plt.legend()
plt.savefig('../figs/Figure_1.png')
