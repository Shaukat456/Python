Perfect 🚀 — let’s dive into **Vectorization in NumPy**

---

# 🔹 What is Vectorization?

👉 **Vectorization means replacing slow Python loops with fast NumPy operations.**

Instead of processing **element by element** in Python, NumPy processes the **whole array at once** (internally using optimized C code).
This makes operations **much faster**.

---

## 🔹 Example 1: Squaring Numbers

### ❌ Without Vectorization (normal Python loop)

```python
nums = [1, 2, 3, 4, 5]
squares = []

for x in nums:
    squares.append(x**2)

print(squares)
```

✅ Output:

```
[1, 4, 9, 16, 25]
```

---

### ✅ With Vectorization (NumPy)

```python
import numpy as np

nums = np.array([1, 2, 3, 4, 5])
squares = nums ** 2   # vectorized operation
print(squares)
```

✅ Output:

```
[ 1  4  9 16 25 ]
```

👉 **Same result, but way faster!**

---

## 🔹 Example 2: Adding Two Arrays

### ❌ Python way (loop)

```python
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)
```

✅ Output:

```
[11, 22, 33, 44]
```

---

### ✅ NumPy way (vectorized)

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

c = a + b   # element-wise addition
print(c)
```

✅ Output:

```
[11 22 33 44]
```

👉 **No loop required.**

---

## 🔹 Example 3: Real-World — Salary Hike

Suppose you have salaries of employees and want to increase them by **10%**.

### ❌ Loop way

```python
salaries = [40000, 50000, 60000, 70000]
new_salaries = []

for s in salaries:
    new_salaries.append(s * 1.1)

print(new_salaries)
```

✅ Output:

```
[44000.0, 55000.0, 66000.0, 77000.0]
```

---

### ✅ Vectorized way

```python
salaries = np.array([40000, 50000, 60000, 70000])
new_salaries = salaries * 1.1
print(new_salaries)
```

✅ Output:

```
[44000. 55000. 66000. 77000.]
```

---

## 🔹 Example 4: Performance Difference

```python
import numpy as np
import time

# Python list way
lst = list(range(1_000_000))
start = time.time()
squares = [x**2 for x in lst]
end = time.time()
print("Python list time:", end - start)

# NumPy way
arr = np.arange(1_000_000)
start = time.time()
squares = arr**2
end = time.time()
print("NumPy vectorized time:", end - start)
```

✅ Output (approx):

```
Python list time: 0.30 sec
NumPy vectorized time: 0.01 sec
```

👉 NumPy is **\~30x faster** because it runs in **compiled C** internally.

---

# 🔹 Real-World Use Cases of Vectorization

1. **Finance** → calculate profits, taxes, stock returns for millions of rows.
2. **Physics/Engineering** → simulate particle movements in large systems.
3. **AI/ML** → matrix multiplications in training neural networks.
4. **Healthcare** → process medical images (pixel arrays).

---

✅ In summary:

- **Without vectorization** = slow loops
- **With vectorization** = fast NumPy operations
