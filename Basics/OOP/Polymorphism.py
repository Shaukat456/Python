# Here is a **Beginner to Advanced** guide on **Polymorphism in Python**, keeping your beginner-friendly yet detailed structure and **expanding it to master level** understanding—with real-world use cases, internal behavior, and advanced examples.

# ---

# # 🎓 **Mastering Polymorphism in Python: From Novice to Expert**

# ---

# ## 🌱 **Beginner Level: What is Polymorphism?**

# ### 🔍 **Definition**:

# Polymorphism means "**many forms**." It allows the **same method name** to have **different behaviors** based on the object calling it.

# > **Core Idea:** One interface, multiple implementations.

# ---

# ## 🎸 **Real-World Analogy: Musical Instruments**

# * A **guitar** plays by strumming.
# * A **piano** plays by pressing keys.
# * A **drum** plays by hitting surfaces.

# 👉 All respond to `.play()`, but each behaves **uniquely**.

# ---

# ## 🐣 **1. Method Overriding (Using Inheritance)**

# ```python
# class Animal:
#     def speak(self):
#         return "Animals make sounds"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
# ```

# ```python
# animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())  # Output differs by object type
# ```

# 📌 **Use Case:** Reusable code with object-specific behavior.

# ---

# ## 🧩 **2. Method Overloading (Emulated in Python)**

# Python doesn’t support **true method overloading**, but it can be mimicked using **default arguments** or `*args`.

# ```python
# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
# ```

# ```python
# calc = Calculator()
# print(calc.add(2, 3))       # 5
# print(calc.add(2, 3, 4))    # 9
# ```

# 📌 **Real Use:** Flexible functions that handle multiple argument patterns.

# ---

# ## 🚙 **3. Polymorphism with Functions (Duck Typing)**

# ```python
# class Car:
#     def move(self):
#         return "Car drives"

# class Boat:
#     def move(self):
#         return "Boat sails"

# class Plane:
#     def move(self):
#         return "Plane flies"

# def transport(vehicle):
#     print(vehicle.move())
# ```

# ```python
# transport(Car())   # Car drives
# transport(Boat())  # Boat sails
# ```

# 📌 **Real Use:** Write general-purpose functions that work with any class that shares the expected method.

# ---

# ## 🧱 **4. Abstract Base Classes (Enforced Polymorphism)**

# ```python
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return 3.14 * self.r * self.r

# class Square(Shape):
#     def __init__(self, s):
#         self.s = s
#     def area(self):
#         return self.s * self.s
# ```

# ```python
# shapes = [Circle(5), Square(4)]
# for s in shapes:
#     print(s.area())
# ```

# 📌 **Use Case:** Build a consistent interface for future developers or teams.

# ---

# # 🚀 **Intermediate Concepts**

# ---

# ## 🧠 **Type-Based Polymorphism vs Interface-Based**

# | Type            | Description                        | Example                         |
# | --------------- | ---------------------------------- | ------------------------------- |
# | Type-based      | Python checks based on object type | `isinstance(obj, Dog)`          |
# | Interface-based | Python trusts behavior, not type   | Just checks if `.move()` exists |

# 📌 **Python supports interface-based** polymorphism, also called **"duck typing."**

# ---

# ## 🧪 **Real-World Use Cases**

# | Domain           | Class Example                     | Method                 |
# | ---------------- | --------------------------------- | ---------------------- |
# | **Game Dev**     | `Enemy`, `Boss`, `Player`         | `attack()`             |
# | **E-commerce**   | `Book`, `Clothing`, `Electronics` | `calculate_discount()` |
# | **Data Science** | `LinearModel`, `TreeModel`        | `train()`              |

# ---

# ## 🏗️ **Advanced Polymorphism Concepts**

# ---

# ### 🔁 **Polymorphism with Iterators and Generators**

# ```python
# for item in [1, 2, 3]: print(item)
# for char in "abc": print(char)
# for key in {"a": 1, "b": 2}: print(key)
# ```

# ➡️ These use the **same `for` loop interface** but behave differently for each type. That’s polymorphism in action.

# ---

# ### 🔧 **Callable Polymorphism**

# You can make classes behave like functions using `__call__`.

# ```python
# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor
#     def __call__(self, num):
#         return self.factor * num

# double = Multiplier(2)
# print(double(5))  # Output: 10
# ```

# ---

# ### 🔄 **Operator Overloading (Another form of polymorphism)**

# ```python
# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3.x, v3.y)  # Output: 4 6
# ```

# ---

# ### 📦 **Strategy Pattern (Polymorphism via Composition)**

# ```python
# class PayPal:
#     def pay(self, amount):
#         return f"Paid {amount} using PayPal"

# class Stripe:
#     def pay(self, amount):
#         return f"Paid {amount} using Stripe"

# class PaymentProcessor:
#     def __init__(self, gateway):
#         self.gateway = gateway

#     def process(self, amount):
#         return self.gateway.pay(amount)

# processor = PaymentProcessor(Stripe())
# print(processor.process(100))
# ```

# ---

# # 🎓 **Mastery Checklist**

# ✅ Use inheritance-based polymorphism
# ✅ Emulate overloading with default values
# ✅ Use duck typing in real projects
# ✅ Implement abstract base classes with `ABC`
# ✅ Use polymorphism with composition (strategy pattern)
# ✅ Recognize polymorphism in design patterns (Observer, Visitor, etc.)
# ✅ Use polymorphism to write extensible and scalable code

# ---

# # 🧩 **Summary Diagram**

# | Technique            | Description                        | Python Feature             |
# | -------------------- | ---------------------------------- | -------------------------- |
# | Overriding           | Redefine inherited method          | Class inheritance          |
# | Overloading          | Same method name, different params | Default args / `*args`     |
# | Duck Typing          | Based on behavior not type         | Interface-based design     |
# | ABC                  | Enforce method implementation      | `abc.ABC`                  |
# | Operator Overloading | Custom `+`, `-`, etc.              | `__add__`, `__sub__`, etc. |

# ---
