import numpy as np
import matplotlib.pyplot as plt
Y_in = []
C_values= []
with open("y_data.txt", "r") as file:
    for line in file:
        Y_in_real, C_value = map(float, line.split())
        Y_in.append(Y_in_real)
        C_values.append(C_value)
plt.plot( C_values,Y_in)
plt.xlabel('Capacitance(C)')
plt.ylabel('magnitude of Y_in')
plt.grid(True)
plt.legend()
plt.savefig('figs/fig2.png')
plt.show()

