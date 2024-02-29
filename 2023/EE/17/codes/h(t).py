import numpy as np
import matplotlib.pyplot as plt
import math

def h(t):
    return 2*(np.exp(-3*t))

t = np.linspace(0,10,100)

plt.plot(t,h(t),label='h(t)')

plt.xlabel('t')
plt.ylabel('h(t)')
plt.xticks(np.arange(0,10,1))
#plt.title('Plot of h(t)')

plt.legend(loc='upper right')
plt.show()
