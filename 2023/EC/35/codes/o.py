import matplotlib.pyplot as plt

# Read data from file
with open("output_data.txt", "r") as file:
    lines = file.readlines()
    data = [line.split() for line in lines[1:]]  # Skip the header line and split each line into a list

# Extract t and y(t) values
t_values = [float(row[0]) for row in data]
y_values = [float(row[1]) for row in data]

# Plot
plt.plot(t_values, y_values, 'b-')  # 'b-' is for a blue continuous line
plt.title('Continuous Plot of y(t) vs. t')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.savefig('fig.png')
plt.show()

