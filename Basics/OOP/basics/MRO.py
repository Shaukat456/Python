Perfect 🔥 — let’s dive into **Python’s MRO (Method Resolution Order)**.
This is the **engine behind `super()`** and multiple inheritance.

---

# 🧠 1. What is MRO?

* **MRO (Method Resolution Order)** is the order in which Python looks for a method (or attribute) when you call it on an object.
* When you do `obj.method()`, Python searches:

  1. The object’s **own class**
  2. Then its **parent(s)** (in left-to-right order)
  3. Keeps going up until it finds the method, or raises `AttributeError`.

---

# 🎬 2. Simple Example

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.greet()
```

👉 Search order: `C → B → A`.
So output = `"Hello from A"`.

---

# 🔄 3. Multiple Inheritance

Now things get interesting:

```python
class A:
    def greet(self):
        print("A")

class B:
    def greet(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.greet()
```

👉 Search order: `C → A → B`.
Output = `"A"` (not `"B"`, because A comes first).

---

# ⚙️ 4. Diamond Problem (the real reason MRO exists)

```python
class A:
    def show(self): print("A")

class B(A):
    def show(self): print("B")

class C(A):
    def show(self): print("C")

class D(B, C):
    pass

obj = D()
obj.show()
```

✅ Output = `"B"`

👉 Search order: `D → B → C → A`.
This avoids calling `A` twice or skipping classes.

---

# 🔑 5. How to See the MRO

Use the `.mro()` method or `__mro__`:

```python
print(D.mro())
```

Output:

```
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

👉 This is the **exact order Python follows**.

---

# 📐 6. Rule Behind MRO (C3 Linearization)

Python uses the **C3 linearization algorithm**.
In short:

* Child class comes before parent.
* If multiple parents: follow left-to-right order.
* Each parent is considered only once (to avoid duplicates).

---

# 🍽️ 7. Real-World Analogy

Imagine a **family dinner** 🍴:

* You want to ask for a recipe.
* First, you ask **your mom** (child’s first parent).
* If she doesn’t know, you ask **your dad**.
* If not, you ask **grandma** (next in the chain).
* You never ask the same person twice, and you follow a polite order.

That’s how MRO works.

---

# ⚡ 8. Why MRO Matters

* Ensures **consistent behavior** in multiple inheritance.
* Allows `super()` to work properly, by calling the **next class in the MRO**.
* Prevents duplicate method calls in complex hierarchies.

---

✅ Summary:

* MRO = the **order Python searches for methods**.
* You can check it with `.mro()`.
* `super()` uses MRO to decide who’s next.
* Solves the **diamond problem** elegantly.

---
