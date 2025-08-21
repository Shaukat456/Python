Perfect 🙌 Let’s dive into **NumPy Mathematical & Statistical Operations** in a **step-by-step way** (with exercises and real-world examples).

---

# 🔢 1. Element-wise Operations (Vectorization)

Instead of looping through lists, NumPy lets you apply math directly:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Square:", arr ** 2)
print("Half:", arr / 2)
```

✅ Output:

```
Add 5: [15 25 35 45]
Multiply by 2: [20 40 60 80]
Square: [100 400 900 1600]
Half: [ 5. 10. 15. 20.]
```

⚡ **Why useful?**

- Finance: Apply tax % to all salaries.
- Physics: Multiply all forces by a constant factor.
- Data Cleaning: Convert Celsius → Fahrenheit for a whole dataset.

---

# 📊 2. Aggregate Functions (Quick Stats)

```python
arr = np.array([5, 10, 15, 20, 25])

print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())
print("Standard Deviation:", arr.std())
```

✅ Output:

```
Sum: 75
Mean: 15.0
Max: 25
Min: 5
Standard Deviation: 7.07
```

⚡ **Why useful?**

- Teachers can quickly calculate class average, topper, lowest marks.
- Analysts can summarize sales figures in seconds.

---

# 🧑‍🎓 3. Real-World Example: Student Marks

```python
marks = np.array([85, 90, 78, 88, 92, 95])

print("Class Average:", marks.mean())
print("Highest Score:", marks.max())
print("Lowest Score:", marks.min())
print("Total Marks:", marks.sum())
```

✅ Output:

```
Class Average: 88.0
Highest Score: 95
Lowest Score: 78
Total Marks: 528
```

⚡ **Usage**: Teacher analyzing students’ performance.

---

# 🌡️ 4. Real-World Example: Weather Station

```python
temps = np.array([30.5, 32.0, 31.2, 29.8, 28.4, 30.1, 31.5])

print("Average Temp:", temps.mean())
print("Hottest Day:", temps.max())
print("Coldest Day:", temps.min())
print("Temperature Variation:", temps.std())
```

✅ Output:

```
Average Temp: 30.5
Hottest Day: 32.0
Coldest Day: 28.4
Temperature Variation: 1.2
```

⚡ **Usage**: Weather forecasting & climate analysis.

---

# 🧮 5. Matrix Operations (Foundation for ML)

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix Addition:\n", A + B)
print("Matrix Subtraction:\n", A - B)
print("Matrix Multiplication (dot product):\n", A @ B)   # or np.dot(A, B)
print("Transpose of A:\n", A.T)
```

✅ Output:

```
Matrix Addition:
 [[ 6  8]
 [10 12]]

Matrix Subtraction:
 [[-4 -4]
 [-4 -4]]

Matrix Multiplication:
 [[19 22]
 [43 50]]

Transpose of A:
 [[1 3]
 [2 4]]
```

⚡ **Usage**:

- Physics: Transformations of coordinates.
- Machine Learning: Training models (matrix multiplication is at the heart of neural networks).

---

# 📝 Exercises for You

1. Create an array of salaries `[25000, 30000, 28000, 35000, 40000]`.

   - Increase each salary by 10%.
   - Find average salary, highest, lowest.

2. Create a NumPy array of cricket runs `[45, 60, 32, 120, 85, 55]`.

   - Find team average, max runs, min runs, and standard deviation.

3. Make two 2×2 matrices and perform addition, subtraction, and multiplication.
