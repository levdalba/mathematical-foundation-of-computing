import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 - 4


def df(x):
    return 2 * x


def newton(x0, eps=1e-9, max_iter=100):
    x_values = [x0]
    errors = [0]

    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        error = abs(x_new - x)
        x_values.append(x_new)
        errors.append(error)
        if error < eps:
            break
        x = x_new
    return x_values, errors, i + 1


def bisection(a, b, eps=1e-9, max_iter=100):
    x_values = [(a + b) / 2]
    errors = [0]

    for i in range(max_iter):
        c = (a + b) / 2
        error = abs(b - a)
        x_values.append(c)
        errors.append(error)
        if error < eps:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return x_values, errors, i + 1


def combined_method(x0, a, b, eps=1e-9, max_iter=100, threshold=1.0):
    x_values = [x0]
    errors = [0]

    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)  # Use Newton's method

        if abs(x_new - x) > threshold:  # If there's a radical change
            c = (a + b) / 2  # Use Bisection method
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            x_new = c

        error = abs(x_new - x)
        x_values.append(x_new)
        errors.append(error)
        if error < eps:
            break
        x = x_new
    return x_values, errors, i + 1


def plot_convergence_graph(errors, methods):
    plt.figure(figsize=(10, 5))

    for error, method in zip(errors, methods):
        plt.plot(error, "-o", label=f"{method} errors")
    plt.title("Convergence of errors")
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.legend()

    plt.tight_layout()
    plt.show()


x0 = float(input("Enter initial point: "))
a, b = 0, 10

x_values_newton, errors_newton, iterations_newton = newton(x0)
x_values_bisection, errors_bisection, iterations_bisection = bisection(a, b)
x_values_combined, errors_combined, iterations_combined = combined_method(x0, a, b)

print(f"Newton Root = {x_values_newton[-1]} in {iterations_newton} iterations")
print(f"Bisection Root = {x_values_bisection[-1]} in {iterations_bisection} iterations")
print(f"Combined Root = {x_values_combined[-1]} in {iterations_combined} iterations")

errors_all = [errors_newton, errors_bisection, errors_combined]
methods = ["Newton", "Bisection", "Combined"]

plot_convergence_graph(errors_all, methods)
