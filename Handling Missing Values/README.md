# NumPy: Handling NaN and Infinity

This section of the repository demonstrates how to detect and replace special numerical values such as **NaN (Not a Number)** and **Infinity** using NumPy.

---

## 📌 Detecting NaN (Not a Number) values
```python
import numpy as np

arr = np.array([1, 2, np.nan, 5, 6, np.nan, 33])
print(np.isnan(arr))
# Output: [False False  True False False  True False]
```
Use `np.isnan()` to return a boolean array indicating the positions of `NaN` values.

---

## 📌 Replacing NaN values
```python
cleaned_arr = np.nan_to_num(arr, nan=4)
print(cleaned_arr)
# Output: [ 1.  2.  4.  5.  6.  4. 33.]
```
Use `np.nan_to_num(array, nan=value)` to replace all NaNs with a specific value (default is 0).

---

## 📌 Detecting Infinity values
```python
arrinf = np.array([1, 2, np.inf, 5, 6, -np.inf, 33])
print(np.isinf(arrinf))
# Output: [False False  True False False  True False]
```
`np.isinf()` returns a boolean array where `True` represents either `+inf` or `-inf`.

---

## 📌 Replacing Infinity values
```python
replaced_inf = np.nan_to_num(arrinf, posinf=10, neginf=-10)
print(replaced_inf)
# Output: [  1.   2.  10.   5.   6. -10.  33.]
```
Use `np.nan_to_num()` to handle infinite values as well using `posinf` and `neginf` parameters.

---

## ✅ Summary
- `np.isnan()` → Detects NaN
- `np.nan_to_num()` → Replaces NaN or infinite values with specified defaults
- `np.isinf()` → Detects infinity (`+inf`, `-inf`)

These utilities are essential for data cleaning and preparing numerical data for machine learning or statistical analysis.
