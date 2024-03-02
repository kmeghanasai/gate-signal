import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('Vy_data.txt')
t = data[:, 0]
Vy = data[:, 1]

plt.figure(figsize=(12, 6))
plt.plot(t, Vy, label='Vy = 4.6 * sin(wt + 90)')
plt.xlabel('Time (radians)')
plt.ylabel('Voltage')
plt.legend()
plt.grid(True)
plt.savefig("V_y.png")
plt.show()

