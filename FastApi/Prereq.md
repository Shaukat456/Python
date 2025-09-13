Let’s go step by step 👇

---

# 🧩 1. **Virtual Environment (venv)**

A **virtual environment** is like a **separate kitchen for each restaurant** 🍳.

- If you install packages globally, every project shares them → conflicts.
- With `venv`, each project gets its **own set of ingredients** (packages).

### Create venv:

```bash
python -m venv venv
```

### Activate:

- **Windows (PowerShell):**

```bash
venv\Scripts\activate
```

- **Linux/Mac:**

```bash
source venv/bin/activate
```

✅ You’ll see `(venv)` in your terminal, meaning you’re inside the virtual kitchen.

---

# 🧩 2. **Packages in FastAPI Projects**

FastAPI is not alone, it works with several important packages:

### Core ones:

- **fastapi** → main framework.
- **uvicorn** → ASGI server (like a waiter serving food).
- **pydantic** → validation (form checker).

### Common extras:

- **sqlalchemy** → database ORM.
- **databases** → async DB queries.
- **alembic** → database migrations.
- **python-multipart** → form & file uploads.
- **jinja2** → templates for HTML responses.

Install like:

```bash
pip install fastapi uvicorn[standard] sqlalchemy
```

---

# 🧩 3. **`requirements.txt`**

Instead of telling your friend every package manually, you write a **shopping list** 🛒.

Create:

```bash
pip freeze > requirements.txt
```

It will look like:

```
fastapi==0.115.0
uvicorn==0.30.0
pydantic==2.9.0
```

Anyone can run:

```bash
pip install -r requirements.txt
```

and get **exact same setup** ✅.

---

# 🧩 4. **Imports & Packages**

In Python, a **package = folder with `__init__.py`** file.

- `import` lets you use code from another module.
- FastAPI apps often break into **packages** for organization.

Example project structure:

```
myshop/
│── main.py
│── models/         # package
│   │── __init__.py
│   │── item.py
│── routes/         # package
│   │── __init__.py
│   │── items.py
```

Inside `routes/items.py`:

```python
from fastapi import APIRouter
from models.item import Item

router = APIRouter()

@router.get("/items")
def get_items():
    return {"msg": "All items"}
```

Inside `main.py`:

```python
from fastapi import FastAPI
from routes import items

app = FastAPI()
app.include_router(items.router)
```

👉 **Routers** = break your app into small packages (like departments in a company).

---

# 🧩 5. **ASGI vs WSGI**

FastAPI runs on **ASGI (Asynchronous Server Gateway Interface)**, not WSGI.

- **WSGI** (Flask, Django classic): Handles one request at a time.
- **ASGI** (FastAPI): Handles multiple requests at the same time → fast 🚀

Analogy:

- WSGI = One waiter per table.
- ASGI = One waiter serving many tables at once.

That’s why `uvicorn` is used → it’s an ASGI server.

---

# 🧩 6. **Auto Docs (Swagger & Redoc)**

FastAPI uses Pydantic + type hints to generate **docs automatically**.

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

👉 You don’t write docs, FastAPI does it for you!

---

# 🧩 7. **Environment Variables (.env)**

Don’t hardcode secrets (like DB passwords). Use `.env`.

`.env` file:

```
DATABASE_URL=sqlite:///shop.db
SECRET_KEY=supersecret
```

Use with:

```bash
pip install python-dotenv
```

`main.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv("DATABASE_URL")
```

---

# 🧩 8. **Project Run Commands**

- Start server:

```bash
uvicorn main:app --reload
```

- Run with host/port:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

- Production: often use **Gunicorn + Uvicorn workers**.

---

# ✅ Summary of Mini Concepts

- **Virtual env** → separate package space per project.
- **Packages** → extra functionality (fastapi, uvicorn, sqlalchemy, etc).
- **Requirements.txt** → reproducible environment.
- **Imports & Packages** → structure large apps cleanly.
- **ASGI** → async + concurrency = faster.
- **Auto docs** → Swagger & Redoc built-in.
- **.env** → manage secrets & config.

---
