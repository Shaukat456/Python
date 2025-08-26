
---

# 🎀 **Python Decorators**

## 🔹 What is a Decorator?

* A **function that takes another function as input and adds extra functionality** without modifying its actual code.
* Uses the **`@` symbol** in Python.
* Promotes **reusability** and follows the **DRY principle**.

---

## 🎯 **Real-World Analogy**

Think of a **pizza 🍕 shop**:

* Base pizza = plain cheese pizza (original function).
* Toppings = decorators (extra functionality).
* You don’t change the original pizza recipe, you just **add layers** on top.

👉 Similarly, decorators **wrap** a function to add extra features.

---

## 🖥️ **Basic Example**

```python
def decorator_function(func):
    def wrapper():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper

@decorator_function
def say_hello():
    print("Hello, World!")

say_hello()
```

✅ **Output:**

```
Before the function runs...
Hello, World!
After the function runs...
```

---

## 🔑 **Why Use Decorators?**

* Logging 📜
* Authentication 🔑
* Measuring performance ⏱️
* Access control 🔒
* Code reusability 🔁

---

# ⚡ **Real-World Use Cases**

### 1️⃣ **Logging**

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} ended")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 10))
```

✅ Output:

```
Function add started
Function add ended
15
```

---

### 2️⃣ **Authentication (Web App Example)**

```python
def login_required(func):
    def wrapper(user):
        if user.get("is_authenticated"):
            return func(user)
        else:
            print("Access Denied! Please log in.")
    return wrapper

@login_required
def view_dashboard(user):
    print(f"Welcome {user['name']} to your dashboard!")

# Test
user1 = {"name": "Ali", "is_authenticated": True}
user2 = {"name": "Sara", "is_authenticated": False}

view_dashboard(user1)
view_dashboard(user2)
```

✅ Output:

```
Welcome Ali to your dashboard!
Access Denied! Please log in.
```

---

### 3️⃣ **Performance Monitoring**

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def compute():
    time.sleep(2)
    print("Computation finished!")

compute()
```

✅ Output:

```
Computation finished!
compute took 2.0005 seconds
```

---

# 🔀 **Decorators with Arguments**

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Shaukat")
```

✅ Output:

```
Hello, Shaukat!
Hello, Shaukat!
Hello, Shaukat!
```

---

# 🧵 **Decorators in OOP (Class Example)**

```python
def method_logger(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @method_logger
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 7))
```

✅ Output:

```
Calling method add
10
```

---

✅ So decorators = "wrappers" around functions/methods to add extra features **without changing the original code**.
This concept is **found everywhere in Python frameworks** (Flask, Django, FastAPI use them a LOT).

---

