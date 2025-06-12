# **Python Decorators (With Real-World Analogies & Examples)**

## **What is a Decorator?**
# A **decorator** in Python is a **special function** that allows you to **modify or extend the behavior** of another function **without changing its actual code**.

# ✅ **Key Idea:** A function is **wrapped inside another function** to modify its behavior.

# ---

## **Real-World Analogy: A Cake with Different Toppings 🍰**
# Imagine you have a **plain cake** 🎂.
# - You can **decorate** it with **chocolate**, **sprinkles**, or **fruit toppings** **without changing the cake itself**.
# - The **cake remains the same**, but its appearance and taste **change** depending on the decoration.

# Similarly, in Python, a **decorator modifies a function's behavior without altering its original code.**

# ---

## **Basic Structure of a Decorator**
# A decorator is a function that **takes another function as an argument, adds some behavior, and returns the modified function.**

### **Example: A Simple Decorator**


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function runs.")
        func()  # Calling the original function
        print("Something is happening after the function runs.")

    return wrapper


@my_decorator  # Using the decorator
def say_hello():
    print("Hello, World!")


say_hello()

# ### **Output:**
#
# Something is happening before the function runs.
# Hello, World!
# Something is happening after the function runs.
#
# **Explanation:**
# 1. `say_hello()` function is wrapped inside `my_decorator()`.
# 2. The `wrapper()` function **modifies** the behavior of `say_hello()` by adding extra prints **before and after** execution.
# 3. The `@my_decorator` is shorthand for writing `say_hello = my_decorator(say_hello)`.

# ---

## **Types of Decorators in Python**
### **1️⃣ Function Decorators (Basic Use Case)**
# Function decorators are commonly used to **add extra functionality** like **logging, authentication, and timing**.

#### **Example: Logging Function Calls**


def log_decorator(func):
    def wrapper():
        print(f"Function {func.__name__} is about to run...")
        func()
        print(f"Function {func.__name__} has finished running.")

    return wrapper


@log_decorator
def greet():
    print("Hello!")


greet()

# ### **Output:**
#
# Function greet is about to run...
# Hello!
# Function greet has finished running.
#
# ✅ **Use Case:** Useful for debugging when you want to track which functions are called.

# ---

### **2️⃣ Decorators with Arguments**
# If the original function takes arguments, we must allow the decorator to **handle them dynamically using `*args` and `**kwargs`**.

#### **Example: Timing a Function Execution**

import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call original function
        end_time = time.time()  # Record end time
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to execute.")
        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)
    print("Finished running!")


slow_function()

# ### **Output:**
#
# Finished running!
# slow_function took 2.00023 seconds to execute.
#
# ✅ **Use Case:** Useful for **performance monitoring** in apps or APIs.

# ---

### **3️⃣ Multiple Decorators (Stacking Decorators)**
# You can apply multiple decorators to a single function by **stacking them**.

#### **Example: Logging & Timing a Function**


@log_decorator
@timing_decorator
def compute():
    time.sleep(1)
    print("Computing done!")


compute()

# ### **Execution Order:**
# 1. `timing_decorator` runs first (because it's closest to the function).
# 2. `log_decorator` wraps around the timing output.

# ---

### **4️⃣ Class-Based Decorators**
# Instead of using functions, we can create decorators using **classes** with the `__call__` method.

#### **Example: Counting Function Calls**


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0  # Track number of calls

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times.")
        return self.func(*args, **kwargs)


@CountCalls
def hello():
    print("Hello!")


hello()
hello()

# ### **Output:**
#
# hello has been called 1 times.
# Hello!
# hello has been called 2 times.
# Hello!
#
# ✅ **Use Case:** Useful for **tracking API requests or function usage** in a system.

# ---

## **Real-World Use Cases of Decorators**
# ✅ **1. Authentication in Web Apps**


def require_login(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            print("Access Denied! Please log in.")
            return
        return func(user)

    return wrapper


@require_login
def dashboard(user):
    print(f"Welcome {user['name']} to your dashboard!")


# Simulating users
user1 = {"name": "Alice", "is_logged_in": True}
user2 = {"name": "Bob", "is_logged_in": False}

dashboard(user1)  # Works
dashboard(user2)  # Access Denied!


# ✅ **2. Caching Expensive Function Calls (Memoization)**


def cache_decorator(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            print("Fetching from cache...")
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Fast computation with caching


# ✅ **3. Rate Limiting API Calls**

import time


def rate_limiter(func):
    last_called = [0]  # Using a list to store last call time

    def wrapper():
        now = time.time()
        if now - last_called[0] < 5:  # Limit: 5 seconds between calls
            print("Too many requests! Slow down.")
            return
        last_called[0] = now
        return func()

    return wrapper


@rate_limiter
def fetch_data():
    print("Fetching data from API...")


fetch_data()
fetch_data()  # Too soon, will be blocked


# ---

## **Summary**
# | **Concept**          | **Explanation** | **Example Use Case** |
# |----------------------|----------------|----------------------|
# | **Function Decorator** | Modifies behavior of a function | Logging function calls |
# | **Decorator with Arguments** | Allows functions with parameters | Measuring execution time |
# | **Multiple Decorators** | Stacking multiple behaviors | Logging & timing together |
# | **Class-Based Decorator** | Uses a class instead of a function | Counting API requests |
# | **Real-World Use Cases** | Authentication, caching, rate-limiting | Web apps, APIs, ML models |

# 🚀 **Decorators are powerful tools that allow Python developers to write cleaner, reusable, and more maintainable code.**
