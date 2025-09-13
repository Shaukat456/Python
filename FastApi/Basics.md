## 🚀 **1. What is FastAPI?**

- FastAPI is a **Python web framework** for building APIs (Application Programming Interfaces).
- It uses:

  - **Python OOP principles** (classes, inheritance, methods).
  - **Type hints** (`str`, `int`, `List[str]`, etc.).
  - **Decorators** (`@app.get("/")`) to map functions to routes.

Think of it as:
👉 You have a restaurant. Customers order food (requests). Your waiter (FastAPI app) takes orders, hands them to the kitchen (your Python functions), and returns the dish (response).

---

# ⚙️ **2. First FastAPI App**

```python
from fastapi import FastAPI

# Create an "app" object (like creating an instance of a class)
app = FastAPI()

@app.get("/")   # decorator → tells FastAPI this function is for GET requests to "/"
def home():
    return {"message": "Hello, World!"}
```

👉 Run with:

```bash
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 OOP Concepts here:

1. **`app = FastAPI()` → Object Instantiation**

   - `FastAPI` is a **class**.
   - `app` is an **object** created from that class.

2. **Decorators (`@app.get`) → Method binding**

   - Under the hood, `@app.get("/")` is just calling a method like:

     ```python
     app.add_api_route("/", home, methods=["GET"])
     ```

So, it’s like attaching a **new ability (route)** to your `app` object.

---

# 🍔 **3. Real-World Example: Restaurant Menu API**

```python
from fastapi import FastAPI

app = FastAPI()

# Example data (like a database)
menu = {
    1: {"name": "Burger", "price": 200},
    2: {"name": "Pizza", "price": 500},
}

@app.get("/menu")
def get_menu():
    return menu

@app.get("/menu/{item_id}")
def get_item(item_id: int):
    return menu.get(item_id, {"error": "Item not found"})
```

- `@app.get("/menu")` → See the full menu.
- `@app.get("/menu/{item_id}")` → See details of one dish.

---

## 🔑 OOP Concepts:

- **Dictionary as a simple database** → In real world, you’ll use a database, but this dict is like an in-memory object.
- **Path Parameters** (`item_id: int`) → Using Python **type hints** → OOP concept of **strong typing**.

---

# 🏗 **4. Using Classes (OOP in FastAPI)**

Let’s structure it with **Pydantic models** (classes with validation).

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a model (like a blueprint of an object)
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True   # default value

menu = {}

@app.post("/add-item/{item_id}")
def add_item(item_id: int, item: Item):
    menu[item_id] = item
    return {"message": "Item added!", "item": item}
```

Try sending JSON in a POST request:

```json
{
  "name": "Sandwich",
  "price": 150,
  "is_available": true
}
```

---

## 🔑 OOP Concepts:

1. **`class Item(BaseModel)` → Inheritance**

   - `Item` inherits from `BaseModel` (Pydantic).
   - Gains features: validation, auto JSON conversion, etc.

2. **Objects as Data**

   - Each new `Item(...)` is like creating an object with attributes.

---

# 🌍 Real-World Analogy

Think of **`BaseModel`** as a “form template” in a restaurant:

- Customer fills name, price, availability.
- FastAPI checks:

  - Is `price` a number?
  - Is `name` a string?

- If wrong → rejects order.

Just like a restaurant won’t accept an invalid order slip.

---

# 🔄 **5. HTTP Methods & CRUD**

In APIs, CRUD = Create, Read, Update, Delete.

```python
@app.get("/items")   # Read
def get_items():
    return menu

@app.get("/items/{item_id}")  # Read one
def get_item(item_id: int):
    return menu.get(item_id, {"error": "Not found"})

@app.post("/items/{item_id}")  # Create
def create_item(item_id: int, item: Item):
    menu[item_id] = item
    return {"message": "Item created", "item": item}

@app.put("/items/{item_id}")  # Update
def update_item(item_id: int, item: Item):
    menu[item_id] = item
    return {"message": "Item updated", "item": item}

@app.delete("/items/{item_id}")  # Delete
def delete_item(item_id: int):
    if item_id in menu:
        del menu[item_id]
        return {"message": "Item deleted"}
    return {"error": "Not found"}
```

---

## 🔑 OOP Concepts:

- **Encapsulation**: `menu` is your internal data, routes are controlled access methods.
- **Polymorphism**: Same function name (`create_item`, `update_item`) but different request methods (POST, PUT).
- **Abstraction**: Client doesn’t care how menu is stored (dict or database).

---

# ✅ Next Steps for You

1. Install FastAPI & Uvicorn:

   ```bash
   pip install fastapi uvicorn
   ```

2. Create `main.py` with the above examples.
3. Run:

   ```bash
   uvicorn main:app --reload
   ```

4. Play with it in browser:

   - `http://127.0.0.1:8000/docs` → Auto Swagger UI!

---
