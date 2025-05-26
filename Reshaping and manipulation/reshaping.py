import numpy as np

# ----------------------------
# Reshaping Arrays
# ----------------------------
# The reshape() method is used to change the shape of an array without changing its data.
# It returns a view of the original array, not a copy (if possible).
# Syntax: reshape(new_rows, new_columns)

arr = np.array([1, 2, 3, 4, 5, 6])  # A 1D array with 6 elements
reshaped_arr = arr.reshape(2, 3)    # Reshape into 2 rows and 3 columns
print("Reshaped Array (2x3):")
print(reshaped_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]

# ----------------------------
# Flattening Arrays
# ----------------------------
# To convert a multidimensional array to 1D, we can use:
# 1. flatten() – returns a new copy of the array, flattened into 1D
# 2. ravel() – returns a flattened view (no copy if possible)

arr_2d = np.array([[2, 3, 4], [5, 6, 7]])

print("\nFlattened using ravel():")
print(arr_2d.ravel())
# Output: [2 3 4 5 6 7]

print("\nFlattened using flatten():")
print(arr_2d.flatten())
# Output: [2 3 4 5 6 7]

# Note:
# Use ravel() when you want performance (and don't need a copy).
# Use flatten() when you need an independent copy of the data.

# ----------------------------------------
# ARRAY COMPATIBILITY CHECK
# ----------------------------------------

# Define three arrays
a = np.array([1, 2, 3])         # Shape: (3,)
b = np.array([4, 5, 6, 0])      # Shape: (4,)
c = np.array([7, 8, 9])         # Shape: (3,)

# Compare shapes of arrays to check compatibility (e.g., for element-wise operations)
print('Compatibility between a and b:', a.shape == b.shape)  # False: shape (3,) != (4,)
print('Compatibility between a and c:', a.shape == c.shape)  # True: both have shape (3,)
