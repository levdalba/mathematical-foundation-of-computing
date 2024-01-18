import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
from sklearn.linear_model import LinearRegression


def interpolate_slr(points):
    """Interpolate a polynomial using Simple Linear Regression."""
    x = np.array([point[0] for point in points]).reshape(-1, 1)
    y = np.array([point[1] for point in points])
    model = LinearRegression().fit(x, y)
    return [model.intercept_, model.coef_[0]]


def interpolate_lagrange(points):
    """Interpolate a polynomial using Lagrange's formula."""
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])
    poly = lagrange(x, y)
    return poly.coef


def interpolate_cubic_spline(points):
    """Interpolate a function using natural cubic spline."""
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])
    cs = CubicSpline(x, y, bc_type="natural")
    return cs


def evaluate_polynomial(coefs, x):
    """Evaluate a polynomial at x."""
    y = 0
    for i, coef in enumerate(reversed(coefs)):
        y += coef * x**i
    return y


def plot_interpolation(func, interpolate_func, num_points, interval):
    """Plot the given function, its interpolation, and the interpolation points."""
    # Generate the interpolation points
    x = np.linspace(*interval, num_points)
    y = func(x)
    points = list(zip(x, y))

    # Interpolate a function
    f_interpolated = interpolate_func(points)

    # Plot the function
    x_plot = np.linspace(*interval, 100)
    y_plot = func(x_plot)
    plt.figure()
    plt.plot(x_plot, y_plot, label="Function")

    # Plot the interpolation
    if isinstance(f_interpolated, CubicSpline):
        y_plot = f_interpolated(x_plot)
    else:
        y_plot = evaluate_polynomial(f_interpolated, x_plot)
    plt.plot(x_plot, y_plot, label="Interpolation")

    # Plot the points
    plt.scatter(x, y, color="red", label="Points")

    plt.legend()
    plt.grid(True)
    plt.show()


# Test the functions with various functions, interpolation methods, numbers of points, and intervals
functions = [
    np.sin,
    lambda x: np.sin(5 * x),
    lambda x: 1 / (1 + x**2),
    np.polynomial.Polynomial([-1, 1, -2, 1]).__call__,
]
interpolation_methods = [
    interpolate_slr,
    interpolate_lagrange,
    interpolate_cubic_spline,
]
num_points_values = [10, 20, 30]
interval_values = [(0, 1), (0, 2), (0, 3)]

for func in functions:
    for interpolate_func in interpolation_methods:
        for num_points in num_points_values:
            for interval in interval_values:
                plot_interpolation(func, interpolate_func, num_points, interval)
