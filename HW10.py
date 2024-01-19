def linear_interpolation(x, x_values, y_values):
    """
    Performs linear interpolation for a given set of points.

    Args:
        x (float): The x-coordinate for which to perform interpolation.
        x_values (list): List of x-coordinates of the known points.
        y_values (list): List of y-coordinates of the known points.

    Returns:
        float: The interpolated y-coordinate corresponding to the given x-coordinate.
    """
    if len(x_values) != len(y_values):
        raise ValueError(
            "The number of x-values must be equal to the number of y-values."
        )

    n = len(x_values)
    if n < 2:
        raise ValueError("At least two points are required for interpolation.")

    for i in range(n - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            # Perform linear interpolation
            slope = (y_values[i + 1] - y_values[i]) / (x_values[i + 1] - x_values[i])
            interpolated_y = y_values[i] + slope * (x - x_values[i])
            return interpolated_y

    raise ValueError("The given x-coordinate is outside the range of the known points.")
