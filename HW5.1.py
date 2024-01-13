import numpy as np
import matplotlib.pyplot as plt
import time


def generate_test_vector(A, x_test):
    """Generate a vector b of size n so the solution of Ax=b will be x_test."""
    return np.dot(A, x_test)


def gaussian_elimination(A, b):
    """Solve the system of linear equations Ax = b using Gaussian elimination."""
    n = len(A)
    M = np.hstack([A, b.reshape(-1, 1)])  # Combine A and b into an augmented matrix

    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i + 1 : n], x[i + 1 : n])) / M[i, i]

    return x


def generate_hilbert_matrix(n):
    """Generate a Hilbert matrix of size n x n."""
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H


def plot_errors(dimensions, errors_gauss, errors_numpy, title):
    plt.figure(figsize=(10, 6))
    plt.plot(dimensions, errors_gauss, label="Gaussian elimination")
    plt.plot(dimensions, errors_numpy, label="numpy.linalg.solve")
    plt.xlabel("Dimension")
    plt.ylabel("Error")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_time(dimensions, times):
    plt.figure(figsize=(10, 6))
    plt.plot(dimensions, times)
    plt.xlabel("Dimension")
    plt.ylabel("Time (s)")
    plt.title("Running time of Gaussian elimination")
    plt.grid(True)
    plt.show()


dimensions = range(2, 101)
errors_gauss_rand = []
errors_gauss_hilbert = []
errors_numpy_rand = []
errors_numpy_hilbert = []
times = []

for n in dimensions:
    # Random matrix
    A_rand = np.random.rand(n, n)
    b_rand = generate_test_vector(A_rand, np.ones(n))
    start = time.time()
    x_gauss_rand = gaussian_elimination(A_rand, b_rand)
    times.append(time.time() - start)
    x_numpy_rand = np.linalg.solve(A_rand, b_rand)
    errors_gauss_rand.append(np.linalg.norm(x_gauss_rand - np.ones(n)))
    errors_numpy_rand.append(np.linalg.norm(x_numpy_rand - np.ones(n)))

    # Hilbert matrix
    A_hilbert = generate_hilbert_matrix(n)
    b_hilbert = generate_test_vector(A_hilbert, np.ones(n))
    x_gauss_hilbert = gaussian_elimination(A_hilbert, b_hilbert)
    x_numpy_hilbert = np.linalg.solve(A_hilbert, b_hilbert)
    errors_gauss_hilbert.append(np.linalg.norm(x_gauss_hilbert - np.ones(n)))
    errors_numpy_hilbert.append(np.linalg.norm(x_numpy_hilbert - np.ones(n)))

plot_errors(
    dimensions, errors_gauss_rand, errors_numpy_rand, "Error growth for random matrix"
)
plot_errors(
    dimensions,
    errors_gauss_hilbert,
    errors_numpy_hilbert,
    "Error growth for Hilbert matrix",
)
plot_time(dimensions, times)
