---
---

# 🌐 BASIC NETWORKING CONCEPTS

## (For Backend Developers — Beginner Level)

---

## 1️⃣ What is a Network?

### 💡 Definition

A **network** is a group of computers/devices connected so they can **communicate and share data**.

### 🧠 Analogy

- Humans → talk using language
- Computers → talk using **protocols**

---

## 2️⃣ Client–Server Model (FOUNDATION)

### 💡 What is it?

One machine **requests**, another machine **responds**.

```
Client (Browser / App)
        ↓ request
Server (FastAPI / Django)
        ↑ response
```

### 🧠 Analogy

Restaurant 🍽️

- Client → Customer
- Server → Waiter
- Kitchen → Backend logic

---

### 🔧 Backend Relevance

- You build the **server**
- Clients could be:
  - Browser
  - Mobile app
  - Another server

---

## 3️⃣ IP Address — _Digital Home Address_

### 💡 What is an IP Address?

A unique number that identifies a device on a network.

Example:

```
192.168.1.10
```

### 🏠 Analogy

Home address:

```
House #12, Street 5
```

👉 Without IP → data doesn’t know where to go

---

### Types of IPs

| Type    | Meaning              |
| ------- | -------------------- |
| Private | Inside local network |
| Public  | On the internet      |

---

## 4️⃣ Port — _Service Door_

### 💡 What is a Port?

A **port** tells _which application_ on a machine should receive the data.

```
IP        → Machine
Port      → Application
```

### 🚪 Analogy

Building (IP)
Different doors (Ports):

- Door 80 → Web
- Door 22 → SSH
- Door 5432 → PostgreSQL

---

### Common Ports (Important)

| Port | Service     |
| ---- | ----------- |
| 80   | HTTP        |
| 443  | HTTPS       |
| 22   | SSH         |
| 5432 | PostgreSQL  |
| 3306 | MySQL       |
| 8000 | FastAPI dev |

---

## 5️⃣ DNS — _Internet Phonebook_

### 💡 What is DNS?

Converts **domain name → IP address**

```
google.com → 142.250.x.x
```

### 📞 Analogy

Contact name → phone number

👉 Humans remember names
👉 Computers use IPs

---

## 6️⃣ HTTP / HTTPS — _Web Communication_

### 💡 What is HTTP?

A **protocol** that defines how clients and servers talk.

```
Client → HTTP Request
Server → HTTP Response
```

---

### HTTP Request Contains:

- Method (GET, POST, etc.)
- Headers
- Body (optional)

### HTTP Response Contains:

- Status code
- Headers
- Body

---

### HTTPS

- HTTP + Encryption (TLS)
- Protects passwords, tokens

👉 **Backend must always use HTTPS in production**

---

## 7️⃣ HTTP METHODS (VERY IMPORTANT)

| Method | Purpose                |
| ------ | ---------------------- |
| GET    | Read data              |
| POST   | Create data            |
| PUT    | Update entire resource |
| PATCH  | Update partial         |
| DELETE | Delete data            |

### 🧠 REST Mapping

```
GET    /users
POST   /users
GET    /users/1
PUT    /users/1
DELETE /users/1
```

---

## 8️⃣ HTTP STATUS CODES (INTERVIEW FAVORITE)

### Categories

| Range | Meaning      |
| ----- | ------------ |
| 2xx   | Success      |
| 4xx   | Client error |
| 5xx   | Server error |

---

### Common Ones

| Code | Meaning      |
| ---- | ------------ |
| 200  | OK           |
| 201  | Created      |
| 400  | Bad request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not found    |
| 500  | Server error |

---

## 9️⃣ Headers — _Metadata_

### 💡 What are Headers?

Extra info about request/response.

Examples:

- Content-Type
- Authorization
- User-Agent

### 🧠 Analogy

Envelope on a letter:

- Sender
- Receiver
- Instructions

---

## 🔐 10️⃣ Authentication vs Authorization

### Authentication

👉 Who are you?

### Authorization

👉 What are you allowed to do?

---

### 🧠 Analogy

- Authentication → Login
- Authorization → Permission

Backend handles **both**

---

## 11️⃣ Cookies vs Tokens (JWT)

### Cookies

- Stored by browser
- Auto sent with requests

### Tokens (JWT)

- Stored by client
- Manually sent in header

```http
Authorization: Bearer <token>
```

👉 Modern APIs use **JWT**

---

## 12️⃣ REST API (Core Backend Concept)

### REST Principles:

- Stateless
- Resource-based
- Uses HTTP methods

### Example:

```
/users
/orders
/products
```

---

## 13️⃣ Load Balancer — _Traffic Controller_

### 💡 What is it?

Distributes requests across multiple servers.

### 🚦 Analogy

Traffic police at intersection

```
Client → Load Balancer → Server 1 / Server 2
```

---

## 14️⃣ Latency & Bandwidth

### Latency

- Delay
- “Time to reach”

### Bandwidth

- Amount of data per second

### 🧠 Analogy

- Latency → time to open tap
- Bandwidth → pipe width

---

## 15️⃣ TCP vs UDP (Basic Awareness)

| TCP          | UDP                 |
| ------------ | ------------------- |
| Reliable     | Fast                |
| Ordered      | No guarantee        |
| Used by HTTP | Used by video/games |

Backend → **mostly TCP**

---

## 16️⃣ Firewall — _Security Guard_

### 💡 What is a Firewall?

Controls **who can access your server**

### 🧠 Analogy

Security guard checking entry

Backend dev must know:

- Open ports
- Block dangerous traffic

---

## 17️⃣ Proxy & Reverse Proxy (IMPORTANT)

### Reverse Proxy (Nginx)

- Stands in front of backend
- Handles:
  - HTTPS
  - Load balancing
  - Caching

```
Client → Nginx → FastAPI
```

---

## 18️⃣ CORS — _Frontend–Backend Rule_

### 💡 What is CORS?

Security rule for browsers.

### Problem:

Frontend (localhost:3000)
Backend (localhost:8000)

Browser says ❌

### Solution:

Backend allows frontend

```python
from fastapi.middleware.cors import CORSMiddleware
```

---

## 19️⃣ WebSockets (Basic Idea)

### HTTP

Request → Response → Done

### WebSocket

Connection stays open (chat, live updates)

---

## 20️⃣ How All This Fits Together (Big Picture)

```
Browser
   ↓ DNS
Server IP + Port
   ↓ HTTPS
Reverse Proxy
   ↓
FastAPI
   ↓
Database
```

---

# 🎯 WHAT A BACKEND BEGINNER SHOULD REMEMBER

✅ Client–Server
✅ IP + Port
✅ DNS
✅ HTTP/HTTPS
✅ Status Codes
✅ REST APIs
✅ Auth basics
✅ Load balancing
✅ CORS

---
