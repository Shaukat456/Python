# 🏗️ What is System Design?

System design = **designing the architecture of a large software system** so that it works correctly, efficiently, and can scale as users/data grow.

It’s about answering:

- **How do we structure the system?** (monolith, microservices, etc.)
- **How do we store and retrieve data?** (databases, caching, indexing)
- **How do we handle scale?** (load balancers, distributed systems, sharding)
- **How do we make it reliable?** (replication, failover, monitoring)

---

# 🎯 Two Types

1. **High-Level Design (HLD):**

   - Big picture architecture.
   - What components exist (API, DB, Cache, Load Balancer, etc.) and how they talk.
   - Example: “Our app has a web frontend → talks to backend → backend uses DB + Redis.”

2. **Low-Level Design (LLD):**

   - Class diagrams, database schema, APIs.
   - Example: “The `User` table has fields: id, name, email. The `AuthenticationService` has a `login()` method.”

---

# 🚖 Real-World Analogy: **Ride-Hailing App (Careem/Uber)**

Imagine you’re building **Uber**.

- **High-Level:**

  - Mobile app → sends request to backend.
  - Backend → has services (User Service, Ride Matching Service, Payment Service).
  - Database stores users, drivers, rides.
  - Redis cache stores live driver locations.
  - Kafka event system sends "ride booked" to notification service.

- **Low-Level:**

  - `Ride` class has fields: `id, rider_id, driver_id, start_location, end_location`.
  - `MatchService` finds nearest driver using Haversine formula (geo distance).

---

# 🔑 Core System Design Topics

Here’s the roadmap we’ll cover (step by step, each with examples):

1. **Scalability Basics**

   - Vertical vs Horizontal scaling
   - Load balancers
   - Caching (Redis, Memcached)

2. **Databases**

   - SQL vs NoSQL
   - Indexing, Sharding, Replication

3. **APIs & Communication**

   - REST vs gRPC vs GraphQL
   - Sync vs Async communication

4. **Distributed Systems**

   - CAP theorem
   - Event-driven architecture (Kafka, RabbitMQ)

5. **Designing Key Components**

   - Rate limiting
   - Authentication & Authorization
   - Search systems
   - Feed systems (like Twitter/Instagram)

6. **Case Studies (step by step)**

   - Design **URL Shortener (like bit.ly)**
   - Design **Instagram/Twitter Feed**
   - Design **WhatsApp**
   - Design **Quantum Computing Cloud Service** (since you’re physics-focused 🚀)

---

# ⚡ Example 1: URL Shortener (Bit.ly)

This is a classic **intro system design problem**.

**Requirements:**

- User gives a long URL → system returns short URL.
- Short URL redirects to original URL.
- Should handle **millions of requests/day**.

**High-Level Design:**

1. User → API Gateway → URL Service → Database.
2. Store mapping:

   ```
   short_code → long_url
   ```

3. Use **hashing or base62 encoding** to generate short code.
4. Add **cache (Redis)** to serve popular links fast.
5. Add **Load Balancer** to scale horizontally.

---

# ⚡ Example 2: WhatsApp (Chat System)

**Requirements:**

- 1-to-1 chat + group chat.
- Messages must be delivered **instantly**.
- Messages stored for history.

**Design:**

1. **Client (mobile app)** → sends message via API.
2. **Backend** uses **message queue (Kafka/RabbitMQ)** to deliver messages.
3. Store messages in **NoSQL DB (like Cassandra)** for high write throughput.
4. For **real-time delivery**, use **WebSockets** instead of HTTP polling.
5. Replication ensures messages aren’t lost.

---

# 📌 Key Principle

👉 System design is **trade-offs**:

- SQL = consistency, NoSQL = scalability.
- Caching = fast, but may serve stale data.
- Async = scalable, but adds complexity.

---
