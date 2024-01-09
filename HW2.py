import numpy as np


def f(x):
    return (x - 3) * (x - 1) ** 2


def f_prime(x):
    return 3 * (x - 1) ** 2 - 2 * (x - 3) * (x - 1)


def newton_step(x):
    return x - f(x) / f_prime(x)


def hybrid_solver(a, b, epsilon=0.0001):
    iterations = 0
    x_n = (a + b) / 2

    while abs(newton_step(x_n) - x_n) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations

        x_n = newton_step(x_n)
        if a < x_n < b:
            a, b = x_n, c
        else:
            a, b = (a + b) / 2, c

        iterations += 1

    return x_n, iterations


print(hybrid_solver(1, 3))
print(hybrid_solver(-1, -3))
print(hybrid_solver(0, -2))
