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

Great question 👍 Let’s unpack **why we need getter and setter functions** in Python with examples + analogies.

---

## 🔑 What are Getters and Setters?

- **Getter** → A method that **retrieves (gets)** the value of a variable.
- **Setter** → A method that **updates (sets)** the value of a variable.

They are used when we want to **control access** to variables instead of allowing direct access.

---

## 🟢 Why not just access variables directly?

In Python, you _can_ directly access variables:

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Ali", 85)
print(s.grade)   # ✅ Direct access
s.grade = 120    # ❌ Invalid grade (no validation!)
print(s.grade)   # 120 (nonsense!)
```

⚠️ Problem: The `grade` got set to `120`, which is not realistic (grades should be between 0–100).

---

## 🔴 Why use Getter & Setter?

1. **Validation** – Ensure values are correct.
2. **Encapsulation** – Hide internal details from outside users.
3. **Read-only / Write-only** – Control whether a variable can only be read or updated.
4. **Future-proofing** – You can change how data is stored internally without breaking user code.

---

## 🏫 Example with Getter and Setter

```python
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = None
        self.set_grade(grade)   # use setter for validation

    # Getter
    def get_grade(self):
        return self.__grade

    # Setter (with validation)
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade! Must be between 0 and 100.")


s = Student("Ali", 85)
print(s.get_grade())   # ✅ 85

s.set_grade(95)        # ✅ Valid update
print(s.get_grade())   # 95

s.set_grade(120)       # ❌ Invalid grade
print(s.get_grade())   # still 95
```

👉 Now the student’s grade is **protected from nonsense values**.

---

## 🛠 Real-World Analogy

- Think of a **TV remote**.

  - You don’t directly fiddle with wires inside the TV (private variable).
  - Instead, you use **buttons (getter & setter)** to change channels or volume.
  - This ensures you don’t break the TV by sending invalid signals.

---

## ⚡ Pythonic Way: `@property` (Cleaner Getters & Setters)

Instead of writing separate `get_` and `set_` functions, Python gives us the `@property` decorator:

```python
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.grade = grade   # calls setter

    @property
    def grade(self):       # Getter
        return self.__grade

    @grade.setter
    def grade(self, value):   # Setter
        if 0 <= value <= 100:
            self.__grade = value
        else:
            raise ValueError("Grade must be between 0 and 100")


s = Student("Ali", 85)
print(s.grade)   # ✅ Calls getter → 85

s.grade = 95     # ✅ Calls setter
print(s.grade)   # 95

s.grade = 120    # ❌ Raises ValueError
```

👉 Cleaner, more **Pythonic**, and looks like normal attribute access.

---

✅ **Summary: Why use getters & setters?**

1. To **protect data** from invalid values.
2. To **encapsulate logic** (hide details).
3. To allow **controlled access** (read-only, write-only).
4. To make code **robust & future-proof**.

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
