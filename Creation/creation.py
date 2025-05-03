import numpy as np

# -----------------------------------------------------
# 1. Creating a One-Dimensional Array
one_d_array = np.array([1, 2, 3, 4])
# print(one_d_array)

# -----------------------------------------------------
# 2. Creating a Two-Dimensional Array (Matrix)
two_d_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]])
# print(two_d_array)

# -----------------------------------------------------
# 3. One-Dimensional Array Filled with Zeros
zero_array_1d = np.zeros(3)  # Creates a 1D array of 3 elements, all set to 0
# print(zero_array_1d)

# -----------------------------------------------------
# 4. Two-Dimensional Array Filled with Zeros
zero_array_2d = np.zeros((3, 4))  # 3 rows × 4 columns of zeros
# print(zero_array_2d)

# -----------------------------------------------------
# 5. Two-Dimensional Array Filled with Ones
ones_array = np.ones((2, 3))  # 2 rows × 3 columns filled with 1s
# print(ones_array)

# -----------------------------------------------------
# 6. Two-Dimensional Array Filled with a Specific Value
filled_array = np.full((2, 3), 5)  # 2×3 matrix filled with 5s
# print(filled_array)

# -----------------------------------------------------
# 7. Sequence of Numbers Using arange()
sequence_array = np.arange(1, 11, 2)  # From 1 to 10 (excluding 11), step size 2
# print(sequence_array)

# -----------------------------------------------------
# 8. Identity Matrix (square matrix with 1s on diagonal)
identity_matrix = np.eye(5)  # 5x5 identity matrix
print(identity_matrix)

# -----------------------------------------------------
# 9. Creating a 3D Array with np.ones()
# Shape (4, 3, 4) = 4 blocks, each with 3 rows and 4 columns
arr_3d = np.ones((4, 3, 4))
# print(arr_3d)

# -----------------------------------------------------
# 10. Creating a 4D Array with np.ones()
# Shape (2, 3, 4, 5):
# 2 blocks → each has 3 sub-blocks → each has 4 rows → each row has 5 elements
arr_4d = np.ones((2, 3, 4, 5))
# print(arr_4d)

# -----------------------------------------------------
# 11. Creating Arrays with Random Module

'''
np.random.rand(shape): Random floats in range [0.0, 1.0)
np.random.random(shape): Similar to rand(), returns random floats in [0.0, 1.0)
np.random.randint(low, high, size): Random integers from low (inclusive) to high (exclusive)
np.random.choice(list, size): Random samples picked from the provided list
np.random.seed(value): Sets the seed for reproducibility (same output each run)
'''

# Random floats between 0 and 1 with shape (2, 3)
print(np.random.rand(2, 3))

# Random floats between 0 and 1 with shape (3, 2)
print(np.random.random((3, 2)))

# Random integers from 1 to 9 (7 values in 1D array)
print(np.random.randint(1, 10, size=7))

# Random integers from 1 to 9 in a 3×4 array
print(np.random.randint(1, 10, (3, 4)))

# Picking 5 random values from the list [10, 20, 30, 40]
print(np.random.choice([10, 20, 30, 40], size=5))

# Setting seed ensures consistent random values every run (important for reproducibility)
np.random.seed(37)
print(np.random.randint(1, 100, 5))
