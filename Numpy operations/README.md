# 📊 NumPy Operators, Aggregation & Sorting Functions

This repository showcases how to perform mathematical operations, aggregation functions, and array sorting using NumPy. These fundamental concepts help you manipulate, summarize, and order data with high performance and minimal code.

---

## 📘 Table of Contents
1. [Introduction](#1-introduction)
2. [Mathematical Operators](#2-mathematical-operators)
3. [Aggregation Functions](#3-aggregation-functions)
4. [Sorting Arrays](#4-sorting-arrays)
5. [Conclusion](#5-conclusion)

---

## 1. Introduction

NumPy is a powerful library in Python used for numerical computing. It enables fast operations on arrays, matrix calculations, and statistical evaluations. This guide walks through the basics of using NumPy for arithmetic, summarization, and sorting.

---

## 2. Mathematical Operators

NumPy supports element-wise operations between arrays using familiar Python symbols:

| Operator | Description          |
|----------|----------------------|
| `+`      | Addition              |
| `-`      | Subtraction           |
| `*`      | Multiplication        |
| `/`      | Division              |
| `**`     | Exponentiation        |
| `//`     | Floor Division        |
| `%`      | Modulo (Remainder)    |

**Example:**
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Output: [5 7 9]
```

## 3. Aggregation Functions

Aggregation functions help summarize and analyze your data.

| Function    | Description                        |
| ----------- | ---------------------------------- |
| `np.sum()`  | Sum of all elements                |
| `np.mean()` | Mean (average)                     |
| `np.min()`  | Minimum value                      |
| `np.max()`  | Maximum value                      |
| `np.std()`  | Standard deviation                 |
| `np.var()`  | Variance (square of std deviation) |

**Example:**
```python
import numpy as np

data = np.array([10, 20, 30, 40])
print(np.mean(data))  # Output: 25.0
print(np.sum(data))   # Output: 100
```

## 4. Sorting Arrays

Sorting is often required for organizing and analyzing datasets. This section refers to the code in `sorting.py`.

### ✅ 4.1 1D Array Sorting
```python
import numpy as np

unsorted_1d_arr = np.array([3, 1, 5, 8, 3, 0])
sorted_asc = np.sort(unsorted_1d_arr)         # Ascending
sorted_desc = np.sort(unsorted_1d_arr)[::-1]  # Descending

print("Sorted Ascending:", sorted_asc)
print("Sorted Descending:", sorted_desc)
```

### ✅ 4.2 2D Array Sorting
```python
unsorted_2d_arr = np.array([[3, 1], [1, 2], [2, 3]])

# Column-wise sort (axis=0)
print("Column-wise Sort:\n", np.sort(unsorted_2d_arr, axis=0))

# Row-wise sort (axis=1)
print("Row-wise Sort:\n", np.sort(unsorted_2d_arr, axis=1))
```

### ✅ 4.3 Reverse Sorting in 2D Arrays
```python
# Row-wise reverse sort
sorted_rows_desc = np.sort(unsorted_2d_arr, axis=1)[:, ::-1]
print("Row-wise Reverse Sort:\n", sorted_rows_desc)

# Column-wise reverse sort
sorted_cols_desc = np.sort(unsorted_2d_arr, axis=0)[::-1, :]
print("Column-wise Reverse Sort:\n", sorted_cols_desc)
```
###✅ 4.4 Getting Sort Indices
```python
arr = np.array([10, 2, 8, 4, 6])

# Get indices for descending sort
indices_desc = np.argsort(arr)[::-1]
print("Descending order indices:", indices_desc)

# Use indices to reorder the array
print("Sorted using indices:", arr[indices_desc])
```

## 5. Conclusion

With NumPy, you can efficiently:

-✅ Perform fast, vectorized mathematical operations
-✅ Aggregate data with built-in statistical functions
-✅ Sort and index arrays flexibly, even in multiple dimensions

### 💡 Key Takeaways:

-NumPy enables concise and efficient array operations.
-Aggregation functions are powerful tools for summarizing data.
-Sorting tools include standard sorting, reverse sorting, and index tracking.
