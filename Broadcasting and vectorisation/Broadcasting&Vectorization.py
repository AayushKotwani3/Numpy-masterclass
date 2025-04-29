import numpy as np

'''
🔁 Broadcasting in NumPy
Broadcasting allows NumPy to perform operations between arrays of different shapes during arithmetic operations. 
It "stretches" the smaller array across the larger one so they have compatible shapes.
'''

# 🎯 Example 1: Subtracting a scalar from each element of a 1D array
arr = np.array([10, 13, 45, 79, 90])
discount = 10  # 10% discount
# Apply the discount using broadcasting
discounted_arr = arr - (arr * (discount / 100))
print("Discounted Array:", discounted_arr)

# Output: [ 9.  11.7  40.5  71.1  81. ] — each element is reduced by 10%

# 🎯 Example 2: Broadcasting with 2D array and scalar
arr_2d = np.array([[2, 3, 4, 8, 10], 
                   [5, 6, 7, 12, 4]])

# Add 10 to every element
print("2D Array + 10:\n", arr_2d + 10)

# Output:
# [[12 13 14 18 20]
#  [15 16 17 22 14]]

# 🎯 Example 3: Broadcasting between two arrays of same shape
# Adding a 1D array to each row of the 2D array
print("2D Array + 1D Array:\n", arr_2d + arr)

# Output:
# [[12 16 49 87 100]
#  [15 19 52 91 94]]

# ⚠️ Example 4: Broadcasting error
# Attempting to add an incompatible shape [2,3] to a shape (2,5)
try:
    print(arr_2d + [2, 3])
except ValueError as e:
    print("Broadcasting Error:", e)

# Output: ValueError due to shape mismatch (2,5) vs (2,)


import numpy as np

'''
⚡ Vectorization in NumPy
Vectorization refers to performing operations on entire arrays without using explicit loops.
This leads to faster and more concise code.
'''

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# ➕ Element-wise addition
print("Addition:", array1 + array2)
# Output: [5 7 9]

# ✖️ Scalar multiplication (broadcasting 35 to each element)
print("Scalar Multiplication (array1 * 35):", array1 * 35)
# Output: [ 35  70 105]

# ➗ Modulus operator on array elements
print("Modulo (array2 % 3):", array2 % 3)
# Output: [1 2 0]

# ➗ Division of each element in arr_2d by 2
arr_2d = np.array([[2, 3, 4, 8, 10],
                   [5, 6, 7, 12, 4]])
print("2D Array Division by 2:\n", arr_2d / 2)
# Output:
# [[1.  1.5 2.  4.  5. ]
#  [2.5 3.  3.5 6.  2. ]]
