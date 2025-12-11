---
---

# 🚀 **What Are `*args` and `**kwargs`?\*\*

In Python, when defining a function:

### ✅ `*args` = **Variable number of positional arguments**

### ✅ `**kwargs` = **Variable number of keyword arguments**

These allow you to write **flexible functions** that can accept unlimited inputs.

---

# 🔹 1. **Understanding `*args`**

### → Use `*args` when you don't know how many arguments will be passed.

Example:

```python
def add(*args):
    return sum(args)

print(add(1,2,3))
print(add(10,20))
```

**Output**

```
6
30
```

### 📌 `args` becomes a **tuple**:

```
args = (1, 2, 3)
```

---

# 🔹 2. **Understanding `**kwargs`\*\*

### → Use `**kwargs` when you want to accept **named arguments** (key=value)

Example:

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Ali", age=22, city="Karachi")
```

**Output**

```
name: Ali
age: 22
city: Karachi
```

### 📌 `kwargs` becomes a **dictionary**:

```
{'name': 'Ali', 'age': 22, 'city': 'Karachi'}
```

---

# 🔥 3. **Using `*args` and `**kwargs` Together\*\*

```python
def student_data(course, *args, **kwargs):
    print("Course:", course)
    print("Args:", args)
    print("Kwargs:", kwargs)

student_data(
    "Python",
    "Section A",
    "Evening",
    name="Ahmed",
    age=20
)
```

**Output**

```
Course: Python
Args: ('Section A', 'Evening')
Kwargs: {'name': 'Ahmed', 'age': 20}
```

---

# 🔴 RULE: Order Matters

When defining a function:

```
def func(positional, *args, default=None, **kwargs):
    ...
```

Correct order is:

1. Positional arguments
2. `*args`
3. Default parameters
4. `**kwargs`

---

# 🌍 REAL-WORLD USE CASES

---

# ✅ **Use Case 1: Building a Calculator That Accepts Unlimited Numbers**

```python
def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result

print(multiply(2, 3, 4))
```

---

# ✅ **Use Case 2: API / JSON functions (Flexible Options)**

```python
def save_user(**kwargs):
    print("Saving user with data:", kwargs)

save_user(id=10, name="Ali", role="Admin")
```

---

# ✅ **Use Case 3: Passing Arguments to Another Function**

EXTREMELY COMMON IN DJANGO / FLASK / FASTAPI

```python
def wrapper(*args, **kwargs):
    return original_function(*args, **kwargs)
```

This makes decorators possible.

---

# ✅ **Use Case 4: Format Strings Dynamically**

```python
def format_message(**kwargs):
    return "{name} is {age} years old, living in {city}".format(**kwargs)

print(format_message(name="Sara", age=25, city="Lahore"))
```

---

# ✅ **Use Case 5: Dynamic Configurations (Machine Learning / Automation)**

```python
def train_model(**config):
    print("Training with config:", config)

train_model(epochs=10, lr=0.001, batch_size=32)
```

---

# 🔥 **Advanced Example: Mixing All**

```python
def order(item, *extras, **details):
    print("Item:", item)
    print("Extras:", extras)
    print("Details:", details)

order(
    "Burger",
    "Cheese", "Fries",
    size="Large",
    drink="Cola"
)
```

---

# ⭐ Summary (Easy Table)

| Keyword    | Meaning                        | Stored As  |
| ---------- | ------------------------------ | ---------- |
| `*args`    | Unlimited positional arguments | Tuple      |
| `**kwargs` | Unlimited named arguments      | Dictionary |

---
