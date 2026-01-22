---
---

# 🧠 PART 1 — What is a Database? (Big Picture)

### 🔹 Problem Without a Database

Imagine storing users like this in Python:

```python
users = [
    {"id": 1, "name": "Ali", "email": "ali@gmail.com"},
    {"id": 2, "name": "Sara", "email": "sara@gmail.com"}
]
```

❌ Problems:

- Data is lost when program stops
- Hard to search, filter, update
- No multiple users at once
- No security
- No relationships (users ↔ orders)

👉 **Database solves all of this**

---

### 🔹 What is a Database?

A **database** is:

> A **structured, persistent, organized** way to store data so programs can **read, write, update, and delete** it efficiently.

---

# 🧱 PART 2 — Database vs DBMS vs SQL

### 1️⃣ Database

The **actual data**

```
Users Table
Orders Table
Products Table
```

### 2️⃣ DBMS (Database Management System)

Software that manages the database
Examples:

- MySQL
- PostgreSQL ⭐ (BEST with FastAPI)
- SQLite (good for beginners)
- Oracle

### 3️⃣ SQL (Structured Query Language)

Language used to **talk to the DBMS**

👉 SQL is **NOT a database**
👉 SQL is a **language**

---

# 🧩 PART 3 — Relational Databases (Most Important Concept)

### 🔹 What does “Relational” mean?

Data is stored in **tables**, and tables are **related** to each other.

---

### 🔹 Table Structure

| Column (Field) | Data Type |
| -------------- | --------- |
| id             | INTEGER   |
| name           | TEXT      |
| email          | TEXT      |

Rows = Records
Columns = Attributes

---

### 🔹 Real-World Analogy

Excel Sheet 📊

- Sheet = Table
- Row = One person
- Column = Property (name, age, email)

---

# 🔑 PART 4 — Primary Key & Foreign Key (VERY IMPORTANT)

## 🔹 Primary Key (PK)

A column that:

- Uniquely identifies a row
- Cannot be NULL
- Cannot repeat

Example:

```sql
id INTEGER PRIMARY KEY
```

| id  | name |
| --- | ---- |
| 1   | Ali  |
| 2   | Sara |

---

## 🔹 Foreign Key (FK)

A column that **references another table’s primary key**

### Example: Users & Orders

#### Users Table

| id  | name |
| --- | ---- |
| 1   | Ali  |

#### Orders Table

| id  | user_id | product |
| --- | ------- | ------- |
| 1   | 1       | Laptop  |

```sql
user_id REFERENCES users(id)
```

👉 This creates a **relationship**

---

# 🔄 PART 5 — CRUD Operations (Core of SQL)

Every app does **CRUD**:

| Operation | SQL Keyword |
| --------- | ----------- |
| Create    | INSERT      |
| Read      | SELECT      |
| Update    | UPDATE      |
| Delete    | DELETE      |

---

# 🧪 PART 6 — SQL Basics (Hands-On)

## 1️⃣ CREATE TABLE

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);
```

Concepts:

- `PRIMARY KEY` → unique id
- `NOT NULL` → must have value
- `UNIQUE` → no duplicates

---

## 2️⃣ INSERT DATA

```sql
INSERT INTO users (name, email)
VALUES ('Ali', 'ali@gmail.com');
```

---

## 3️⃣ READ DATA (SELECT)

### Get everything

```sql
SELECT * FROM users;
```

### Get specific columns

```sql
SELECT name, email FROM users;
```

### Filter (WHERE)

```sql
SELECT * FROM users WHERE name = 'Ali';
```

---

## 4️⃣ UPDATE DATA

```sql
UPDATE users
SET email = 'new@gmail.com'
WHERE id = 1;
```

⚠️ Without WHERE → updates ALL rows

---

## 5️⃣ DELETE DATA

```sql
DELETE FROM users WHERE id = 1;
```

⚠️ Without WHERE → deletes EVERYTHING

---

# 🔍 PART 7 — WHERE, AND, OR, LIKE

```sql
SELECT * FROM users
WHERE name = 'Ali' AND email LIKE '%gmail%';
```

Operators:

- `=`
- `>`
- `<`
- `LIKE`
- `%` wildcard

---

# 🔢 PART 8 — Data Types (Important)

| SQL Type         | Meaning      |
| ---------------- | ------------ |
| INTEGER          | Numbers      |
| TEXT             | Strings      |
| BOOLEAN          | true / false |
| REAL             | Float        |
| DATE / TIMESTAMP | Time         |

👉 PostgreSQL has richer types (UUID, JSON)

---

# 🔗 PART 9 — JOINS (MOST CONFUSING but MOST IMPORTANT)

## Example: Users & Orders

```sql
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id;
```

### Types of Joins:

- `INNER JOIN` → matching only
- `LEFT JOIN` → all left + matches
- `RIGHT JOIN`
- `FULL JOIN`

👉 90% of time → **INNER JOIN**

---

# 📦 PART 10 — Indexes (Performance)

```sql
CREATE INDEX idx_users_email ON users(email);
```

- Makes searching faster
- Trade-off: slower inserts

---

# 🔐 PART 11 — Constraints (Data Safety)

| Constraint  | Purpose       |
| ----------- | ------------- |
| NOT NULL    | Must exist    |
| UNIQUE      | No duplicates |
| CHECK       | Custom rules  |
| FOREIGN KEY | Relationships |

Example:

```sql
age INTEGER CHECK (age >= 18)
```

---

# 🧠 PART 12 — Transactions (Atomicity)

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

If error → `ROLLBACK`

👉 VERY important for money systems

---

# 🐍 PART 13 — SQL with Python (Preview for FastAPI)

```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
```

FastAPI will use:

- `SQLAlchemy`
- `asyncpg`
- `psycopg2`

---

# 🏗 PART 14 — How This Fits into FastAPI

### Flow:

```
FastAPI Route
   ↓
SQLAlchemy ORM
   ↓
SQL Query
   ↓
PostgreSQL
```

SQL knowledge helps you:

- Design schemas
- Optimize queries
- Debug slow APIs
- Write custom queries

---
