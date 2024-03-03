import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('Vo_data.txt')
t = data[:, 0]
Vo = data[:, 1]

plt.figure(figsize=(12, 6))
plt.plot(t, Vo, label='Vo = 4.6 - 4.6*2^(0.5) * cos(2wt)')
plt.xlabel('Time (radians)')
plt.ylabel('Voltage')
plt.legend()
plt.grid(True)
plt.savefig("V_o.png")
plt.show

