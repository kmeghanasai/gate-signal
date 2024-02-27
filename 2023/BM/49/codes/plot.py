import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Values.txt')
data2 = np.loadtxt('Differentiation.txt')
x_values = data[:,0]
xd_values = data2[:,0]

y_values = data[:,1]
yd_values = data2[:,1]

y_calcu = data[:,2]
def plotting(x_values,y_values,name, ylabel, y_calcu = []):
	plt.plot(x_values, y_values, label='y(t) v/s t')
	if len(y_calcu) == len(x_values):
		plt.scatter(x_values, y_calcu, marker = 'X',s=100, color = 'red', label = r'Simulation')
	plt.xlabel('t')
	plt.ylabel(ylabel)
	plt.grid(True)
	plt.savefig(name)

plotting(x_values, y_values,'y(t)_vs_t.png', 'y(t)', y_calcu)
plt.clf()
plotting(xd_values, yd_values,'dy_dt_vs_t.png','dy(t)/dt',[])
