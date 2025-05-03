# NumPy Array Creation Guide

This guide provides examples for creating NumPy arrays of various dimensions, initializing arrays with specific values, generating sequences, identity matrices, and using random number generation.

---

## 1. Creating Arrays

### 1.1 One-Dimensional Array
```python
one_d_array = np.array([1, 2, 3, 4])
```

### 1.2 Two-Dimensional Array (Matrix)
```python
two_d_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]])
```

---

## 2. Arrays with Constant Values

### 2.1 Zeros
```python
zero_array_1d = np.zeros(3)           # [0. 0. 0.]
zero_array_2d = np.zeros((3, 4))      # 3x4 matrix of zeros
```

### 2.2 Ones
```python
ones_array = np.ones((2, 3))          # 2x3 matrix of ones
```

### 2.3 Filled with a Specific Value
```python
filled_array = np.full((2, 3), 5)     # 2x3 matrix filled with 5
```

---

## 3. Sequence Arrays

### 3.1 Using `np.arange()`
```python
sequence_array = np.arange(1, 11, 2)   # [1 3 5 7 9]
```

### 3.2 Identity Matrix
```python
identity_matrix = np.eye(5)           # 5x5 Identity matrix
```

---

## 4. Multidimensional Arrays

### 4.1 Three-Dimensional Array
```python
# Shape: 4 blocks, each with 3 rows and 4 columns
arr_3d = np.ones((4, 3, 4))
```

### 4.2 Four-Dimensional Array
```python
# Shape: 2 blocks × 3 sub-blocks × 4 rows × 5 elements
arr_4d = np.ones((2, 3, 4, 5))
```

You can continue this pattern to create arrays with even higher dimensions (5D, 6D, etc.).

---

## 5. Arrays with Random Values

### 5.1 Random Float Arrays
```python
np.random.rand(2, 3)              # Random floats in [0, 1)
np.random.random((3, 2))          # Same as rand, alternative syntax
```

### 5.2 Random Integers
```python
np.random.randint(1, 10, size=7)      # 1D array of 7 random ints [1, 10)
np.random.randint(1, 10, (3, 4))      # 2D array of random ints
```

### 5.3 Random Choice
```python
np.random.choice([10, 20, 30, 40], size=5)  # Picks 5 values randomly from list
```

### 5.4 Reproducibility with Seed
```python
np.random.seed(37)
np.random.randint(1, 100, 5)  # Same output every time when seed is set
```

Setting a seed ensures your results are reproducible for testing or demonstration purposes.

---

✅ With these methods, you can efficiently create and initialize arrays in NumPy across different shapes, dimensions, and value types!
