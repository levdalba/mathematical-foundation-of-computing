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


# Define A and b
A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
b = np.array([1, 2, 3], dtype=float)

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
