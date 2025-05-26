import numpy as np

# Creating a 1D NumPy array
arr_1d = np.array([1.4, 2, 3.7, 4, 5, 6])

# Creating a 2D NumPy array (3x3 matrix)
arr_2d = np.array([[1, 2, 30],
                   [4, 50, 6],
                   [70, 8, 9]])

# ----------------------------------------
# INDEXING
# ----------------------------------------
# Indexing in NumPy:
# For 1D arrays: arr[index]
# For 2D arrays: arr[row, column]

# Example:
# print(arr_1d[2])    # Access 3rd element (3.7)
# print(arr_2d[1,2])  # Access value at 2nd row, 3rd column (6)


# ----------------------------------------
# SLICING
# ----------------------------------------
# General form: arr[start:stop:step]
# Note: 'stop' index is excluded

first = arr_1d[1:4]     # Slicing from index 1 to 3 (i.e., 2, 3.7, 4)
second = arr_1d[:4]     # From start to index 3 (i.e., 1.4 to 4)
third = arr_1d[::2]     # Every second element (step size 2)
fourth = arr_1d[::-1]   # Reversing the array using negative step

print("First slice:", first)
print("Second slice:", second)
print("Third slice:", third)
print("Reversed array:", fourth)


# ----------------------------------------
# 2D ARRAY INDEXING AND SLICING
# ----------------------------------------

# Accessing a specific row in a 2D array
# Example: Second row (index 1)
print('Second row:', arr_2d[1])

# Accessing a specific column in a 2D array
# Example: Third column (index 2)
print('Third column:', arr_2d[:, 2])

# Extracting a sub-array using slicing
# Syntax: arr[row_start:row_end, col_start:col_end]
# Example: Extracts rows 0–2 and columns 1–2 (excluding row 3 and column 3)
sub_array = arr_2d[0:3, 1:3]
print("2D Sliced Sub-array:\n", sub_array)


# ----------------------------------------
# FANCY INDEXING
# ----------------------------------------
# Select multiple specific elements by index
print("Fancy indexing on 1D:", arr_1d[[0, 2, 4]])  # Fetch elements at index 0, 2, and 4


# ----------------------------------------
# BOOLEAN MASKING
# ----------------------------------------
# Select values based on condition (returns a new array with elements that satisfy the condition)
print("Boolean masking on 2D:", arr_2d[arr_2d > 25])  # All elements > 25
