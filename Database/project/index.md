===

- Is **production-style (clean structure)**
- Covers **MOST IMPORTANT database + SQL concepts**
- Is **teachable** (you can explain this to students)
- Uses **FastAPI + SQLAlchemy + SQLite**
- Can later be **easily upgraded to PostgreSQL**

I’ll **explain every layer** so nothing feels like magic.

---

# 🏗️ COMPLETE FASTAPI CRUD APP (BEGINNER → SOLID)

## 🎯 APP IDEA (Simple but Real)

We’ll build a **User Management System**:

- Create user
- Read users
- Update user
- Delete user

This app demonstrates:

- Primary Key
- Unique constraint
- Index
- CRUD
- Sessions
- Schemas
- Error handling

---

# 📁 FINAL PROJECT STRUCTURE

```
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
```

👉 This is the **industry-standard structure**

---

# 1️⃣ `database.py` — DATABASE CONNECTION

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()
```

### 🧠 CONCEPTS USED

| Concept | Meaning          |
| ------- | ---------------- |
| Engine  | DB connection    |
| Session | Transaction      |
| Base    | Parent of tables |

📌 **Session = short conversation with DB**

---

# 2️⃣ `models.py` — DATABASE TABLE (SQL → PYTHON)

```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
```

### 🧠 SQL CONCEPTS HERE

- **Primary Key** → `id`
- **Unique Constraint** → `email`
- **Index** → fast search
- **NOT NULL** → `name`

📌 ORM = Python version of SQL

---

# 3️⃣ `schemas.py` — DATA VALIDATION (VERY IMPORTANT)

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
```

### 🧠 WHY SCHEMAS?

- Prevent invalid input
- Control output
- Protect database

📌 **Never expose DB models directly**

---

# 4️⃣ `crud.py` — DATABASE LOGIC (SQL LIVES HERE)

```python
from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
```

### 🧠 CRUD ↔ SQL MAPPING

| Operation | SQL    | SQLAlchemy      |
| --------- | ------ | --------------- |
| Create    | INSERT | add             |
| Read      | SELECT | query           |
| Update    | UPDATE | modify + commit |
| Delete    | DELETE | delete          |

---

# 5️⃣ `main.py` — FASTAPI APP (ROUTES)

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User CRUD App")
```

---

## 🔌 DATABASE DEPENDENCY

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

📌 Always close DB connections

---

## ➕ CREATE USER

```python
@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
```

---

## 📄 READ ALL USERS

```python
@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)
```

---

## 🔍 READ SINGLE USER

```python
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

---

## ✏️ UPDATE USER

```python
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    updated_user = crud.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
```

---

## ❌ DELETE USER

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
```

---

# ▶️ RUN THE APP

```bash
uvicorn main:app --reload
```

Open:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

🎉 You now have a **FULLY WORKING CRUD APP**

---

# 🧠 WHAT A BEGINNER LEARNS FROM THIS APP

✅ SQL Primary Key
✅ Unique constraint
✅ Indexing
✅ CRUD mapping
✅ ORM fundamentals
✅ Dependency Injection
✅ Session management
✅ Error handling
✅ Real API flow

---

# 🧩 HOW THIS SCALES TO REAL APPS

Same pattern for:

- Orders
- Products
- Auth systems
- Dashboards
- SaaS apps

Change only:

- Models
- Schemas
- CRUD logic

---
