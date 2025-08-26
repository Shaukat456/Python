
---

# 🔑 **What is Encapsulation?**

* **Encapsulation = wrapping data (variables) and methods (functions) into a single unit (class)**.
* Think of it as a **capsule/medicine capsule**:

  * Inside = medicine (data + methods).
  * Outside = shell (access control).
* It helps us **control access** to class internals.

👉 Encapsulation protects data by restricting how it can be accessed or modified.

---

# 🐍 **Encapsulation in Python**

Python doesn’t have true **private/public keywords** like Java or C++.
Instead, it follows a **naming convention**:

1. **Public Members** → accessible from anywhere.

   ```python
   class Student:
       def __init__(self, name):
           self.name = name   # public variable

   s = Student("Ali")
   print(s.name)  # ✅ accessible
   ```

2. **Protected Members** (convention: `_variable`) → should not be accessed directly (only inside class & subclasses).

   ```python
   class Student:
       def __init__(self, name):
           self._name = name   # protected variable

   s = Student("Ali")
   print(s._name)  # ⚠️ works, but not recommended
   ```

3. **Private Members** (convention: `__variable`) → name-mangled (harder to access).

   ```python
   class Student:
       def __init__(self, name):
           self.__name = name   # private variable

   s = Student("Ali")
   # print(s.__name) ❌ Error
   print(s._Student__name)  # ✅ but possible (not recommended)
   ```

---

# ✨ **Getter & Setter Methods**

We usually use **getter** (to read) and **setter** (to update) methods to safely access private data.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

acc = BankAccount(1000)
print(acc.get_balance())  # 1000
acc.deposit(500)
print(acc.get_balance())  # 1500
acc.withdraw(2000)        # Insufficient funds
```

👉 Here, **balance is hidden**, can only be modified via methods.

---

# 🎯 **Real-World Examples**

### 1. **Bank Account Security**

* Balance should not be directly changed (`acc.balance = -999` ❌).
* Instead, use methods like `deposit()` and `withdraw()`.

---

### 2. **Physics (Encapsulation of a Particle System)**

```python
import numpy as np

class Particle:
    def __init__(self, position, velocity):
        self.__position = np.array(position)   # private
        self.__velocity = np.array(velocity)   # private

    def get_position(self):
        return self.__position

    def update(self, dt):
        self.__position += self.__velocity * dt

p = Particle([0,0], [1,1])
print("Initial:", p.get_position())
p.update(2)
print("After 2s:", p.get_position())
```

👉 Position & velocity are **hidden** from direct modification. Updates happen only through methods.

---

# ✅ **Why Encapsulation is Important?**

* **Security** → protects data from unauthorized access.
* **Flexibility** → can control how variables are set/changed.
* **Abstraction** → hides unnecessary details.
* **Maintainability** → makes code cleaner and less error-prone.

---

