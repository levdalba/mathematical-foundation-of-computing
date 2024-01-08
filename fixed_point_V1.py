import math


def fixed_point_iteration(g, x0, eps=1e-5, max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < eps:
            return x_new, i + 1
        if abs(x_new) > 1e100:
            return None, i + 1
        x = x_new
    return None, max_iter


def sqrt_function(x):
    return 0.5 * (x + 2 / x)


def modified_function(alpha):
    return lambda x: x**2 - 4 + alpha


print(fixed_point_iteration(sqrt_function, 0.5))
print(fixed_point_iteration(modified_function(0.5), 0.5))
print(fixed_point_iteration(modified_function(-0.0001), 0.5))
