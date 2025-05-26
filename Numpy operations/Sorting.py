import numpy as np

# ----------------------------------------
# 1D ARRAY SORTING
# ----------------------------------------

# Create an unsorted 1D array
unsorted_1d_arr = np.array([3, 1, 5, 8, 3, 0, 1, 4, 5, 6, 12, 34, 67, 998])

# Sort the 1D array in ascending order (default behavior)
print("Sorted 1D Array (Ascending):", np.sort(unsorted_1d_arr))

# ----------------------------------------
# 2D ARRAY SORTING
# ----------------------------------------

# Create a 2D array
unsorted_2d_arr = np.array([[3, 1], [1, 2], [2, 3], [8, 5]])

# Column-wise sort (sorts each column independently)
# axis=0 means sorting down each column
print("Column-wise Sort (axis=0):\n", np.sort(unsorted_2d_arr, axis=0))

# Row-wise sort (sorts each row independently)
# axis=1 means sorting across each row
print("Row-wise Sort (axis=1):\n", np.sort(unsorted_2d_arr, axis=1))

# ----------------------------------------
# DESCENDING SORTING
# ----------------------------------------

# Reverse sort 1D array by slicing after sort
sorted_desc = np.sort(unsorted_1d_arr)[::-1]
print("1D Reverse Sorted Array:", sorted_desc)

# Reverse sort each row of a 2D array
# First sort row-wise ascending, then reverse each row using [:, ::-1]
sorted_rows_desc = np.sort(unsorted_2d_arr, axis=1)[:, ::-1]
print("Row-wise Reverse Sort:\n", sorted_rows_desc)

# Reverse sort each column of a 2D array
# First sort column-wise ascending, then reverse all rows using [::-1, :]
sorted_cols_desc = np.sort(unsorted_2d_arr, axis=0)[::-1, :]
print("Column-wise Reverse Sort:\n", sorted_cols_desc)

# ----------------------------------------
# BONUS: GET INDICES FOR SORTED ORDER
# ----------------------------------------

# Create a 1D array
arr_1d = np.array([10, 2, 8, 4, 6])

# Get indices that would sort the array in descending order
# np.argsort() gives indices for ascending order, then [::-1] reverses them
indices_desc = np.argsort(arr_1d)[::-1]
print("Descending order indices:", indices_desc)

# Use those indices to display the values in descending order
print("Sorted in descending order using indices:", arr_1d[indices_desc])

