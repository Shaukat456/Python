# ---

# # What is FastAPI and How Does it Work?

# ### What is FastAPI?

# * **FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
# * It's designed to be **easy to use** and **fast to code**, with automatic interactive documentation.
# * It uses **Starlette** (for the web parts) and **Pydantic** (for data validation).
# * It is asynchronous-friendly, meaning it can handle many requests concurrently, improving performance.

# ### How Does FastAPI Work?

# * You write Python functions (called **path operations** or **endpoints**) that correspond to HTTP routes (like `/items`, `/users`).
# * FastAPI reads your function parameters and type hints to:

#   * Validate input data automatically.
#   * Parse and convert data types.
#   * Generate automatic **OpenAPI** and **Swagger UI** docs.
# * FastAPI runs on an ASGI server like **Uvicorn** to serve your app.

# ---

# # Creating Routes / Endpoints in FastAPI

# Endpoints are URLs where your API listens and responds to requests.

# Basic example:

# ```python
# from fastapi import FastAPI

# app = FastAPI()


@app.get("/")  # This decorator creates a GET endpoint at root "/"
def read_root():
    return {"message": "Hello World"}


# * `@app.get("/")` means "when someone sends a GET request to `/`, call this function."
# * The function returns a JSON response by default.

# Other HTTP methods: `.post()`, `.put()`, `.delete()`, `.patch()`

# ---

# # Sending and Receiving JSON Data

# ### Sending JSON (Response)

# Return Python dictionaries or lists — FastAPI converts them to JSON automatically:

# ```python
# @app.get("/items/")
# def get_items():
#     return [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]
# ```

# ### Receiving JSON (Request)

# To accept JSON data in POST/PUT requests, define a **Pydantic model**:

# ```python
# from pydantic import BaseModel

# class Item(BaseModel):
#     id: int
#     name: str
#     completed: bool

# @app.post("/items/")
# def create_item(item: Item):
#     return {"message": f"Item {item.name} created", "item": item}
# ```

# * `Item` defines expected JSON structure.
# * FastAPI automatically validates incoming JSON and converts it into the `item` parameter.

# ---

# # Hands-on: Build a Simple CRUD API for a To-Do List

# ---

# ### Step 1: Setup

# ```bash
# pip install fastapi uvicorn
# ```

# Create a file `main.py`:

# ---

# ### Step 2: Define the FastAPI app and data model

# ```python
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# app = FastAPI()

# # Pydantic model for To-Do item
# class TodoItem(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     completed: bool = False

# # In-memory "database" (list)
# todos = []
# ```

# ---

# ### Step 3: Create Endpoints (CRUD)

# ---

# #### Create a new to-do (POST)

# ```python
# @app.post("/todos/", response_model=TodoItem)
# def create_todo(todo: TodoItem):
#     # Check for duplicate ID
#     for t in todos:
#         if t.id == todo.id:
#             raise HTTPException(status_code=400, detail="ID already exists")
#     todos.append(todo)
#     return todo
# ```

# * Accepts JSON data for a new todo.
# * Adds it to the list.
# * Returns the created item.

# ---

# #### Read all to-dos (GET)

# ```python
# @app.get("/todos/", response_model=List[TodoItem])
# def get_todos():
#     return todos
# ```

# * Returns a list of all to-dos.

# ---

# #### Read a to-do by ID (GET)

# ```python
# @app.get("/todos/{todo_id}", response_model=TodoItem)
# def get_todo(todo_id: int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     raise HTTPException(status_code=404, detail="To-Do not found")
# ```

# ---

# #### Update a to-do (PUT)

# ```python
# @app.put("/todos/{todo_id}", response_model=TodoItem)
# def update_todo(todo_id: int, updated_todo: TodoItem):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[index] = updated_todo
#             return updated_todo
#     raise HTTPException(status_code=404, detail="To-Do not found")
# ```

# * Replace the entire to-do with new data.

# ---

# #### Delete a to-do (DELETE)

# ```python
# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos.pop(index)
#             return {"message": "To-Do deleted"}
#     raise HTTPException(status_code=404, detail="To-Do not found")
# ```

# ---

# ### Step 4: Run the app

# ```bash
# uvicorn main:app --reload
# ```

# ---

# ### Step 5: Test your API

# * Open your browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
#   FastAPI provides an **interactive API documentation** where you can try the API.

# ---

# # Summary of Concepts Covered

# | Concept                   | Explanation                                                      |
# | ------------------------- | ---------------------------------------------------------------- |
# | FastAPI                   | Fast Python framework for building APIs                          |
# | Creating routes/endpoints | Defining URL paths with decorators (`@app.get()`, `@app.post()`) |
# | Sending JSON data         | Return Python dict or list from endpoint functions               |
# | Receiving JSON data       | Use Pydantic models to parse and validate incoming JSON          |
# | CRUD Operations           | Create, Read, Update, Delete endpoints for managing resources    |
# | HTTPException Handling    | Return proper HTTP status codes and messages for errors          |
# | Interactive docs          | Auto-generated Swagger UI to test API endpoints                  |
