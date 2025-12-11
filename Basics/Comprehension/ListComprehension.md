---
---

# ✅ **List Comprehension in Python (Beginner to Pro)**

List comprehension is a **short and powerful way** to create new lists from existing data.

### 👉 **It is basically a shortcut for writing loops to build lists.**

---

# 🔹 1. **Basic Syntax**

```
new_list = [ expression  for item in iterable ]
```

### Example:

```
numbers = [1, 2, 3, 4]
squares = [n*n for n in numbers]
print(squares)
```

**Output:**

```
[1, 4, 9, 16]
```

---

# 🔹 2. **With Condition (if)**

Syntax:

```
new_list = [ expression for item in iterable if condition ]
```

### Example: Keep even numbers only

```python
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print(evens)
```

**Output:**

```
[2, 4, 6]
```

---

# 🔹 3. **If–Else Inside List Comprehension**

Syntax:

```
new_list = [ expression_if_true if condition else expression_if_false for item in iterable ]
```

### Example: Label numbers as odd/even

```python
nums = [1, 2, 3, 4]
labels = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(labels)
```

**Output:**

```
['Odd', 'Even', 'Odd', 'Even']
```

---

# 🔹 4. **Nested List Comprehension**

Example: Flatten a 2D list

```python
matrix = [[1,2,3],[4,5,6]]
flat = [num for row in matrix for num in row]
print(flat)
```

**Output**

```
[1, 2, 3, 4, 5, 6]
```

---

# 🔥 REAL WORLD USE CASES

---

# ✅ **Use Case 1: Cleaning Data (Removing Empty Strings)**

```python
names = ["Ali", "", "Ahmed", "", "Zara"]
cleaned = [n for n in names if n != ""]
print(cleaned)
```

**Output**

```
['Ali', 'Ahmed', 'Zara']
```

---

# ✅ **Use Case 2: Extract Numbers from a Mixed List**

```python
items = ["apple", 3, "banana", 5, 18, "cat"]
numbers = [i for i in items if type(i) == int]
print(numbers)
```

**Output**

```
[3, 5, 18]
```

---

# ✅ **Use Case 3: Convert All Text to Lowercase (Data processing)**

```python
words = ["Hello", "PYTHON", "WORLD"]
lower = [w.lower() for w in words]
print(lower)
```

---

# ✅ **Use Case 4: Create a List of Squares from 1 to 100 (Math/ML preprocessing)**

```python
squares = [n*n for n in range(1, 101)]
```

Useful in **machine learning**, **matrix operations**, etc.

---

# ✅ **Use Case 5: Filtering Emails (Real App Scenario)**

```python
emails = ["a@gmail.com","b@yahoo.com","x@gmail.com"]
gmail_only = [e for e in emails if e.endswith("@gmail.com")]
print(gmail_only)
```

**Output**

```
['a@gmail.com', 'x@gmail.com']
```

---

# ✅ **Use Case 6: Read File and Extract Only Important Lines**

```python
lines = [line.strip() for line in open("log.txt") if "ERROR" in line]
```

---

# 🚀 BONUS: **Dictionary & Set Comprehensions**

### Dictionary:

```python
squares = {n: n*n for n in range(5)}
```

### Set:

```python
unique_lengths = {len(word) for word in ["hi", "hello", "hi"]}
```

---

# ⭐ Summary

| Concept | Example                                       |
| ------- | --------------------------------------------- |
| Basic   | `[x*x for x in nums]`                         |
| Filter  | `[x for x in nums if x>5]`                    |
| If-Else | `["Even" if x%2==0 else "Odd" for x in nums]` |
| Nested  | `[num for row in matrix for num in row]`      |

---
