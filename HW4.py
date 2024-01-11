import numpy as np


def gaussian_elimination(A, b):
    n = len(b)
    AugmentedMatrix = np.hstack((A, b.reshape(-1, 1)))

    for col in range(n):
        print("Step", col + 1)
        print(AugmentedMatrix)

        # Check if the leading position is zero
        if AugmentedMatrix[col, col] == 0:
            print("Zero found on the leading position at step", col + 1)
            continue

        # Make the diagonal contain all 1's
        AugmentedMatrix[col] = AugmentedMatrix[col] / AugmentedMatrix[col, col]

        # Make the elements below the diagonal contain all 0's
        for row in range(col + 1, n):
            multiplier = -AugmentedMatrix[row, col]
            AugmentedMatrix[row] += multiplier * AugmentedMatrix[col]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (
            AugmentedMatrix[i, -1]
            - sum(AugmentedMatrix[i, j] * x[j] for j in range(i + 1, n))
        ) / AugmentedMatrix[i, i]

    return x


# Test with given input
A = np.array([[1, 1, 1], [2, 2, 1], [3, 2, 1]], dtype=float)
b = np.array([3, 5, 6], dtype=float)

solution_vector_x = gaussian_elimination(A, b)
print("Solution Vector x:", solution_vector_x)
