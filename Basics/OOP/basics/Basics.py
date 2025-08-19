Awesome—let’s build a clean, beginner-friendly but **detailed** guide to **OOP in Python**. I’ll go from foundations → practical patterns → “pro” Pythonic tools, with tiny examples you can copy in class and short exercises at the end.

---

# What is OOP (big picture)

OOP = **Object-Oriented Programming** → you model your program as **objects** (things) with **data** (attributes) and **behaviors** (methods).

**Four pillars:**

1. **Encapsulation** – keep data + methods together (and protect invariants).
2. **Abstraction** – expose a simple interface; hide internal details.
3. **Inheritance** – reuse/extend behavior from a base class.
4. **Polymorphism** – different objects respond to the same message (method name) in their own way.

---

# 1) Classes & Objects

### Minimal class

```python
class Student:
    def __init__(self, name, marks):   # constructor
        self.name = name               # instance attribute
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student("Ahmed", [85, 92, 78])
print(s.name, s.average())
```

* `self` = “this object”.
* `__init__` runs after the object is created; set up attributes here.

### Instance vs Class attributes

```python
class Counter:
    created = 0                 # class attribute (shared)
    def __init__(self):
        Counter.created += 1
        self.value = 0          # instance attribute (per object)

c1, c2 = Counter(), Counter()
print(Counter.created)  # 2
```

---

# 2) Encapsulation & Properties (validation)

In Python there’s no true “private”, but convention `_name` = “internal”. Use **properties** to validate/set rules.

```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = float(amount)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance = self.balance - amount
```

* Users do `acc.balance = 100` and your setter enforces rules.

---

# 3) Inheritance & Method Overriding

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):            # override
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

pets = [Dog(), Cat()]
for p in pets:
    print(p.speak())            # polymorphism: same call, different result
```

### `super()` to reuse parent logic

```python
class LoggedList(list):
    def append(self, x):
        print(f"Appending {x}")
        super().append(x)       # call list.append
```

---

# 4) Composition (prefer often) vs Inheritance

**Composition** = “has-a” relationship (flexible).
**Inheritance** = “is-a” relationship (tighter coupling).

```python
class Engine:
    def start(self): print("Engine on")

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def drive(self):
        self.engine.start()
        print("Car moving")
```

Use composition to combine behaviors without deep hierarchies.

---

# 5) Multiple Inheritance, Mixins & MRO (brief)

Python allows multiple inheritance. Keep it **simple**; use **mixins**—small classes that add a feature.

```python
class ReprMixin:
    def __repr__(self):
        cls = self.__class__.__name__
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls}({attrs})"

class User(ReprMixin):
    def __init__(self, name): self.name = name

print(User("Ali"))  # User(name='Ali')
```

**MRO** = Method Resolution Order, i.e., the order Python searches for attributes/methods in multiple inheritance. You can see it with `Class.__mro__`.

---

# 6) Abstract Base Classes (interfaces) & Polymorphism

Use `abc` to define required methods without implementation.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Square(Shape):
    def __init__(self, a): self.a = a
    def area(self): return self.a * self.a

def total_area(shapes: list[Shape]) -> float:
    return sum(s.area() for s in shapes)
```

This is formal polymorphism; **duck typing** is informal:

```python
def make_it_speak(obj):
    # works for anything with .speak()
    return obj.speak()
```

---

# 7) Magic (dunder) Methods & Operator Overloading

Make your objects feel built-in.

```python
class Vector2:
    def __init__(self, x, y): self.x, self.y = x, y

    def __repr__(self): return f"Vector2({self.x}, {self.y})"
    def __add__(self, other): return Vector2(self.x + other.x, self.y + other.y)
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __len__(self): return 2

v1, v2 = Vector2(2, 3), Vector2(1, 5)
print(v1 + v2)      # Vector2(3, 8)
print(v1 == v2)     # False
print(len(v1))      # 2
```

Common dunders: `__init__`, `__repr__/__str__`, `__len__`, `__iter__`, `__getitem__`, `__eq__/__lt__`, `__hash__`, `__enter__/__exit__` (context manager), arithmetic ones (`__add__`, etc.).

---

# 8) Dataclasses (Pythonic OOP booster)

For “data carrier” classes—less boilerplate, built-in `__init__`, `__repr__`, `__eq__`, etc.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass(slots=True)              # slots reduce memory, speed attr access
class Course:
    name: str
    students: List[str] = field(default_factory=list)  # avoid mutable default bug

c = Course("Math")
c.students.append("Ayesha")
print(c)  # Course(name='Math', students=['Ayesha'])
```

* `default_factory` avoids the **mutable default** trap.
* `frozen=True` makes instances **immutable**.
* `slots=True` avoids per-instance `__dict__` for efficiency.

---

# 9) Context Managers (resource-safe OOP)

```python
class Timer:
    import time
    def __enter__(self):
        from time import perf_counter
        self.start = perf_counter(); return self
    def __exit__(self, exc_type, exc, tb):
        from time import perf_counter
        self.elapsed = perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")

with Timer():
    sum(range(5_000_00))
```

`__enter__/__exit__` encapsulate setup/cleanup.

---

# 10) Practical micro-patterns

**Factory method:**

```python
class User:
    def __init__(self, name): self.name = name

    @classmethod
    def from_email(cls, email):
        name = email.split("@")[0].title()
        return cls(name)

u = User.from_email("ali@example.com")
```

**Static method (utility grouped with class):**

```python
class Math:
    @staticmethod
    def clamp(x, lo, hi): return max(lo, min(hi, x))
```

**Repository-like wrapper (abstraction):**

```python
class InMemoryStore:
    def __init__(self): self._data = {}
    def get(self, key): return self._data.get(key)
    def set(self, key, value): self._data[key] = value
```

---

## Best practices (Pythonic OOP)

* Prefer **composition** over deep inheritance trees.
* Use **properties** to protect invariants (validation).
* Use **dataclasses** for plain data; custom classes for behavior-heavy objects.
* Keep methods **small & cohesive**; name things clearly.
* Add `__repr__` for easy debugging.
* Type-hint your attributes & methods.
* Avoid mutable default args (`list`, `dict`)—use `default_factory`.

---

## Quick exercises (with hints)

1. **Rectangle class**

   * attrs: `width`, `height`
   * methods: `area()`, `perimeter()`
   * property: enforce `width > 0`, `height > 0`.

2. **Inventory with composition**

   * `Item(name, price)`
   * `Cart` holds a list of `Item`s
   * `Cart.total()` returns sum of prices.

3. **Shapes hierarchy**

   * `Shape(ABC)` with abstract `area()`
   * `Circle`, `Rectangle` implement it
   * function `largest_shape(shapes)` returns shape with max area.

4. **Vector overloading**

   * `Vector2(x, y)` implement `__add__`, `__sub__`, `__mul__(scalar)`, `__repr__`.

5. **Dataclass Student**

   * fields: `name: str`, `marks: list[int] = field(default_factory=list)`
   * `average` method (non-field function) using a normal method.

6. **SafeBankAccount**

   * use properties to validate deposits/withdrawals
   * add `__repr__` to show owner & balance.

