# 🧩 NumPy Reshaping, Insertion, Appending & Splitting Guide

This guide provides a comprehensive overview of NumPy array manipulations, including reshaping arrays, inserting or appending elements, and splitting or stacking arrays. These are fundamental operations that every data scientist and Python enthusiast should understand.

---

## 📘 Table of Contents
1. [Reshaping Arrays](#reshaping-arrays)
2. [Flattening Arrays](#flattening-arrays)
3. [Insertion](#insertion)
4. [Appending Arrays](#appending-arrays)
5. [Concatenation](#concatenation)
6. [Deletion](#deletion)
7. [Stacking Arrays](#stacking-arrays)
8. [Splitting Arrays](#splitting-arrays)
9. [Conclusion](#conclusion)

---

## 🔁 Reshaping Arrays
- **`reshape(rows, columns)`**
- Used to convert a 1D array into 2D or higher dimensions.
- Returns a **view**, not a copy.

```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
```

**Output:**
```
[[1 2 3]
 [4 5 6]]
```

---

## 📤 Flattening Arrays
To convert multi-dimensional arrays into 1D:
- **`flatten()`** – returns a **copy**
- **`ravel()`** – returns a **view**

```python
arr_2d = np.array([[2, 3, 4], [5, 6, 7]])
print(arr_2d.ravel())
print(arr_2d.flatten())
```

**Output:**
```
[2 3 4 5 6 7]
[2 3 4 5 6 7]
```

---

## ➕ Insertion
Use `np.insert()` to insert values into arrays.

```python
np.insert(array, index, value, axis=None)
```
- **axis=None**: Flattens the array before insertion
- **axis=0**: Insert row in 2D
- **axis=1**: Insert column in 2D

```python
arr_2d = np.array([[2,3,4],[5,6,7]])
new_row = np.insert(arr_2d, 1, [8,6,0], axis=0)
new_col = np.insert(arr_2d, 0, [8,6], axis=1)
```

---

## 📎 Appending Arrays
Use `np.append()` to add elements to the end of an array.

```python
new_array = np.append(arr, arr2)
```

---

## 🔗 Concatenation
Use `np.concatenate()` to join multiple arrays.

```python
combined = np.concatenate((arr, arr2), axis=0)
```

---

## ❌ Deletion
Remove elements using `np.delete()`.

```python
np.delete(arr, index)
np.delete(arr_2d, index, axis=0)  # row
np.delete(arr_2d, index, axis=1)  # column
```

---

## 🧱 Stacking Arrays
- **Vertical stacking**: `np.vstack()`
- **Horizontal stacking**: `np.hstack()`

```python
np.vstack((arr, arr2))
np.hstack((arr, arr2))
```

---

## ✂️ Splitting Arrays
Split arrays using:
- `np.hsplit()` for horizontal
- `np.vsplit()` for vertical

```python
np.hsplit(arr, 2)
np.vsplit(arr_2d, 2)
```

---

## ✅ Conclusion
By mastering these core NumPy functions, you'll be able to handle real-world data manipulation tasks efficiently:
- Reshape and transform array dimensions.
- Insert, append, and concatenate values.
- Remove unnecessary elements.
- Stack and split arrays with ease.

NumPy's flexible and powerful array operations make it the go-to library for numerical computing in Python!

---

**🔗 Explore more**: [NumPy Documentation](https://numpy.org/doc/) for advanced operations and optimization tips.

