---
---

# 🧠 `map`, `filter`, `reduce` (WITHOUT lambda)

# 🔹 1️⃣ `map()` — WITHOUT lambda

### 👉 Applies a function to every element

### Example: Square numbers

```python
def square(x):
    return x * x

nums = [1, 2, 3, 4]

squares = list(map(square, nums))
print(squares)
```

**Output**

```
[1, 4, 9, 16]
```

---

### Real-World Example: Convert USD → PKR

```python
def usd_to_pkr(price):
    return price * 280

prices = [10, 20, 50]
converted = list(map(usd_to_pkr, prices))
print(converted)
```

---

# 🔹 2️⃣ `filter()` — WITHOUT lambda

### 👉 Keeps items that pass a condition

### Example: Keep even numbers

```python
def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(is_even, nums))
print(evens)
```

**Output**

```
[2, 4, 6]
```

---

### Real-World Example: Filter valid emails

```python
def is_valid_email(email):
    return "@" in email

emails = ["a@gmail.com", "test", "b@yahoo.com"]

valid = list(filter(is_valid_email, emails))
print(valid)
```

---

# 🔹 3️⃣ `reduce()` — WITHOUT lambda

### 👉 Reduces list to a single value

```python
from functools import reduce

def add(a, b):
    return a + b

nums = [1, 2, 3, 4]

total = reduce(add, nums)
print(total)
```

**Output**

```
10
```

---

### Real-World Example: Total cart price

```python
from functools import reduce

def total_price(a, b):
    return a + b

prices = [100, 200, 300]

bill = reduce(total_price, prices)
print(bill)
```

---

# 🔥 Combining map, filter, reduce (WITHOUT lambda)

### Task:

✔ Filter even numbers
✔ Square them
✔ Find sum

```python
from functools import reduce

def is_even(x):
    return x % 2 == 0

def square(x):
    return x * x

def add(a, b):
    return a + b

nums = [1, 2, 3, 4, 5, 6]

result = reduce(add, map(square, filter(is_even, nums)))
print(result)
```

---

# 🧠 Pythonic Alternative (BEST PRACTICE)

```python
result = sum(x*x for x in nums if x % 2 == 0)
```

✔ Cleaner
✔ Faster
✔ More readable

---

# ⭐ Summary Table

| Function   | What it does   | Without lambda          |
| ---------- | -------------- | ----------------------- |
| `map()`    | Transform data | `map(square, nums)`     |
| `filter()` | Select data    | `filter(is_even, nums)` |
| `reduce()` | Combine data   | `reduce(add, nums)`     |

---
