---
# 🎯 1. What is an Interface?

An **interface** is like a **contract**:
  - It **defines what methods a class must have**, but **doesn’t say how to implement them**.
  - Any class that "signs" this contract is **obliged** to implement those methods.

👉 Think of an interface as a **promise**:
  - _"If you want to call yourself a PaymentGateway, you must have `pay()` and `refund()`."_
---

# 🛠 2. Interfaces in Python

⚠️ Python doesn’t have a built-in `interface` keyword (like Java or C#).
Instead, we achieve interfaces using **abstract base classes (ABC)** with **only abstract methods**.

👉 An **interface = abstract class with no concrete methods**.

---

# 🔑 3. Example: Payment System

```python
from abc import ABC, abstractmethod

# Interface (contract)
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


# Implementing classes
class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"💻 Paid {amount} via PayPal")

    def refund(self, amount):
        print(f"💻 Refunded {amount} via PayPal")


class Stripe(PaymentGateway):
    def pay(self, amount):
        print(f"💳 Paid {amount} via Stripe")

    def refund(self, amount):
        print(f"💳 Refunded {amount} via Stripe")


# Client code works with interface, not implementation
def process_payment(payment: PaymentGateway, amount):
    payment.pay(amount)
    payment.refund(amount)

process_payment(PayPal(), 200)
process_payment(Stripe(), 500)
```

👉 Output:

```
💻 Paid 200 via PayPal
💻 Refunded 200 via PayPal
💳 Paid 500 via Stripe
💳 Refunded 500 via Stripe
```

Notice:

- The client (`process_payment`) doesn’t care whether it’s PayPal or Stripe.
- It only depends on the **interface (PaymentGateway)**.

---

# 🎭 4. Real-World Analogy

💡 Think of **USB ports**:

- The **USB standard (interface)** says: "Any USB device must have `plug_in()` and `transfer_data()`".
- Whether it’s a **keyboard, mouse, or flash drive**, they all must follow that contract.
- Your computer doesn’t care _how_ the device works internally, just that it provides the required methods.

👉 That’s exactly what interfaces do.

---

# 🔄 5. Multiple Interfaces in Python

A class can implement multiple interfaces by inheriting from multiple abstract base classes.

```python
class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass

class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, user, password):
        pass

# Implements both interfaces
class SecureApp(Logger, Authenticator):
    def log(self, msg):
        print("Log:", msg)

    def authenticate(self, user, password):
        print(f"Authenticating {user}... ✅")

app = SecureApp()
app.log("User login")
app.authenticate("Ali", "1234")
```

---

# 🔍 6. Duck Typing vs Interfaces

Python is **dynamically typed**, so often you don’t need strict interfaces.

👉 Example (duck typing, no abstract class):

```python
class PayPal:
    def pay(self, amount):
        print(f"Paid {amount} via PayPal")

class Stripe:
    def pay(self, amount):
        print(f"Paid {amount} via Stripe")

def process_payment(payment, amount):
    payment.pay(amount)   # Works as long as object has a pay() method

process_payment(PayPal(), 100)
process_payment(Stripe(), 200)
```

⚡ This works without an interface because of **duck typing**:

> "If it looks like a duck and quacks like a duck, it’s a duck."

But in **large systems**, interfaces give **clarity, consistency, and safety**.

---

# ✅ 7. Why Use Interfaces?

1. **Consistency** → Every implementation class must follow the same rules.
2. **Decoupling** → Client code depends on interface, not specific implementation.
3. **Flexibility** → Swap one implementation for another easily (e.g., PayPal → Stripe).
4. **Testability** → You can pass in mock objects that follow the interface.

---

# 📌 Summary

- **Interface = Contract (only method signatures, no implementation).**
- In Python → Achieved via abstract base classes with only abstract methods.
- Classes that implement the interface must define those methods.
- Useful for consistency, flexibility, and clean architecture.

---

# 🎭 1. Abstract Classes vs Interfaces (Big Picture)

Both **abstract classes** and **interfaces** are used for **abstraction**, but they differ in purpose:

| Feature                      | Abstract Class                                                                        | Interface                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Purpose**                  | To provide a base class with shared code + rules                                      | To provide only rules (contract), no implementation                                    |
| **Can have implementation?** | ✅ Yes (regular methods, variables, constructors)                                     | ❌ No (only method signatures)                                                         |
| **Multiple inheritance?**    | 🚫 Usually only single inheritance (Python allows multiple though)                    | ✅ Multiple interfaces can be implemented                                              |
| **When to use?**             | When you want to share common code and force subclasses to implement specific methods | When you just want to enforce a “must-do” contract without caring about implementation |
| **Analogy**                  | A **template** → Some parts ready-made, some parts left for you to fill               | A **promise** → "Whoever signs must do these tasks"                                    |

---

# 🟢 2. Abstract Class in Python

We’ve already seen — it’s a class that can have:

- **abstract methods** (must be implemented by subclasses).
- **concrete methods** (already implemented).
- **instance variables, constructors, properties**.

Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass

    def info(self):  # concrete method
        print(f"This is a {self.brand} vehicle.")

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} car engine started 🚗")

car = Car("Toyota")
car.start_engine()
car.info()
```

👉 Here, `Car` gets both **enforced rules** (`start_engine`) and **ready-made functionality** (`info()`).

---

# 🔴 3. Interface in Python

⚠️ Python doesn’t have a dedicated `interface` keyword like Java or C#.
Instead:

- We simulate interfaces using **abstract classes with only abstract methods**.
- Or sometimes, with **duck typing** (any object with required methods is acceptable).

Example (pure interface-like abstract class):

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):   # acts like an interface
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"💻 Paid {amount} using PayPal")

    def refund(self, amount):
        print(f"💻 Refunded {amount} via PayPal")


class Stripe(PaymentGateway):
    def pay(self, amount):
        print(f"💳 Paid {amount} using Stripe")

    def refund(self, amount):
        print(f"💳 Refunded {amount} via Stripe")
```

👉 `PaymentGateway` acts as a **contract** — all payment providers **must** implement `pay()` and `refund()`.

---

# 🛠 4. Multiple Interfaces in Python

In Python, classes can inherit from multiple abstract base classes → simulating multiple interfaces.

```python
class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass

class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, user, password):
        pass

class SecureApp(Logger, Authenticator):  # multiple interfaces
    def log(self, msg):
        print("Log:", msg)

    def authenticate(self, user, password):
        print(f"Authenticating {user}... ✅")

app = SecureApp()
app.log("User login")
app.authenticate("Ali", "1234")
```

---

# 🧩 5. Real-World Analogy

- **Abstract Class (Template)**
  Imagine a **base smartphone design**:

  - Already has a touchscreen, battery, speakers (concrete features).
  - Requires brands (Samsung, iPhone) to add camera technology (abstract features).

- **Interface (Contract)**
  Think of a **charger standard (USB-C, Lightning)**:

  - Any device implementing this must provide `plug_in()` and `supply_power()`.
  - The standard does not say how the device is built, just that these methods exist.

---

# ✅ 6. When to Use What?

- **Use Abstract Class** when:

  - You want to **share code** among related classes.
  - You want a **partial implementation** + rules.
  - Example: `Vehicle` → All vehicles have wheels, but `start_engine()` differs.

- **Use Interface** when:

  - You just want to **enforce rules**, with no shared implementation.
  - You want to allow **multiple unrelated classes** to implement the same contract.
  - Example: `PaymentGateway` → PayPal, Stripe, BankTransfer all must implement `pay()` and `refund()`.

---

# ⚡ 7. Key Summary

- **Abstract Class** = Mix of **rules + ready-made code**.
- **Interface** = **Only rules**, no implementation.
- Python doesn’t have a strict `interface` keyword → we use abstract base classes for both roles.
- Interfaces = "must-do", Abstract Classes = "must-do + already-done".
