# import numpy as np


# def gaussian_elimination(A, b):
#     n = len(b)
#     AugmentedMatrix = np.hstack((A, b.reshape(-1, 1)))

#     for col in range(n):
#         print("Step", col + 1)
#         print(AugmentedMatrix)

#         # Check if the leading position is zero
#         if AugmentedMatrix[col, col] == 0:
#             print("Zero found on the leading position at step", col + 1)
#             continue

#         # Make the diagonal contain all 1's
#         AugmentedMatrix[col] = AugmentedMatrix[col] / AugmentedMatrix[col, col]

#         # Make the elements below the diagonal contain all 0's
#         for row in range(col + 1, n):
#             multiplier = -AugmentedMatrix[row, col]
#             AugmentedMatrix[row] += multiplier * AugmentedMatrix[col]

#     # Back substitution
#     x = np.zeros(n)
#     for i in range(n - 1, -1, -1):
#         x[i] = (
#             AugmentedMatrix[i, -1]
#             - sum(AugmentedMatrix[i, j] * x[j] for j in range(i + 1, n))
#         ) / AugmentedMatrix[i, i]

#     return x


# # Test with given input
# A = np.array([[1, 1, 1], [2, 2, 1], [3, 2, 1]], dtype=float)
# b = np.array([3, 5, 6], dtype=float)

# solution_vector_x = gaussian_elimination(A, b)
# print("Solution Vector x:", solution_vector_x)
# import numpy as np


# def gaussian_elimination(A, b):
#     n = len(A)
#     M = A

#     i = 0
#     for x in M:
#         x.append(b[i])
#         i += 1

#     for k in range(n):
#         for i in range(k, n):
#             if abs(M[i][k]) > abs(M[k][k]):
#                 M[k], M[i] = M[i], M[k]
#             else:
#                 pass

#         for j in range(k + 1, n):
#             q = float(M[j][k]) / M[k][k]
#             for m in range(k, n + 1):
#                 M[j][m] -= q * M[k][m]

#     x = [0 for i in range(n)]

#     x[n - 1] = float(M[n - 1][n]) / M[n - 1][n - 1]
#     for i in range(n - 1, -1, -1):
#         z = 0
#         for j in range(i + 1, n):
#             z = z + float(M[i][j]) * x[j]
#         x[i] = float(M[i][n] - z) / M[i][i]
#     return x


# # Generate a random 100x100 matrix
# A = np.random.rand(100, 100).tolist()

# # Generate a random 100-element vector
# b = np.random.rand(100).tolist()

# # Test the function
# x = gaussian_elimination(A, b)

# # Print the first 10 elements of the result
# print(x[:10])
