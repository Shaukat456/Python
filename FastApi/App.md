---
---

## 📝 **Full CRUD App (FastAPI)**

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Step 1: Create app instance
app = FastAPI()

# Step 2: Define a Pydantic model (blueprint for items)
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Step 3: In-memory "database"
items_db = {}

# Step 4: CRUD Routes

# Home
@app.get("/")
def home():
    return {"message": "Welcome to My FastAPI Shop!"}

# CREATE (POST) → Add item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        return {"error": "Item already exists"}
    items_db[item_id] = item
    return {"msg": "Item added", "item": item}

# READ (GET) → Get single item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items_db:
        return items_db[item_id]
    return {"error": "Item not found"}

# READ ALL (GET) → Get all items
@app.get("/items")
def list_items():
    return items_db

# UPDATE (PUT) → Update item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        return {"error": "Item not found"}
    items_db[item_id] = item
    return {"msg": "Item updated", "item": item}

# DELETE (DELETE) → Remove item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    del items_db[item_id]
    return {"msg": f"Item {item_id} deleted"}
```

---

# ⚡ **How to Run**

```bash
uvicorn main:app --reload
```

Swagger docs: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
(FastAPI gives you an interactive playground automatically 🎉)

---

# 📦 **Example Workflows**

### ✅ 1. Create (POST)

URL: `/items/1`
Payload:

```json
{
  "name": "Pizza",
  "price": 500,
  "in_stock": true
}
```

Response:

```json
{
  "msg": "Item added",
  "item": {
    "name": "Pizza",
    "price": 500,
    "in_stock": true
  }
}
```

---

### ✅ 2. Read All (GET)

URL: `/items`
Response:

```json
{
  "1": {
    "name": "Pizza",
    "price": 500,
    "in_stock": true
  }
}
```

---

### ✅ 3. Update (PUT)

URL: `/items/1`
Payload:

```json
{
  "name": "Pizza (Large)",
  "price": 800,
  "in_stock": false
}
```

Response:

```json
{
  "msg": "Item updated",
  "item": {
    "name": "Pizza (Large)",
    "price": 800,
    "in_stock": false
  }
}
```

---

### ✅ 4. Delete (DELETE)

URL: `/items/1`
Response:

```json
{
  "msg": "Item 1 deleted"
}
```

---

# 🔑 **OOP Concepts Inside**

- `class Item(BaseModel)` → **Inheritance** (validation comes from `BaseModel`).
- `items_db = {}` → **Encapsulation** (internal state hidden).
- Same function names with different HTTP verbs → **Polymorphism**.
- Routes (`@app.get`, `@app.post`) → **Abstraction** (client doesn’t care how you store items).

---

👉 Now you have a **complete CRUD FastAPI app** 🎉
