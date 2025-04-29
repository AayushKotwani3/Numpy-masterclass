# 📦 NumPy Broadcasting and Vectorization

This guide explains two core concepts in NumPy that enable high-performance array operations without the need for explicit Python loops: **Broadcasting** and **Vectorization**.

---

## 📘 Table of Contents
1. Introduction
2. Broadcasting
3. Vectorization
4. Key Differences
5. Conclusion

---

## 1. Introduction

NumPy is optimized for fast numerical operations. Two of its most powerful features are:
- **Broadcasting**: Automatically expanding dimensions to match arrays during operations.
- **Vectorization**: Applying operations to entire arrays at once without explicit iteration.

These help in writing concise, readable, and efficient code for large-scale data processing.

---

## 2. 📡 Broadcasting

Broadcasting allows NumPy to perform operations on arrays of different shapes, by automatically expanding the smaller array to match the shape of the larger one.

### ✅ Example:
```python
import numpy as np

arr = np.array([10, 13, 45, 79, 90])
discount = 10

# Applying scalar discount to each item in array
# Equivalent to arr - (arr * 0.10)
disc_arr = arr - (arr * (discount / 100))
print(disc_arr)
# Output: [ 9.  11.7  40.5  71.1  81. ]
```

### ✅ Broadcasting between 1D and 2D:
```python
arr_2d = np.array([[2, 3, 4, 8, 10],
                   [5, 6, 7, 12, 4]])

# Broadcasting scalar 10
print(arr_2d + 10)
# Output:
# [[12 13 14 18 20]
#  [15 16 17 22 14]]

# Broadcasting 1D array to 2D
arr = np.array([10, 13, 45, 79, 90])
print(arr_2d + arr)
# Output:
# [[12 16 49 87 100]
#  [15 19 52 91 94]]
```

### ❌ When shapes are not compatible:
```python
# This will raise an error because the shape [2, 5] and [2,] can't broadcast
print(arr_2d + [2, 3])
# ValueError
```

---

## 3. ⚡ Vectorization

Vectorization allows you to perform operations on entire arrays without using `for` loops.

### ✅ Example:
```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
print(array1 + array2)  # Output: [5 7 9]

# Scalar multiplication
print(array1 * 35)      # Output: [35 70 105]

# Modulo operation
print(array2 % 3)       # Output: [1 2 0]

# Vectorized division of 2D array
arr_2d = np.array([[2, 3, 4, 8, 10],
                   [5, 6, 7, 12, 4]])
print(arr_2d / 2)
# Output:
# [[1.  1.5 2.  4.  5. ]
#  [2.5 3.  3.5 6.  2. ]]
```

### ✅ Advantages:
- Much faster than using loops
- Less code = better readability
- Takes advantage of underlying C implementations

---

## 4. 🔍 Key Differences
| Feature        | Broadcasting                     | Vectorization                         |
|----------------|----------------------------------|----------------------------------------|
| Definition     | Auto-expanding shapes to match   | Applying operations over entire arrays |
| Requirement    | Operands of different shapes      | Arrays must support element-wise ops   |
| Use Case       | Mixing scalars with arrays, etc. | Mathematical operations on arrays      |

---

## 5. ✅ Conclusion

With **broadcasting**, you can mix and match scalars and arrays. With **vectorization**, you can avoid slow `for` loops entirely. Combined, they make NumPy extremely powerful for numerical computing.

Explore more in the [NumPy documentation](https://numpy.org/doc/stable/).

