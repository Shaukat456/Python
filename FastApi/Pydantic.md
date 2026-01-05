---
---

# 🧩 **What is Pydantic?**

- **Pydantic** is a Python library for **data validation** and **data parsing**.
- It uses **Python type hints** to check that incoming data is in the correct shape and type.
- FastAPI uses Pydantic **under the hood** for request & response models.

Think of Pydantic as:
👉 A **form checker** in a restaurant.
If someone orders food, Pydantic checks:

- Did they write the food name as a **string**?
- Did they write the price as a **number**?
- If not → Reject the request with an error.

---

# ⚙️ **Example Without Pydantic**

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/add-item/")
def add_item(name: str, price: float):
    return {"name": name, "price": price}
```

This works, but you’ll have to manually handle things if someone sends wrong data.

---

# ⚙️ **Example With Pydantic**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a "model" (blueprint for data)
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True  # default value

@app.post("/add-item/")
def add_item(item: Item):
    return {"message": "Item added", "data": item}
```

👉 Now if the client sends:

```json
{
  "name": "Pizza",
  "price": "abc"   # ❌ wrong type
}
```

FastAPI will **automatically reject** the request with a nice error message:

```json
{
  "detail": [
    {
      "loc": ["body", "price"],
      "msg": "value is not a valid float",
      "type": "type_error.float"
    }
  ]
}
```

---

# 🔑 **OOP Concepts in Pydantic**

1. **Classes & Inheritance**

   - `class Item(BaseModel)` → `Item` inherits from `BaseModel`.
   - Inheritance gives `Item` features: validation, serialization, etc.

2. **Encapsulation**

   - Data validation is hidden inside the class; you don’t worry about writing it.

3. **Polymorphism**

   - Different models can behave differently, but share the same `BaseModel` interface.

---

# 🌍 **Real-World Analogy**

Imagine every restaurant order must be written on a **standard form**:

- **Name** → must be text.
- **Price** → must be a number.
- **Is Available** → must be yes/no.

If someone writes “free” instead of a number for price, the form checker (Pydantic) rejects it before it reaches the kitchen (your business logic).

---

# 🏗️ **Bonus: Pydantic also does Conversion**

If you send:

```json
{
  "name": "Burger",
  "price": "200"
}
```

Even though `"200"` is a string, Pydantic will **auto-convert** it into `float(200)` ✅.
This is called **data parsing**.

---

⚡ In short:
👉 **Pydantic = Data model + Validation + Auto-conversion**
That’s why FastAPI feels “magical”.

---
