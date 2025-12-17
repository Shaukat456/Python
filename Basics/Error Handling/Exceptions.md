---
---

# ⏱️ **Compile Time vs Runtime**

## 🔹 What is Compile Time?

**Compile time** is the phase when **code is translated** (compiled) **before execution**.

👉 Errors found here are called **compile-time errors**.

### Happens:

- Before program runs
- While converting source code → machine/byte code

---

## 🔹 What is Runtime?

**Runtime** is the phase when the **program is actually executing**.

👉 Errors found here are called **runtime errors (exceptions)**.

---

# 🧠 Important Python Note (Very Important)

Python is an **interpreted language**, not fully compiled like C/C++.

✔ Python **compiles to bytecode first**, then runs
✔ Many errors appear **at runtime**, not compile time

So in Python:

- **Syntax errors** → compile time
- **Exceptions** → runtime

---

# 🔴 COMPILE-TIME ERRORS

### ❌ Syntax Error (Python example)

```python
if True
    print("Hello")
```

❌ Missing colon → detected **before execution**

---

### ❌ Indentation Error

```python
def test():
print("Hi")
```

---

### ❌ Name Errors (sometimes detected early)

```python
print(x)
```

---

# 🔵 RUNTIME ERRORS (EXCEPTIONS)

### ❌ Divide by zero

```python
print(10 / 0)
```

---

### ❌ Wrong input type

```python
x = int("abc")
```

---

### ❌ File not found

```python
open("missing.txt")
```

---

# 🌍 REAL-WORLD ANALOGY

### 🏗️ Compile Time = **Building inspection**

- Blueprints checked
- Structural mistakes found
- Building not used yet

### 🚗 Runtime = **Driving the car**

- Engine failure
- Flat tire
- Accident during driving

---

# 🧠 COMPARISON TABLE

| Feature        | Compile Time        | Runtime                |
| -------------- | ------------------- | ---------------------- |
| When           | Before execution    | During execution       |
| Errors         | Syntax, indentation | Exceptions             |
| Python Example | `SyntaxError`       | `ZeroDivisionError`    |
| Fix needed     | Code structure      | Logic / input handling |
| Detected       | Early               | While program runs     |

---

# 🔥 Language Comparison (Extra Knowledge)

| Language | Compile Time Errors | Runtime Errors |
| -------- | ------------------- | -------------- |
| C / C++  | Very strict         | Fewer          |
| Java     | Many                | Many           |
| Python   | Few                 | Many           |

---

# ⭐ Interview One-Liner

> **Compile-time errors are detected before program execution, while runtime errors occur during program execution.**

---

# 🚨 **Error Handling in Python**

## Error handling lets your program **handle crashes gracefully** instead of stopping suddenly.

## 🔹 1️⃣ Types of Errors

### ❌ **Syntax Error** (code won’t run)

```python
if True
    print("Hello")
```

---

### ❌ **Runtime Error (Exception)** (program crashes while running)

```python
print(10 / 0)   # ZeroDivisionError
```

---

# 🔹 2️⃣ What is an Exception?

An **exception** is an error that occurs **during execution**.

Common exceptions:

| Exception           | Cause                   |
| ------------------- | ----------------------- |
| `ZeroDivisionError` | Divide by zero          |
| `ValueError`        | Wrong value type        |
| `TypeError`         | Wrong data type         |
| `IndexError`        | List index out of range |
| `KeyError`          | Missing dictionary key  |
| `FileNotFoundError` | File not found          |

---

# 🔹 3️⃣ Basic `try` – `except`

### ❌ Without error handling

```python
x = int(input("Enter number: "))
print(10 / x)
```

### ✅ With error handling

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Something went wrong")
```

✔ Program doesn’t crash
✔ Error handled safely

---

# 🔹 4️⃣ Catching Specific Errors (BEST PRACTICE)

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 🔹 5️⃣ `else` Block

Runs **only if no error occurs**.

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except Exception as e:
    print("Error:", e)
else:
    print("Calculation successful")
```

---

# 🔹 6️⃣ `finally` Block

Runs **no matter what** (error or not).

```python
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
```

✔ Used for cleanup (files, DB connections)

---

# 🔹 7️⃣ Handling Multiple Exceptions Together

```python
try:
    x = int(input())
    y = int(input())
    print(x / y)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```

---

# 🔹 8️⃣ Raising Your Own Exceptions (`raise`)

### Example: Age validation

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

print(check_age(20))
```

---

# 🔹 9️⃣ Custom Exceptions (ADVANCED)

```python
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    return balance - amount

print(withdraw(1000, 1500))
```

---

# 🌍 REAL-WORLD USE CASES

---

## ✅ Use Case 1: User Login Input

```python
try:
    password = input("Enter password: ")
    if len(password) < 6:
        raise ValueError("Password too short")
except ValueError as e:
    print(e)
```

---

## ✅ Use Case 2: API Data Parsing

```python
data = {"name": "Ali"}

try:
    print(data["age"])
except KeyError:
    print("Age field missing")
```

---

## ✅ Use Case 3: File Handling

```python
try:
    with open("data.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

---

## 🔥 Best Practices (IMPORTANT)

✔ Catch **specific exceptions**
✔ Don’t use empty `except:`
✔ Use `finally` for cleanup
✔ Raise meaningful errors
✔ Don’t hide bugs

---

# ⭐ Summary

| Keyword   | Purpose            |
| --------- | ------------------ |
| `try`     | Code that may fail |
| `except`  | Handle error       |
| `else`    | Runs if no error   |
| `finally` | Always runs        |
| `raise`   | Throw error        |

---
