Perfect 👍 we’ll continue NumPy like this:
👉 **Every topic explained step by step → with code → with real-world example → why it’s useful.**

We just finished **vectorization**.
Now let’s move on to **useful vectorized functions in NumPy** 🚀

---

# 🔹 Common Vectorized Functions in NumPy

## 1. **Arithmetic Functions**

These apply to each element in an array **without loops**.

### Example: `np.add`, `np.subtract`, `np.multiply`, `np.divide`

```python
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(np.add(a, b))       # [11 22 33 44]
print(np.subtract(a, b))  # [ 9 18 27 36]
print(np.multiply(a, b))  # [ 10  40  90 160]
print(np.divide(a, b))    # [10. 10. 10. 10.]
```

✅ **Real-world usage**:
Imagine `a` = salaries, `b` = bonuses → you can compute totals, differences, or multipliers **instantly**.

---

## 2. **Exponential and Logarithmic Functions**

### Example

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.exp(arr))  # exponential growth
print(np.log(arr))  # natural log
print(np.log10(arr)) # log base 10
```

✅ **Real-world usage**:

- `np.exp` → used in **compound interest, population growth, ML activation functions**.
- `np.log` → used in **finance** (log returns of stock prices), or **science** (pH scale in chemistry).

---

## 3. **Power and Square Root**

```python
arr = np.array([4, 9, 16, 25])

print(np.sqrt(arr))      # square root
print(np.power(arr, 2))  # arr^2
```

✅ **Real-world usage**:

- `np.sqrt` → physics (speed = √(2gh)), machine learning (RMSE error).
- `np.power` → amplify signals, image brightness adjustments.

---

## 4. **Trigonometric Functions**

```python
angles = np.array([0, np.pi/2, np.pi])  # radians

print(np.sin(angles))  # [0, 1, 0]
print(np.cos(angles))  # [1, 0, -1]
print(np.tan(angles))  # [0, very large]
```

✅ **Real-world usage**:

- Engineering: wave motion, signals.
- Computer graphics: rotating objects.

---

## 5. **Rounding Functions**

```python
arr = np.array([3.14, 2.718, 1.618])

print(np.round(arr))   # [3. 3. 2.]
print(np.floor(arr))   # [3. 2. 1.] (round down)
print(np.ceil(arr))    # [4. 3. 2.] (round up)
```

✅ **Real-world usage**:

- Finance: rounding prices.
- Gaming: health points → rounded to nearest integer.

---

## 6. **Statistical Functions**

```python
data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))   # average → 30
print(np.median(data)) # middle value → 30
print(np.std(data))    # standard deviation
print(np.var(data))    # variance
print(np.min(data))    # min
print(np.max(data))    # max
```

✅ **Real-world usage**:

- Data science: analyzing exam scores, sensor readings.
- Finance: finding average revenue, risk (std dev).
- Sports: analyzing player performance.

---

## 7. **Cumulative Functions**

```python
arr = np.array([1, 2, 3, 4])

print(np.cumsum(arr))  # cumulative sum → [1, 3, 6, 10]
print(np.cumprod(arr)) # cumulative product → [1, 2, 6, 24]
```

✅ **Real-world usage**:

- Finance: total savings over months.
- Physics: cumulative energy usage.

---

# ⚡ Big Picture

👉 NumPy functions let you:

- Work with **millions of numbers instantly** (no loops).
- Apply **math, finance, engineering, and science formulas**.
- Use **vectorization** for speed.
