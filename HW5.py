import numpy as np


def gaussian_elimination(A, b):
    n = len(A)
    M = np.hstack([A, b.reshape(-1, 1)])  # Combine A and b into an augmented matrix

    for k in range(n):
        # Pivot for maximum absolute value
        max_row = max(range(k, n), key=lambda i: abs(M[i][k]))
        M[[k, max_row]] = M[[max_row, k]]  # Swap rows

        # Zero out below pivot
        for i in range(k + 1, n):
            M[i] -= M[k] * M[i, k] / M[k, k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, :-1], x)) / M[i, i]

    return x


def generate_hilbert_matrix(n):
    """Generate a Hilbert matrix of size n x n."""
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H


def generate_test_vector(A, x_test):
    """Generate a vector b of size n so the solution of Ax=b will be x_test."""
    return np.dot(A, x_test)


# Generate a random 5x5 matrix A
np.random.seed(0)  # for reproducibility
A = np.random.rand(50, 50)

# Generate a Hilbert vector b suitable for A
b = generate_test_vector(A, np.ones(A.shape[0]))

# Solve the system of equations
x = gaussian_elimination(A, b)
print("Solution vector x:", x)

# Calculate the residual vector
residual = b - np.dot(A, x)
print("Residual vector:", residual)

# Check if the solution is good or bad
is_bad = False
for i in range(len(A)):
    if np.dot(A[i], x) != b[i]:
        is_bad = True
        break
if is_bad:
    print("Bad solution")
else:
    print("Good solution")

# Define the real solution
real_solution = np.array([1, 2, 3, 4, 5])  # Adjust this to match the length of x

# Calculate the distance to the real solution
distance = np.linalg.norm(x - real_solution)
print("Distance to the real solution:", distance)


print("Matrix A:\n", A)
print("Vector b:\n", b)
