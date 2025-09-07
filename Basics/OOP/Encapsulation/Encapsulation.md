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

- Balance should not be directly changed (`acc.balance = -999` ❌).
- Instead, use methods like `deposit()` and `withdraw()`.

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

- **Security** → protects data from unauthorized access.
- **Flexibility** → can control how variables are set/changed.
- **Abstraction** → hides unnecessary details.
- **Maintainability** → makes code cleaner and less error-prone.

---

---

## 🟢 Protected in Subclasses

Protected members (`_`) are **directly accessible** in child classes.

```python
class Parent:
    def __init__(self):
        self._protected_var = "I am PROTECTED"

class Child(Parent):
    def show(self):
        # ✅ Accessible directly in subclass
        print("Child accessing:", self._protected_var)


c = Child()
c.show()              # ✅ Child accessing: I am PROTECTED
print(c._protected_var)  # ⚠️ Accessible outside too (but discouraged)
```

👉 **Takeaway**: Protected variables are like "family secrets" → the children can freely use them.

---

## 🔴 Private in Subclasses

Private members (`__`) are **not accessible** directly in child classes (because of name mangling).

```python
class Parent:
    def __init__(self):
        self.__private_var = "I am PRIVATE"

class Child(Parent):
    def show(self):
        try:
            # ❌ Direct access will fail
            print("Child accessing:", self.__private_var)
        except AttributeError:
            print("Child cannot access __private_var")


c = Child()
c.show()

# ⚠️ Can only be accessed with name mangling (not recommended)
print(c._Parent__private_var)  # I am PRIVATE
```

👉 **Takeaway**: Private variables are like "personal diaries" → even children don’t get access unless they **hack it** (via name mangling).

---

## ✅ Summary (Subclass Access)

| Member Type   | Subclass Access                         | Example Output                           |
| ------------- | --------------------------------------- | ---------------------------------------- |
| Protected `_` | ✅ Directly accessible                  | `"I am PROTECTED"`                       |
| Private `__`  | ❌ Not accessible (unless name mangled) | `AttributeError` (unless `_Parent__var`) |

---

⚡ Quick rule of thumb:

- Use `_protected` if you expect subclasses to use/modify it.
- Use `__private` if you want to hide it even from subclasses.
