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


def generate_diagonally_dominant_matrix(n):
    """Generate a diagonally dominant matrix of size n x n."""
    A = np.random.rand(n, n)
    D = np.diag(np.abs(A))  # Diagonal elements of A
    S = (
        np.sum(np.abs(A), axis=1) - D
    )  # Sum of absolute values of non-diagonal elements in each row
    return A + np.diagflat(S - D + 1)  # Make the matrix diagonally dominant


def jacobi_method(A, b, max_iterations=1000):
    """Solve the system of linear equations Ax = b using the Jacobi iterative method."""
    x = np.zeros_like(b)
    for _ in range(max_iterations):
        x_new = (b - (A @ x - np.diag(np.diag(A)) * x)) / np.diag(A)
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new
    return x


def plot_time(dimensions, times_gauss, times_jacobi):
    plt.figure(figsize=(10, 6))
    plt.plot(dimensions, times_gauss, label="Gaussian elimination")
    plt.plot(dimensions, times_jacobi, label="Jacobi method")
    plt.xlabel("Dimension")
    plt.ylabel("Time (s)")
    plt.title("Running time of Gaussian elimination vs. Jacobi method")
    plt.legend()
    plt.grid(True)
    plt.show()


dimensions = range(150, 201)
times_gauss = []
times_jacobi = []

for n in dimensions:
    A = generate_diagonally_dominant_matrix(n)
    b = generate_test_vector(A, np.ones(n))

    start = time.time()
    gaussian_elimination(A, b)
    times_gauss.append(time.time() - start)

    start = time.time()
    jacobi_method(A, b)
    times_jacobi.append(time.time() - start)

plot_time(dimensions, times_gauss, times_jacobi)
