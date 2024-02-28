import numpy as np
import matplotlib.pyplot as plt

# Load data from simulation.dat, skipping the header
n_convolution, y_convolution = np.loadtxt('convolution.dat', skiprows=1, unpack=True)

# Load data from analysis.dat
n_analysis, y_analysis = np.loadtxt('analysis.dat', unpack=True)

# Create stem plot
plt.figure(figsize=(10, 5))

# Plot convolution data in green with increased marker size
markerline, stemlines, baseline = plt.stem(n_convolution, y_convolution, linefmt='g-', markerfmt='bo', basefmt='r-', label='Convolution')
plt.setp(markerline, markersize=10)

# Plot analysis data in blue 
plt.stem(n_analysis, y_analysis, linefmt='b-', markerfmt='go', basefmt='r-', label='Analysis')

plt.title('Comparison of Stimulation and Analysis')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.show()

