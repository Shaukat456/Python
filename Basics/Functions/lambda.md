---
---

# ⚡ **Lambda Functions in Python**

## 🔹 What is a Lambda Function?

A **lambda function** is a **small, anonymous (nameless) function** written in **one line**.

### Syntax

```python
lambda arguments : expression
```

✔ No `def`
✔ One expression only
✔ Returns value automatically

---

## 🔹 1️⃣ Normal Function vs Lambda

### Normal function

```python
def square(x):
    return x * x
```

### Lambda function

```python
square = lambda x: x * x
print(square(5))
```

---

# 🔹 2️⃣ Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(3, 4))
```

---

# 🔹 3️⃣ Lambda Inside Another Function

```python
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(5))   # 10
```

---

# 🔥 WHERE LAMBDA IS ACTUALLY USED

Mostly with:
✅ `map()`
✅ `filter()`
✅ `reduce()`
✅ `sorted()` / `min()` / `max()`

---

# 🧠 4️⃣ `map()` with Lambda

### 👉 Apply a function to every item

```python
nums = [1, 2, 3, 4]

squares = list(map(lambda x: x*x, nums))
print(squares)
```

---

# 🧠 5️⃣ `filter()` with Lambda

### 👉 Keep items that match a condition

```python
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

---

# 🧠 6️⃣ `reduce()` with Lambda

### 👉 Reduce list to a single value

```python
from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, nums)
print(total)
```

---

# 🌍 REAL-WORLD USE CASES

---

## ✅ Use Case 1: Sort Data by Key (Very Common)

```python
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 70}
]

sorted_students = sorted(students, key=lambda s: s["marks"])
print(sorted_students)
```

---

## ✅ Use Case 2: Extract Specific Field

```python
users = [
    {"id": 1, "email": "a@gmail.com"},
    {"id": 2, "email": "b@yahoo.com"}
]

emails = list(map(lambda u: u["email"], users))
print(emails)
```

---

## ✅ Use Case 3: Filter Valid Emails

```python
emails = ["a@gmail.com", "test", "b@yahoo.com"]

valid = list(filter(lambda e: "@" in e, emails))
print(valid)
```

---

## ✅ Use Case 4: Price Calculation (E-commerce)

```python
prices = [100, 200, 300]

with_tax = list(map(lambda p: p * 1.15, prices))
print(with_tax)
```

---

# 🔥 Lambda vs List Comprehension (IMPORTANT)

### Example: Square numbers

```python
# Lambda + map
squares = list(map(lambda x: x*x, nums))

# List comprehension (better & readable)
squares = [x*x for x in nums]
```

👉 **Prefer list comprehension** when possible.

---

# ⚠️ Limitations of Lambda

❌ Only one expression
❌ No statements (`if`, `for`, `while` blocks)
❌ Hard to debug if complex

👉 Use `def` for complex logic.

---

# ⭐ Summary Table

| Concept | Example                                |
| ------- | -------------------------------------- |
| Lambda  | `lambda x: x*x`                        |
| map     | `map(lambda x: x*x, nums)`             |
| filter  | `filter(lambda x: x>5, nums)`          |
| reduce  | `reduce(lambda a,b: a+b, nums)`        |
| key     | `sorted(data, key=lambda x: x["age"])` |

---
