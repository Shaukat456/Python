    Perfect! 🚀 Let’s dive into **Indexing & Boolean Masking in NumPy** — this is one of the most powerful features for **data analysis, filtering, and working with large datasets**.

---

# 🔍 1. Basic Indexing

Just like Python lists, NumPy arrays can be indexed.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])
print("First 3 elements:", arr[:3])
```

✅ Output:

```
First element: 10
Last element: 50
First 3 elements: [10 20 30]
```

⚡ **Real-World Use:** Accessing specific data points (e.g., first 10 students’ marks).

---

# 🔍 2. Indexing in 2D Arrays

```python
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print("Element at row 0, col 1:", matrix[0,1])  # 2
print("First row:", matrix[0])
print("First column:", matrix[:,0])
```

✅ Output:

```
Element at row 0, col 1: 2
First row: [1 2 3]
First column: [1 4 7]
```

⚡ **Real-World Use:** Extracting rows & columns from a dataset (e.g., selecting "Age" column from a student database).

---

# 🔍 3. Boolean Indexing (Masking)

You can filter values based on **conditions**.

```python
scores = np.array([45, 67, 89, 32, 76, 50])

print("Scores greater than 60:", scores[scores > 60])
print("Scores less than 50:", scores[scores < 50])
```

✅ Output:

```
Scores greater than 60: [67 89 76]
Scores less than 50: [45 32]
```

⚡ **Real-World Use:**

* Find students who scored above passing marks.
* Filter products cheaper than \$100.

---

# 🔍 4. Multiple Conditions

```python
ages = np.array([15, 18, 22, 30, 40, 12, 19])

print("Teenagers (13-19):", ages[(ages >= 13) & (ages <= 19)])
```

✅ Output:

```
Teenagers (13-19): [15 18 19]
```

⚡ **Real-World Use:** Selecting customers within a specific age group.

---

# 🔍 5. Fancy Indexing (Select Specific Indices)

```python
arr = np.array([100, 200, 300, 400, 500])

print("Pick elements at positions 0, 2, 4:", arr[[0,2,4]])
```

✅ Output:

```
Pick elements at positions 0, 2, 4: [100 300 500]
```

⚡ **Real-World Use:** Selecting specific records from a dataset.

---

# 🎮 Real-World Example: Students Filtering

```python
students = np.array(["Ali", "Sara", "John", "Fatima", "David"])
marks = np.array([85, 40, 72, 95, 33])

# Find students who passed (marks >= 50)
passed = students[marks >= 50]

print("Students who passed:", passed)
```

✅ Output:

```
Students who passed: ['Ali' 'John' 'Fatima']
```

---

# 📝 Exercises for You

1. From the array `[12, 45, 67, 23, 89, 100, 34]`, get numbers greater than 50.
2. Extract the 2nd row and 3rd column element from a `3x3` matrix.
3. Given `ages = [5, 12, 17, 19, 24, 45, 60]`, find all ages between 18 and 40.
4. Create an array of marks and find students who failed (marks < 40).

