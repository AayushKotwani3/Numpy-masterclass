import numpy as np

# -----------------------------------------
# 1. Creating Different Types of NumPy Arrays

# Creating a 1D array with floating-point numbers
arr_1d = np.array([1.4, 2, 3.7])

# Creating a 2D array (matrix with rows and columns)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Creating a 3D array (array of matrices)
arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]])

# -----------------------------------------
# 2. shape ➔ Find the dimensions of the array
# shape returns a tuple (rows, columns) for 2D arrays
print("Shape of arr_2d:", arr_2d.shape)
# Output: (2, 3) ➔ 2 rows and 3 columns

# In 3D, shape shows (number of matrices, rows, columns)

# -----------------------------------------
# 3. size ➔ Find the total number of elements
# size returns the total number of elements across all dimensions
print("Size of arr_3d:", arr_3d.size)
# Output: 9 ➔ There are 9 elements inside arr_3d

# -----------------------------------------
# 4. dtype ➔ Find the data type of array elements
# dtype shows the type of data stored (e.g., int32, float64, etc.)
print("Data type of arr_1d:", arr_1d.dtype)
# Output: float64 ➔ The elements are floating-point numbers

# -----------------------------------------
# 5. astype ➔ Convert array elements to a different type
# astype creates a **copy** of the array with a new data type

# Converting arr_1d from float to int (decimal parts will be truncated)
int_arr_1d = arr_1d.astype(int)
print("Array after converting to integers:", int_arr_1d)
# Output: [1 2 3] ➔ Decimal part removed

print("Data type after conversion:", int_arr_1d.dtype)
# Output: int64 ➔ Now the array holds integers

# Note: astype() does NOT modify the original array. It returns a new array.

# -----------------------------------------
# 6. ndim ➔ Find the number of dimensions (axes)
# ndim gives how many dimensions (levels) the array has

print("Number of dimensions in arr_1d:", arr_1d.ndim)
# Output: 1 ➔ arr_1d is a 1D array (single list)

print("Number of dimensions in arr_2d:", arr_2d.ndim)
# Output: 2 ➔ arr_2d is a 2D array (matrix)

print("Number of dimensions in arr_3d:", arr_3d.ndim)
# Output: 3 ➔ arr_3d is a 3D array (array of matrices)

# -----------------------------------------
