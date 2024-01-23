import numpy as np
import matplotlib.pyplot as plt


def multilateration(x_coords, y_coords, distances):
    # Create the matrix A
    matrix_A = np.array(
        [
            [2 * (x_coords[i] - x_coords[0]), 2 * (y_coords[i] - y_coords[0])]
            for i in range(1, len(x_coords))
        ]
    )

    # Create the vector B
    vector_B = [
        distances[0] ** 2
        - distances[i] ** 2
        - x_coords[0] ** 2
        - y_coords[0] ** 2
        + x_coords[i] ** 2
        + y_coords[i] ** 2
        for i in range(1, len(x_coords))
    ]

    # Calculate A_transpose * A and A_transpose * B
    A_transpose_A = np.dot(matrix_A.T, matrix_A)
    A_transpose_B = np.dot(matrix_A.T, vector_B)

    # Solve the linear system to find the estimated location
    estimated_location = np.linalg.solve(A_transpose_A, A_transpose_B)

    return estimated_location


# Load the data from the CSV file
data = np.genfromtxt("data1.csv", delimiter=",")
x_coords = data[:, 0]
y_coords = data[:, 1]
distances = data[:, 2]

# Calculate the estimated location
estimated_location = multilateration(x_coords, y_coords, distances)
print("Estimated Location:", estimated_location)

# Plot the data points and the estimated location
plt.scatter(x_coords, y_coords, label="Data Points")
plt.scatter(
    estimated_location[0],
    estimated_location[1],
    color="red",
    label="Estimated Location",
)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Estimated Location")
plt.legend()
plt.show()
