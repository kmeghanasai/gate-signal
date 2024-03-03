import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('Vx_data.txt')
t = data[:, 0]
Vx = data[:, 1]

plt.figure(figsize=(12, 6))
plt.plot(t, Vx, label='Vx = 2^(3/2) * sin(wt - 45)')
plt.xlabel('Time (radians)')
plt.ylabel('Voltage')
plt.legend()
plt.grid(True)
plt.savefig("V_x.png")
plt.show()

