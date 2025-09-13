When you say **“Types in FastAPI”**, there are **three main layers of types** you should know about:

---

# 🧩 **1. Python Type Hints (Basic Types)**

FastAPI heavily relies on **Python type hints** (`int`, `str`, `float`, `bool`, `List`, `Dict`, etc.).

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}
```

- `item_id: int` → must be an integer.
- `q: str | None = None` → optional string query parameter.

🔑 **OOP angle:** Type hints are like **contracts** for function arguments. They tell FastAPI (and Pydantic) how to validate data.

---

# 🧩 **2. Pydantic Types (Data Models)**

For **request bodies** (JSON input), FastAPI uses **Pydantic models** to define **complex types**.

```python
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    price: float
    tags: List[str] = []   # list of strings, default empty

@app.post("/items/")
def create_item(item: Item):
    return item
```

If the client sends JSON:

```json
{
  "name": "Pizza",
  "price": 500,
  "tags": ["cheese", "fast-food"]
}
```

✅ Works fine.
If they send:

```json
{
  "name": 123,
  "price": "abc"
}
```

❌ Rejected automatically.

🔑 **OOP angle:** Here you’re literally defining **classes (models)** that describe your data’s structure.

---

# 🧩 **3. FastAPI-Specific Types (Request/Response Helpers)**

FastAPI also provides its own **special types** in `fastapi` & `pydantic` to work with HTTP concepts.

### ✅ Path, Query, Header, Cookie

```python
from fastapi import Query, Path

@app.get("/items/{item_id}")
def read_items(
    item_id: int = Path(..., gt=0),  # must be > 0
    q: str = Query(None, min_length=3, max_length=50)  # optional, 3–50 chars
):
    return {"item_id": item_id, "q": q}
```

- `Path(...)` → extra rules for path params.
- `Query(...)` → extra rules for query params.

---

### ✅ Request Body Types

- **Form data** → `Form`
- **File uploads** → `File`, `UploadFile`
- **Headers** → `Header`
- **Cookies** → `Cookie`

Example:

```python
from fastapi import Form, File, UploadFile

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

---

### ✅ Response Types

- `Response` → raw response.
- `JSONResponse` → JSON specifically.
- `HTMLResponse` → HTML string.
- `StreamingResponse` → streams data (useful for large files).

Example:

```python
from fastapi.responses import HTMLResponse

@app.get("/hello", response_class=HTMLResponse)
def hello():
    return "<h1>Hello World</h1>"
```

---

# 🧩 **4. Typing with `typing` Module**

FastAPI also supports advanced Python typing:

- `Optional[str]` → same as `str | None`.
- `List[int]`, `Dict[str, float]`, `Tuple[str, int]`.
- `Union[str, int]` → multiple allowed types.

Example:

```python
from typing import Optional, List

@app.get("/numbers/")
def numbers(q: Optional[List[int]] = None):
    return {"numbers": q}
```

Call:
`/numbers/?q=1&q=2&q=3`
👉 Returns: `{"numbers": [1,2,3]}`

---

# 🌍 **Real-World Analogy**

Imagine you’re making a **food delivery API**:

- Basic Types → `order_id: int`, `customer_name: str`.
- Pydantic Model → Full order (items, address, payment).
- FastAPI Types → How the request comes in (query params, form, file upload).
- Response Types → How you send back data (JSON, HTML, file stream).

---

⚡ **Summary**

- **Python Types** → Basic data validation (`int`, `str`, etc.).
- **Pydantic Models** → Complex request/response bodies (structured data).
- **FastAPI Types** → Path, Query, Form, File, Cookie, Header, Response handling.

---
