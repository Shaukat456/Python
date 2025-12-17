---
---

# 📦 **Modules in Python**

### 👉 **A module is a file that contains Python code**

Functions, variables, and classes can all live inside a module.

## Think of modules like **toolboxes** 🧰 — each toolbox contains tools for a specific task.

## 🔹 1. **Why Use Modules?**

✅ Code reusability
✅ Better organization
✅ Easier maintenance
✅ Cleaner, readable programs

---

# 🔹 2. **Using Built-in Modules**

Python already comes with many useful modules.

### Example: `math` module

```python
import math

print(math.sqrt(16))
print(math.pi)
```

---

### Example: Import only what you need

```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

---

### Example: Rename a module (alias)

```python
import math as m

print(m.factorial(5))
```

---

# 🔹 3. **Creating Your Own Module**

### Step 1: Create a file

📄 `calculator.py`

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

---

### Step 2: Use it in another file

📄 `main.py`

```python
import calculator

print(calculator.add(5, 3))
print(calculator.sub(10, 4))
```

---

# 🔹 4. **Import Specific Functions**

```python
from calculator import add

print(add(2, 3))
```

⚠️ Avoid importing everything:

```python
from calculator import *   # ❌ Not recommended
```

---

# 🔹 5. **`__name__ == "__main__"` (Very Important)**

This prevents code from running when the module is imported.

### Example:

```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()
```

✔ Runs only when file is executed directly
❌ Does NOT run when imported

---

# 🔹 6. **Popular Built-in Modules (Must Know)**

| Module     | Use                      |
| ---------- | ------------------------ |
| `math`     | Mathematical operations  |
| `random`   | Random numbers           |
| `datetime` | Date & time              |
| `os`       | File & system operations |
| `sys`      | Python system info       |
| `json`     | Work with JSON data      |

---

# 🌍 REAL-WORLD USE CASES

---

## ✅ **Use Case 1: Random OTP Generator**

```python
import random

otp = random.randint(1000, 9999)
print("Your OTP:", otp)
```

---

## ✅ **Use Case 2: Working With Dates**

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%d-%m-%Y %H:%M"))
```

---

## ✅ **Use Case 3: File Handling (OS Module)**

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
```

---

## ✅ **Use Case 4: JSON (API Responses)**

```python
import json

data = '{"name":"Ali","age":22}'
user = json.loads(data)
print(user["name"])
```

---

## ✅ **Use Case 5: Custom Utility Module (Best Practice)**

📄 `utils.py`

```python
def is_even(n):
    return n % 2 == 0
```

📄 `main.py`

```python
from utils import is_even

print(is_even(10))
```

---

# 🔥 7. **Module Search Path (`sys.path`)**

Python looks for modules in:

1️⃣ Current directory
2️⃣ Standard library
3️⃣ Site-packages

```python
import sys
print(sys.path)
```

---

# ⭐ Summary

| Concept         | Example                     |
| --------------- | --------------------------- |
| Import module   | `import math`               |
| Import function | `from math import sqrt`     |
| Alias           | `import numpy as np`        |
| Custom module   | `calculator.py`             |
| Main guard      | `if __name__ == "__main__"` |

---

Perfect 👍
Let’s continue **step-by-step**, exactly in the order you listed, in a **beginner → practical** way.

---

# 📦 1️⃣ **Modules vs Packages (Very Important)**

## 🔹 What is a Module?

A **module** is **one Python file**.

```
math.py
calculator.py
utils.py
```

Example:

```python
# calculator.py
def add(a, b):
    return a + b
```

---

## 🔹 What is a Package?

A **package** is a **folder** that contains **multiple modules** and a special file:

```
my_package/
│
├── __init__.py
├── math_ops.py
├── string_ops.py
```

### Example structure:

```
project/
│
├── main.py
└── my_package/
    ├── __init__.py
    ├── calculator.py
    └── helpers.py
```

### Import from package:

```python
from my_package.calculator import add
```

---

### 🔑 Difference Summary

| Module              | Package        |
| ------------------- | -------------- |
| Single `.py` file   | Folder         |
| Small functionality | Large projects |
| Easy                | Organized      |

---

# 🧪 2️⃣ **Virtual Environments (venv)**

## 🔹 What is a Virtual Environment?

A **virtual environment** is an **isolated Python setup** for a project.

👉 Prevents library version conflicts.

---

## 🔹 Create Virtual Environment

### Windows:

```bash
python -m venv venv
```

### Activate:

```bash
venv\Scripts\activate
```

### Linux / Mac:

```bash
source venv/bin/activate
```

### Deactivate:

```bash
deactivate
```

---

## 🔹 Why venv is Important?

Without venv:
❌ All projects share libraries
❌ Version conflicts

With venv:
✅ Each project has its own libraries
✅ Safe & professional

---

# 📥 3️⃣ **pip – Installing Libraries**

## 🔹 What is pip?

`pip` is Python’s **package manager**.

---

## 🔹 Common pip Commands

### Install library:

```bash
pip install requests
```

### Install specific version:

```bash
pip install django==4.2
```

### Upgrade library:

```bash
pip install --upgrade pip
```

### Uninstall:

```bash
pip uninstall requests
```

---

## 🔹 `requirements.txt` (Very Important)

### Create file:

```bash
pip freeze > requirements.txt
```

### Install from file:

```bash
pip install -r requirements.txt
```

Used in:
✔ Team projects
✔ Deployment
✔ Production

---

# 🏗️ 4️⃣ **Writing Reusable Python Projects**

## 🔹 Recommended Project Structure

```
my_project/
│
├── venv/
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── services/
│       ├── __init__.py
│       └── user_service.py
```

---

## 🔹 Example: Reusable Function

📄 `utils.py`

```python
def format_name(name):
    return name.title()
```

📄 `main.py`

```python
from utils import format_name

print(format_name("ali"))
```

---

## 🔹 Use `__main__` Guard

```python
def run():
    print("App running")

if __name__ == "__main__":
    run()
```

✔ Prevents auto execution
✔ Makes code reusable

---

# 🌍 REAL-WORLD MINI PROJECT EXAMPLE

### 📁 Email Validator Package

```
email_tool/
│
├── validator.py
├── __init__.py
```

```python
# validator.py
def is_valid(email):
    return "@" in email and "." in email
```

Usage:

```python
from email_tool.validator import is_valid

print(is_valid("test@gmail.com"))
```

---

# ⭐ Final Summary

| Topic             | Purpose              |
| ----------------- | -------------------- |
| Module            | Single functionality |
| Package           | Group of modules     |
| venv              | Isolated environment |
| pip               | Install libraries    |
| requirements.txt  | Dependency list      |
| Project structure | Clean & reusable     |

---
