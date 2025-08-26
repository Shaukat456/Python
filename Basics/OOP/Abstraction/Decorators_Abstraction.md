# 🎯 Decorators + Abstraction in Python

### 🔹 Recap

- **Abstraction** = hiding implementation details, showing only necessary features (like an interface in Java/C++).
- **Decorators** = wrapping functions/methods to add extra behavior without modifying their core code.

👉 When combined, they help us **enforce rules** + **add cross-cutting features** (logging, validation, security) in abstract designs.

---

## 🧾 **Example 1: Abstract Class with Decorators (Bank System)**

```python
from abc import ABC, abstractmethod

# Decorator for logging
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Running {func.__name__} ...")
        return func(*args, **kwargs)
    return wrapper

# Abstract class
class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Concrete class
class SavingsAccount(BankAccount):

    def __init__(self, balance=0):
        self.balance = balance

    @log_action
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance = {self.balance}")

    @log_action
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}, Remaining Balance = {self.balance}")
        else:
            print("Insufficient Balance!")
```

### ✅ Usage

```python
acc = SavingsAccount(100)
acc.deposit(50)
acc.withdraw(70)
```

### 🔎 Output

```
LOG: Running deposit ...
Deposited 50, New Balance = 150
LOG: Running withdraw ...
Withdrew 70, Remaining Balance = 80
```

📌 **What happened?**

- `BankAccount` is **abstract** → forces every account type to have `deposit` and `withdraw`.
- `@log_action` decorator adds logging without touching business logic.

---

## 🧾 **Example 2: Quantum Experiment Simulation (Physics)**

Imagine we design a system for **quantum experiments** where each experiment must implement `run()` but we want to **time** how long each takes.

```python
from abc import ABC, abstractmethod
import time

# Decorator for timing
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

# Abstract Base Class
class QuantumExperiment(ABC):

    @abstractmethod
    def run(self):
        pass

# Concrete Class
class QuantumRandomNumberGen(QuantumExperiment):

    @timer
    def run(self):
        print("Generating quantum random numbers...")
        time.sleep(2)   # simulating hardware delay
        print("Numbers generated!")
```

### ✅ Usage

```python
exp = QuantumRandomNumberGen()
exp.run()
```

### 🔎 Output

```
Generating quantum random numbers...
Numbers generated!
run took 2.0002 seconds
```

📌 **What happened?**

- Abstraction (`QuantumExperiment`) enforces that **every experiment must have a `run()` method**.
- Decorator (`@timer`) ensures we also **measure execution time** for all experiments.

---

## 🧾 **Example 3: Enforcing Authentication in Abstract Web Services**

```python
from abc import ABC, abstractmethod

def auth_required(func):
    def wrapper(self, user, *args, **kwargs):
        if not user.get("is_authenticated", False):
            print("❌ Access Denied! Login required.")
            return
        return func(self, user, *args, **kwargs)
    return wrapper

class WebService(ABC):

    @abstractmethod
    def serve(self, user):
        pass

class DashboardService(WebService):

    @auth_required
    def serve(self, user):
        print(f"✅ Serving dashboard to {user['name']}")
```

✅ Usage:

```python
user1 = {"name": "Ali", "is_authenticated": True}
user2 = {"name": "Sara", "is_authenticated": False}

service = DashboardService()
service.serve(user1)
service.serve(user2)
```

✅ Output:

```
✅ Serving dashboard to Ali
❌ Access Denied! Login required.
```

---

# 🔑 Key Takeaways

- **Abstraction** enforces a contract → "Every child class must implement these methods."
- **Decorators** add features like:

  - Logging
  - Authentication
  - Performance timing
  - Error handling

👉 Together, they make your code **clean, scalable, and real-world ready** (like in **Django/Flask**, abstract base views + decorators are everywhere).
