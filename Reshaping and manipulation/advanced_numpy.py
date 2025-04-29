import numpy as np

# -----------------------------------
# Inserting Values into Arrays
# -----------------------------------
# Syntax: np.insert(array, index, value, axis=None)
# axis=None: Inserts into flattened array (default)
# axis=0: Inserts a row in a 2D array
# axis=1: Inserts a column in a 2D array

arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.insert(arr, 2, 100)  # Insert 100 at index 2
print("After inserting into 1D array:")
print(new_arr)

# Insert in 2D arrays
arr_2d = np.array([[2, 3, 4], [5, 6, 7]])

newarr_flat = np.insert(arr_2d, 1, [8, 6, 0])        # Flattens before insert
newarr_row = np.insert(arr_2d, 1, [8, 6, 0], axis=0) # Insert row at index 1
newarr_col = np.insert(arr_2d, 0, [8, 6], axis=1)    # Insert column at index 0

print("\nOriginal 2D Array:")
print(arr_2d)

print("\nInserted without axis (flattened):")
print(newarr_flat)

print("\nInserted row at index 1:")
print(newarr_row)

print("\nInserted column at index 0:")
print(newarr_col)


# -----------------------------------
# Appending Arrays
# -----------------------------------
# np.append() adds values to the end of an array
arr2 = np.array([10, 20, 30, 40, 50, 60])
new_array = np.append(arr, arr2)
print("\nAppended array:")
print(new_array)


# -----------------------------------
# Concatenating Arrays
# -----------------------------------
# np.concatenate((array1, array2), axis)
arrb = np.concatenate((arr, arr2, [50, 60, 70]), axis=0)
print("\nConcatenated array:")
print(arrb)


# -----------------------------------
# Deleting Elements
# -----------------------------------
# np.delete(array, index, axis)
arrd = np.delete(arr, 0)  # Delete element at index 0 from 1D array
print("\n1D array after deletion:")
print(arrd)

# For 2D arrays
arrd2 = np.delete(arr_2d, 1, axis=1)  # Delete column at index 1
print("\n2D array after deleting column 1:")
print(arrd2)


# -----------------------------------
# Stacking Arrays
# -----------------------------------
# Vertical stacking (row-wise)
print("\nVertically stacked arrays:")
print(np.vstack((arr, arr2)))

# Horizontal stacking (column-wise)
print("\nHorizontally stacked arrays:")
print(np.hstack((arr, arr2)))


# -----------------------------------
# Splitting Arrays
# -----------------------------------
# np.hsplit(array, num_parts): splits horizontally (1D or 2D)
# np.vsplit(array, num_parts): splits vertically (2D only)

print("\nHorizontally split 1D array into 2 parts:")
print(np.hsplit(arr, 2))  # 1D array split into 2 equal parts

print("\nVertically split 2D array into 2 parts:")
print(np.vsplit(arr_2d, 2))  # 2D array split into 2 row blocks
