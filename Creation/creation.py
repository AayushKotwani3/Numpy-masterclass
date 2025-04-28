import numpy as np

# ------------------------------------------
# 1. Creating a One-Dimensional Array
one_d_array = np.array([1, 2, 3, 4])
# print(one_d_array)

# ------------------------------------------
# 2. Creating a Two-Dimensional Array (Matrix)
two_d_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]])
# print(two_d_array)

# ------------------------------------------
# 3. Creating a One-Dimensional Array Filled with Zeros
zero_array_1d = np.zeros(3)   # 3 elements, all zeros
# print(zero_array_1d)

# ------------------------------------------
# 4. Creating a Two-Dimensional Array Filled with Zeros
zero_array_2d = np.zeros((3, 4))   # Shape = 3 rows × 4 columns
# print(zero_array_2d)

# ------------------------------------------
# 5. Creating a Two-Dimensional Array Filled with Ones
ones_array = np.ones((2, 3))    # Shape = 2 rows × 3 columns
# print(ones_array)

# ------------------------------------------
# 6. Creating a Two-Dimensional Array Filled with a Specific Value
filled_array = np.full((2, 3), 5)   # Shape = 2x3, filled with 5
# print(filled_array)

# ------------------------------------------
# 7. Creating a Sequence of Numbers
# Using arange(start, stop, step)
sequence_array = np.arange(1, 11, 2)   # From 1 to 10 (exclusive 11), step by 2
# print(sequence_array)

# ------------------------------------------
# 8. Creating an Identity Matrix
# Identity matrix = square matrix with 1s on the diagonal and 0s elsewhere
identity_matrix = np.eye(5)   # 5x5 Identity matrix
print(identity_matrix)
