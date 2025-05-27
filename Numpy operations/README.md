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
