→ Databases\*\*

---

# 🟢 Step 2: **Databases in System Design**

Every large-scale system **relies heavily on databases**.
The challenge: how to design them so they don’t become the **bottleneck**.

---

## 1. SQL vs NoSQL

### 🔹 SQL (Relational Databases)

- Structured data, with tables and relations (MySQL, PostgreSQL).
- **ACID properties** (Atomicity, Consistency, Isolation, Durability).
- Best when data has **relations** (e.g., Banking, E-commerce Orders).

⚡ Example: Like a **library catalog** → every book must be in proper category & format.

---

### 🔹 NoSQL (Non-Relational)

- Flexible schema (MongoDB, Cassandra, DynamoDB).
- Good for **scaling horizontally**.
- Best for **large, unstructured, fast-growing data** (logs, IoT, social media).

⚡ Example: Like a **notebook** → you can write freely without strict rules.

---

## 2. Replication

What if one database server fails? → **System crashes** 😱

Solution: **Replication** → copy database across multiple servers.

- Master-Slave (Primary-Replica):

  - **Primary** handles writes.
  - **Replicas** handle reads.

- If primary fails → a replica is promoted.

⚡ Real-world analogy: Think of a **main teacher (primary)** writing notes on the board, and all **students (replicas)** copying them.

---

## 3. Sharding (Partitioning Data)

What if the database gets **too big**? One machine can’t handle it.

Solution: **Sharding** → split data across multiple databases.

- Example:

  - Users A–M → DB1
  - Users N–Z → DB2

⚡ Real-world analogy: Instead of keeping **all books in one giant library**, split them across **multiple libraries by subject**.

---

## 4. CAP Theorem

When scaling databases, we face trade-offs:

- **C → Consistency**: Every user sees the same data.
- **A → Availability**: System always responds, even if some servers fail.
- **P → Partition Tolerance**: Works even if network breaks between servers.

⚡ Rule: You can pick **only 2 out of 3**.

Example:

- Banking → **Consistency + Partition Tolerance** (must be correct, even if slow).
- Social Media → **Availability + Partition Tolerance** (better to show old data than fail).

---

## 5. Indexing

Databases get slow when tables grow.
Indexing = making a **search-friendly shortcut**.

- Example:

  - Without index → search like reading a whole book.
  - With index → like using the book’s **table of contents**.

---

✅ So now you know the **database-level tricks** for scalability:

- SQL vs NoSQL
- Replication
- Sharding
- CAP theorem
- Indexing

---

👉 Next step: We can go into **System Components (Message Queues, Microservices, API Gateways, etc.)**, OR we can **design a real system (like Instagram/WhatsApp/URL shortener) using all concepts so far**.
