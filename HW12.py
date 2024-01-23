import numpy as np


def f(x):
    return (x[0] - 2) ** 2 + x[1] ** 2 - 2 * x[0] + 3


def gradient_f(x):
    return np.array([2 * (x[0] - 2) - 2, 2 * x[1]])


def gradient_descent_2d(f, gradient_f, x0, learning_rate, num_iterations):
    x = x0
    for _ in range(num_iterations):
        x -= learning_rate * gradient_f(x)
    return x


x0 = np.array([0.0, 0.0])
learning_rate = 0.1
num_iterations = 1000

result = gradient_descent_2d(f, gradient_f, x0, learning_rate, num_iterations)
print(result)
