import numpy as np

# Creating a 1D NumPy array
arr1d = np.array([2, 4, 6, 8, 9, 20, 10, 45])

# -------------------------
# Element-wise addition
# Adds 2 to each element in the array
print(arr1d + 2)  
# Output: [ 4  6  8 10 11 22 12 47 ]
# Meaning: Each element of arr1d is increased by 2

# -------------------------
# Element-wise subtraction
# Subtracts 2 from each element
print(arr1d - 2)  
# Output: [ 0  2  4  6  7 18  8 43 ]
# Meaning: Each element of arr1d is decreased by 2

# -------------------------
# Element-wise multiplication
# Multiplies each element by 2
print(arr1d * 2)  
# Output: [  4   8  12  16  18  40  20  90 ]
# Meaning: Each element is doubled

# -------------------------
# Element-wise division
# Divides each element by 2
print(arr1d / 2)  
# Output: [ 1.  2.  3.  4.  4.5 10.  5. 22.5 ]
# Meaning: Each element is halved
# Note: The result is in float even if input was integer.

# -------------------------
# Element-wise exponentiation
# Raises each element to the power of 2 (square)
print(arr1d ** 2)  
# Output: [  4  16  36  64  81 400 100 2025 ]
# Meaning: Each element is squared

# -------------------------
# Element-wise floor division
# Divides each element by 2 and rounds down to the nearest integer
print(arr1d // 2)  
# Output: [ 1  2  3  4  4 10  5 22 ]
# Meaning: Similar to normal division but result will be integer (floor value).

# -------------------------
# Element-wise modulus operation
# Returns the remainder after division by 2
print(arr1d % 2)  
# Output: [0 0 0 0 1 0 0 1 ]
# Meaning: 
#   - If the result is 0 → even number.
#   - If the result is 1 → odd number.
#   This operation helps in checking even/odd easily.
