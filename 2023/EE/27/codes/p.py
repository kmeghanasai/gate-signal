import numpy as np
import matplotlib.pyplot as plt

#n_values_discrete = np.arange(-5,11)

data1_file = 'data31.txt'
data = np.loadtxt(data1_file)

n_values = data[:, 0]
y_values = data[:, 1]

plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo')
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid(True)
plt.savefig('p.jpeg')
plt.show()

data2_file = 'data32.txt'
data = np.loadtxt(data2_file)

n_values = data[:, 0]
y_values = data[:, 1]

plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo')
plt.xlabel("n")
plt.ylabel("y(n)")
plt.grid(True)
plt.savefig('p1.jpeg')
plt.show()

data3_file = 'data33.txt'
data = np.loadtxt(data3_file)

n_values = data[:, 0]
y_values = data[:, 1]

plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo')
plt.xlabel("n")
plt.ylabel("g(n)")
plt.grid(True)
plt.savefig('p2.jpeg')
plt.show()

