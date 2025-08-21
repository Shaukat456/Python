Perfect 👍 Let’s learn **NumPy in English step by step**.

---

# 🧠 What is NumPy?

**NumPy** = **Numerical Python**

* It’s **much faster than Python lists**.
* Used for **large data handling**.
* Provides **arrays** (multi-dimensional data structures) optimized for mathematical calculations.

---

## 🔍 Step 1: Installation

If you don’t have NumPy installed:

```bash
pip install numpy
```

---

## 🔍 Step 2: Import

```python
import numpy as np
```

We use `np` as a shortcut.

---

## 🔍 Step 3: Creating Arrays

Convert Python list → NumPy array:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)       # [1 2 3 4 5]
print(type(arr)) # <class 'numpy.ndarray'>
```

⚡ Difference:

* **Python List** → `[1, 2, 3]` (slower for math)
* **NumPy Array** → optimized, faster

---

## 🔍 Step 4: Dimensions

```python
# 1D Array
a = np.array([1, 2, 3])
print(a.ndim)   # 1

# 2D Array (Matrix)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.ndim)   # 2

# 3D Array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c.ndim)   # 3
```

---

## 🔍 Step 5: Array Properties

```python
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)   # (2, 3) → 2 rows, 3 columns
print(arr.size)    # 6 elements
print(arr.dtype)   # int32 (data type)
```

---

## 🔍 Step 6: Mathematical Operations

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # [5 7 9]
print(x * y)  # [ 4 10 18]
print(x ** 2) # [1 4 9]
print(np.sqrt(y)) # [2. 2.236 2.449]
```

---

## 🔍 Step 7: Special Arrays

```python
print(np.zeros((2,3)))   # 2x3 matrix of zeros
print(np.ones((2,2)))    # 2x2 matrix of ones
print(np.eye(3))         # 3x3 Identity matrix
print(np.arange(0, 10, 2))  # [0 2 4 6 8]
print(np.linspace(0, 1, 5)) # [0.   0.25 0.5  0.75 1. ]
```

---

## 🔍 Step 8: Indexing & Slicing

```python
arr = np.array([10,20,30,40,50])
print(arr[0])    # 10
print(arr[-1])   # 50
print(arr[1:4])  # [20 30 40]
```

2D Example:

```python
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0,1])   # Row 0, Col 1 → 2
print(arr[1,:])   # Row 1 → [4 5 6]
print(arr[:,2])   # Col 2 → [3 6 9]
```

---

## 🔍 Step 9: Real-World Example

👉 Example: Physics (Velocity = Distance / Time)

```python
distance = np.array([100, 200, 300, 400])  # meters
time = np.array([10, 20, 25, 40])          # seconds

velocity = distance / time
print(velocity)  # [10. 10. 12. 10.]
```

---

