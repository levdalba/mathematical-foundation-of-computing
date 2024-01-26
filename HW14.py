import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.0
beta = 0.1
delta = 0.075
gamma = 1.5

# Initial conditions
x0 = 10  # initial prey population
y0 = 9  # initial predator population

# Time step (dt) and number of steps
dt = 0.01
num_steps = 1000

# Arrays to store x and y values
x = np.zeros(num_steps + 1)
y = np.zeros(num_steps + 1)
x[0] = x0
y[0] = y0

# Euler method
for i in range(num_steps):
    dx = (alpha * x[i] - beta * x[i] * y[i]) * dt
    dy = (delta * x[i] * y[i] - gamma * y[i]) * dt
    x[i + 1] = x[i] + dx
    y[i + 1] = y[i] + dy

# Plot the populations over time
plt.plot(x, label="Prey population")
plt.plot(y, label="Predator population")
plt.legend()
plt.show()
