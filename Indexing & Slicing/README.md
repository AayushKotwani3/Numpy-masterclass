
# 🔍 NumPy Indexing, Slicing, and Filtering

This repository demonstrates how to access and manipulate data in NumPy arrays using **indexing**, **slicing**, **fancy indexing**, and **boolean masking** techniques. These operations are essential for data manipulation and form the backbone of most data science and numerical computing workflows.

---

## 📘 Table of Contents

1. [Introduction](#introduction)  
2. [Indexing](#indexing)  
3. [Slicing](#slicing)  
4. [2D Array Slicing](#2d-array-slicing)  
5. [Fancy Indexing](#fancy-indexing)  
6. [Boolean Masking & Filtering](#boolean-masking--filtering)  
7. [Using `np.where`](#using-npwhere)  
8. [Conclusion](#conclusion)

---

## 📌 Introduction

NumPy is a foundational Python library used for efficient numerical operations. Understanding how to access and modify elements in arrays is key to working with NumPy. This guide walks through examples that explain:

- Accessing single and multiple values
- Selecting slices or subarrays
- Applying conditional logic to filter data

---

## 🧹 Indexing

### 1D Array  
```python
arr[index]
```

### 2D Array  
```python
arr[row, column]
```

🔹 Example:  
```python
arr_1d = np.array([1.4, 2, 3.7, 4, 5, 6])
arr_2d = np.array([[1, 2, 30], [4, 50, 6], [70, 8, 9]])

print(arr_1d[2])      # Output: 3.7  
print(arr_2d[1, 2])   # Output: 6
```

---

## ✂️ Slicing

### Syntax  
```python
arr[start:stop:step]
```

🔹 Examples:  
```python
first = arr_1d[1:4]    # [2, 3.7, 4]
second = arr_1d[:4]    # [1.4, 2, 3.7, 4]
third = arr_1d[::2]    # [1.4, 3.7, 5]
fourth = arr_1d[::-1]  # [6, 5, 4, 3.7, 2, 1.4]
```

---

## 🧩 2D Array Slicing

You can slice rows and columns simultaneously:

```python
print(arr_2d[1])          # Second row
print(arr_2d[:, 2])       # Third column
print(arr_2d[0:3, 1:3])   # Sub-array from rows 0-2 and columns 1-2
```

---

## 🎯 Fancy Indexing

Fancy indexing lets you access multiple arbitrary indices at once.

```python
print(arr_1d[[0, 2, 4]])  # Output: [1.4, 3.7, 5]
```

---

## 🧪 Boolean Masking & Filtering

### Filtering 2D Array  
```python
print(arr_2d[arr_2d > 25])  # Output: [30 50 70]
```

### Filtering Even Numbers from 1D  
```python
numbers = np.array([1, 2, 0, 3, 5, 6, 7, 8, 9, 10, 12, 45, 68, 90])
even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)  # Output: [ 2  0  6  8 10 12 68 90]
```

### Filtering with Boolean Mask  
```python
mask = numbers > 5
print(numbers[mask])  # Output: [ 6  7  8  9 10 12 45 68 90]
```

---

## 🧠 Using `np.where`

### Getting Indices of Elements Matching a Condition  
```python
where_result = np.where(numbers > 5)
print(where_result)             # Output: (array([...]),)
print(numbers[where_result])    # Output: [ 6  7  8  9 10 12 45 68 90]
```

### Conditional Replacement  
```python
condition_array = np.where(numbers > 5, numbers * 4, numbers)
print(condition_array)
```

### Conditional Labeling  
```python
condition_array2 = np.where(numbers > 5, "True", "False")
print(condition_array2)
```

---

## ✅ Conclusion

This guide covered the core techniques for working with subsets of NumPy arrays:

- Indexing individual elements  
- Slicing ranges  
- Fancy indexing for custom selection  
- Boolean masks and conditionals for filtering  

These skills are essential for data preprocessing and manipulation in any scientific or machine learning pipeline.

---

## 💡 Pro Tip

Practice modifying arrays and chaining these techniques to prepare for real-world data workflows.

