import numpy as np
import matplotlib.pyplot as plt


def interpolate(points):
    """Interpolate a polynomial that passes through the given points."""
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])
    n = len(points)
    A = np.vander(x, n)  # Vandermonde matrix
    c = np.linalg.solve(A, y)  # Solve Ac = y for c
    return c[::-1]  # Reverse c to get the coefficients in descending order of powers


def evaluate_polynomial(c, x):
    """Evaluate the polynomial with coefficients c at the point x."""
    return np.polyval(c, x)


def plot_polynomial(c, points):
    """Plot the polynomial with coefficients c and the given points."""
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])
    x_plot = np.linspace(min(x), max(x), 100)
    y_plot = evaluate_polynomial(c, x_plot)
    plt.figure()
    plt.plot(x_plot, y_plot, label="Interpolating polynomial")
    plt.scatter(x, y, color="red", label="Points")
    plt.legend()
    plt.grid(True)
    plt.show()


# Test the functions
points = [(0, 1), (1, 0), (2, 1)]
c = interpolate(points)
print("Coefficients:", c)
print("Polynomial value at x = 3:", evaluate_polynomial(c, 3))
plot_polynomial(c, points)
