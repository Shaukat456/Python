---
# 🎭 1. What is Abstraction?

👉 **Abstraction** means **hiding implementation details** and showing only the **essential features**.

- Users care about _what something does_, not _how it does it_.
- In Python → achieved using **abstract classes** and **abstract methods** (`abc` module).
---

# 🏦 2. Real-World Analogies

- **ATM**: You withdraw cash without knowing the internal banking logic.
- **Car**: You press the brake; you don’t care whether it’s hydraulic, ABS, or electric braking.
- **Phone Apps**: You tap "send message"; you don’t see the TCP/IP networking behind it.

👉 In all cases, **complexity is hidden**, only essentials are exposed.

---

# 🟢 3. Abstraction in Python

Implemented using **abstract base classes (ABC)**.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract class
    @abstractmethod
    def start_engine(self):  # Abstract method
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started 🚗")

    def stop_engine(self):
        print("Car engine stopped 🛑")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started 🏍️")

    def stop_engine(self):
        print("Bike engine stopped 🛑")


# ✅ Polymorphism + Abstraction
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start_engine()
    v.stop_engine()
```

⚠️ You **cannot instantiate** an abstract class:

```python
v = Vehicle()  # ❌ Error
```

---

# 🔑 4. Why Use Abstraction?

1. **Hides complexity** – user doesn’t see messy details.
2. **Enforces rules** – all subclasses must implement certain methods.
3. **Improves maintainability** – internal changes don’t affect user code.
4. **Supports polymorphism** – different classes can be used interchangeably.

---

# 🛠 5. Example: Payment System

All payment methods must follow the same structure.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"💳 Paid {amount} using Credit Card.")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"💻 Paid {amount} using PayPal.")


def checkout(payment_method: Payment, amount):
    payment_method.pay(amount)


checkout(CreditCardPayment(), 500)
checkout(PayPalPayment(), 300)
```

👉 The system doesn’t care **how** payment is made, only that `.pay()` exists.

---

# 🔐 6. Abstraction vs Encapsulation

Many mix these up. Let’s clarify 👇

| Feature         | Abstraction                                        | Encapsulation                                            |
| --------------- | -------------------------------------------------- | -------------------------------------------------------- |
| **Definition**  | Hides implementation, shows only features          | Hides data by restricting direct access                  |
| **Focus**       | _What a class does_                                | _How data is controlled_                                 |
| **Achieved by** | Abstract classes & methods (`abc`)                 | Access modifiers (`public`, `_protected`, `__private`)   |
| **User sees**   | Only functionality (e.g., `deposit`)               | Only safe access to data (`getter/setter`)               |
| **Analogy**     | Car brake pedal (you press, car stops, no details) | Car engine under hood (hidden, you can’t touch directly) |

---

# 🧩 7. Example Showing Both Together

```python
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # encapsulated (private)

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # encapsulation: controlled access
    def get_balance(self):
        return self.__balance

    def _set_balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("❌ Balance cannot be negative!")


class SavingsAccount(Account):
    def deposit(self, amount):
        self._set_balance(self.get_balance() + amount)
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}")
        else:
            print("❌ Insufficient funds")


# ✅ Using abstraction + encapsulation
acc = SavingsAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())   # ✅ 1300
```

👉 Here:

- **Abstraction** → `deposit` & `withdraw` are required in all accounts.
- **Encapsulation** → balance is private, only accessed via methods.

---

# 🧠 8. How Abstraction Connects with Other OOP Concepts

1. **Abstraction + Encapsulation**

   - Abstraction → hides _implementation_
   - Encapsulation → hides _data_

2. **Abstraction + Inheritance**

   - Abstract class defines the **contract**
   - Subclasses inherit and provide specific implementations

3. **Abstraction + Polymorphism**

   - Different subclasses can be used interchangeably
   - Example: `Vehicle` → `Car`, `Bike`, `Bus` all implement `.start_engine()` differently

---

# 🛠 9. Advanced: Abstract Properties & Abstract Static Methods

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(5)
print(circle.area)   # ✅ 78.5
```

👉 You can even enforce subclasses to define **properties**.

---

# ✅ 10. Final Takeaway

- **Abstraction** = Hiding implementation details, showing only essentials.
- Achieved with **abstract classes/methods**.
- Makes code **cleaner, more maintainable, and consistent**.
- Works best with **encapsulation, inheritance, and polymorphism**.

---
