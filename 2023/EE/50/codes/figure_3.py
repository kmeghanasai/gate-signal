import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a file
def read_data(filename):
    data = np.loadtxt(filename, skiprows=1)
    k = data[:, 0]
    real = data[:, 1]
    imag = data[:, 2]
    magnitude = data[:, 3]
    return k, real, imag, magnitude

# Read data from files
k1, real1, imag1, magnitude1 = read_data('data3.txt')
k2, real2, imag2, magnitude2 = read_data('data4.txt')

# Plot data
plt.figure(figsize=(10, 5))

# Plot data from data3.txt as stem plot
plt.stem(k1, magnitude1, linefmt='b-', markerfmt='bo', basefmt=' ', label='Magnitude (data3.txt)')
plt.plot(k1[3], magnitude1[3], 'ro', markersize=10)  # Highlight fourth term with a red circle

# Plot data from data4.txt as scatter plot
plt.scatter(k2, magnitude2, color='g', label='Magnitude (data4.txt)')
plt.plot(k2[3], magnitude2[3], 'rx', markersize=10)  # Highlight fourth term with a red cross

# Plot red crosses where both graphs coincide
for i in range(len(k1)):
    if k1[i] in k2 and magnitude1[i] in magnitude2:
        plt.plot(k1[i], magnitude1[i], 'rx', markersize=10)  # Red cross for coincidence

plt.xlabel('k')
plt.ylabel('Magnitude')
plt.title('Combined Plot')
plt.grid(True)

plt.tight_layout()
plt.show()
