Awesome 🚀 Let’s build **practice problems for Matrix Operations in NumPy** step by step.
I’ll give you **problems + hints + solutions** (like worksheets you can give to your students).

---

# 📝 Practice Problems – Matrix Operations

---

## **Problem 1: Basic Addition & Subtraction**

Matrix of sales in two shops (in units sold):

```
Shop A:
[[10 20]
 [30 40]]

Shop B:
[[5 10]
 [15 20]]
```

**Task:**

1. Find the **total sales** (A + B).
2. Find the **difference in sales** (A - B).

🔍 *Hint:* Use `+` and `-`.

✅ **Solution:**

```python
import numpy as np

A = np.array([[10, 20], [30, 40]])
B = np.array([[5, 10], [15, 20]])

print("Total sales:\n", A + B)
print("Difference in sales:\n", A - B)
```

---

## **Problem 2: Element-wise vs Dot Product**

Given:

```
A = [[1 2]
     [3 4]]

B = [[2 0]
     [1 2]]
```

**Task:**

1. Multiply element-wise (`A * B`).
2. Find dot product (`A @ B`).

🔍 *Hint:* `*` = element-wise, `@` = dot product.

✅ **Solution:**

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print("Element-wise:\n", A * B)
print("Dot product:\n", A @ B)
```

---

## **Problem 3: Transpose (Switching Rows & Columns)**

Matrix of students’ marks:

```
Marks = [[80 90 70]
         [85 95 75]]
```

Rows = Students, Columns = Subjects.
**Task:** Find transpose to see subjects vs students.

✅ **Solution:**

```python
marks = np.array([[80, 90, 70], [85, 95, 75]])
print(marks.T)
```

---

## **Problem 4: Determinant & Inverse**

Given:

```
A = [[4 7]
     [2 6]]
```

**Task:**

1. Find determinant.
2. Find inverse.
3. Verify that `A @ A_inv = I` (Identity).

✅ **Solution:**

```python
A = np.array([[4, 7], [2, 6]])

det = np.linalg.det(A)
inv = np.linalg.inv(A)

print("Determinant:", det)
print("Inverse:\n", inv)
print("Check:\n", A @ inv)  # should be Identity
```

---

## **Problem 5: Solving Linear Equations**

Solve the system:

```
3x + 2y = 18
x +  y  =  8
```

**Hint:** Write in matrix form `AX = B`.

✅ **Solution:**

```python
A = np.array([[3, 2], [1, 1]])
B = np.array([18, 8])

X = np.linalg.solve(A, B)
print("Solution: x =", X[0], ", y =", X[1])
```

---

## **Problem 6 (Real-World Physics Example): Force Calculation**

A car company tested 2 cars with different masses and accelerations:

```
Mass = [[1000 1200]
        [1500 1800]]   # kg

Acceleration = [[2]
                [3]]   # m/s²
```

**Task:** Calculate force using `Force = Mass @ Acceleration`.

✅ **Solution:**

```python
mass = np.array([[1000, 1200], [1500, 1800]])
acceleration = np.array([[2], [3]])

force = mass @ acceleration
print("Force (N):\n", force)
```

---
