import numpy as np

# Creating a 1D NumPy array
array = np.array([20, 30, 40, 50, 60])

# -------------------------
# np.sum()
# Calculates the sum of all elements in the array
print(np.sum(array))  
# Output: 200
# Meaning: 20 + 30 + 40 + 50 + 60 = 200

# -------------------------
# np.mean()
# Calculates the average (arithmetic mean) of the array elements
print(np.mean(array))  
# Output: 40.0
# Meaning: (Sum of elements) / (Number of elements) → 200/5 = 40.0

# -------------------------
# np.min()
# Finds the smallest (minimum) value in the array
print(np.min(array))  
# Output: 20
# Meaning: Among 20, 30, 40, 50, 60 → minimum is 20

# -------------------------
# np.max()
# Finds the largest (maximum) value in the array
print(np.max(array))  
# Output: 60
# Meaning: Among 20, 30, 40, 50, 60 → maximum is 60

# -------------------------
# np.std()
# Calculates the standard deviation (spread or dispersion) of the array elements
print(np.std(array))  
# Output: 14.142135623730951
# Meaning: How much the numbers differ from the mean (larger std means more spread).

# -------------------------
# np.var()
# Calculates the variance (square of standard deviation)
print(np.var(array))  
# Output: 200.0
# Meaning: Variance measures the average degree to which each number is different from the mean.

