# 🔍 NumPy Indexing, Slicing, and Filtering

This repository demonstrates how to access and manipulate data in NumPy arrays using **indexing**, **slicing**, **fancy indexing**, and **boolean masking** techniques. These operations are essential for data manipulation and form the backbone of most data science and numerical computing workflows.

---

## 📘 Table of Contents

1. [Introduction](#introduction)  
2. [Indexing](#indexing)  
3. [Slicing](#slicing)  
4. [2D Array Slicing](#2d-array-slicing)  
5. [Fancy Indexing](#fancy-indexing)  
6. [Boolean Masking](#boolean-masking)  
7. [Conclusion](#conclusion)

---

## 📌 Introduction

NumPy is a foundational Python library used for efficient numerical operations. Understanding how to access and modify elements in arrays is key to working with NumPy. This guide walks through examples that explain:

- Accessing single and multiple values
- Selecting slices or subarrays
- Applying conditional logic to filter data

---

## 🧩 Indexing

### 1D Array  
```python
arr[index]
2D Array
python
Copy
Edit
arr[row, column]
🔹 Example:

python
Copy
Edit
arr_1d[2]  # returns 3rd element  
arr_2d[1, 2]  # returns element at 2nd row, 3rd column  
✂️ Slicing
Syntax
python
Copy
Edit
arr[start:stop:step]
start: starting index

stop: stopping index (excluded)

step: step size or skip

🔹 Examples:

python
Copy
Edit
arr[1:4]      # elements from index 1 to 3  
arr[::2]      # every 2nd element  
arr[::-1]     # reverse array  
🧮 2D Array Slicing
You can slice rows and columns simultaneously:

python
Copy
Edit
arr[row_start:row_end, col_start:col_end]
🔹 Example:

python
Copy
Edit
arr_2d[0:3, 1:3]  # selects specific rows and columns from a 2D array
🎯 Fancy Indexing
Fancy indexing lets you access multiple arbitrary indices at once.

🔹 Example:

python
Copy
Edit
arr[[0, 2, 4]]  # retrieves values at those indices
🧪 Boolean Masking
Use logical conditions to filter arrays.

🔹 Example:

python
Copy
Edit
arr[arr > 25]  # returns all values greater than 25
✅ Conclusion
This guide covered the core techniques for working with subsets of NumPy arrays:

Indexing individual elements

Slicing ranges

Fancy indexing for custom selection

Boolean masks for condition-based filtering

These skills are essential for data preprocessing and manipulation in any scientific or machine learning pipeline.

