# FastAPI Authentication - Postman Testing Guide

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python main.py`
3. Server will run at: `http://localhost:8000`
4. API docs available at: `http://localhost:8000/docs`

---

## 1. Root Endpoint (Public)

**GET** `http://localhost:8000/`

**Headers:** None required

**Expected Response:**

```json
{
  "message": "Welcome to FastAPI with Authentication",
  "endpoints": {
    "register": "POST /auth/register",
    "login": "POST /auth/login",
    "me": "GET /auth/me (protected)",
    "items": "GET /items (protected)",
    "create_item": "POST /items (protected)",
    "get_item": "GET /items/{item_id} (protected)",
    "update_item": "PUT /items/{item_id} (protected)",
    "delete_item": "DELETE /items/{item_id} (protected)"
  }
}
```

---

## 2. Register a New User

**POST** `http://localhost:8000/auth/register`

**Headers:**

```
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePassword123",
  "full_name": "John Doe"
}
```

**Alternative Body (minimal):**

```json
{
  "username": "jane_smith",
  "email": "jane@example.com",
  "password": "MyPassword456"
}
```

**Expected Response (201 Created):**

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "disabled": false
}
```

---

## 3. Login (Get Access Token)

**POST** `http://localhost:8000/auth/login`

**Headers:**

```
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "username": "john_doe",
  "password": "SecurePassword123"
}
```

**Expected Response (200 OK):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**⚠️ IMPORTANT:** Copy the `access_token` value. You'll need it for all protected endpoints below!

---

## 4. Get Current User Info (Protected)

**GET** `http://localhost:8000/auth/me`

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Example:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Expected Response (200 OK):**

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "disabled": false
}
```

---

## 5. Create an Item (Protected)

**POST** `http://localhost:8000/items`

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "name": "Laptop",
  "description": "High-performance laptop for coding",
  "price": 1299.99
}
```

**Alternative Body:**

```json
{
  "name": "Wireless Mouse",
  "description": "Ergonomic wireless mouse",
  "price": 29.99
}
```

**Expected Response (201 Created):**

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop for coding",
  "price": 1299.99,
  "owner": "john_doe",
  "created_at": "2026-02-02T10:30:00.123456"
}
```

---

## 6. Get All User's Items (Protected)

**GET** `http://localhost:8000/items`

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Expected Response (200 OK):**

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "High-performance laptop for coding",
    "price": 1299.99,
    "owner": "john_doe",
    "created_at": "2026-02-02T10:30:00.123456"
  },
  {
    "id": 2,
    "name": "Wireless Mouse",
    "description": "Ergonomic wireless mouse",
    "price": 29.99,
    "owner": "john_doe",
    "created_at": "2026-02-02T10:31:00.789012"
  }
]
```

---

## 7. Get Specific Item (Protected)

**GET** `http://localhost:8000/items/1`

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Expected Response (200 OK):**

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop for coding",
  "price": 1299.99,
  "owner": "john_doe",
  "created_at": "2026-02-02T10:30:00.123456"
}
```

---

## 8. Update an Item (Protected)

**PUT** `http://localhost:8000/items/1`

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "name": "Gaming Laptop",
  "description": "High-performance gaming laptop with RTX GPU",
  "price": 1599.99
}
```

**Expected Response (200 OK):**

```json
{
  "id": 1,
  "name": "Gaming Laptop",
  "description": "High-performance gaming laptop with RTX GPU",
  "price": 1599.99,
  "owner": "john_doe",
  "created_at": "2026-02-02T10:30:00.123456"
}
```

---

## 9. Delete an Item (Protected)

**DELETE** `http://localhost:8000/items/1`

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
```

**Expected Response (204 No Content):**

```
No body returned
```

---

## Error Responses

### 401 Unauthorized (Missing/Invalid Token)

```json
{
  "detail": "Not authenticated"
}
```

### 401 Unauthorized (Expired Token)

```json
{
  "detail": "Token has expired"
}
```

### 403 Forbidden (Accessing another user's item)

```json
{
  "detail": "Not authorized to access this item"
}
```

### 404 Not Found

```json
{
  "detail": "Item not found"
}
```

### 400 Bad Request (Username already exists)

```json
{
  "detail": "Username already registered"
}
```

---

## Testing Flow in Postman

1. **Register a new user** (POST `/auth/register`)
2. **Login with that user** (POST `/auth/login`) → Copy the token
3. **Set up Authorization** in Postman:
   - Go to the Authorization tab
   - Select Type: "Bearer Token"
   - Paste your token
4. **Test protected endpoints:**
   - Get your profile (GET `/auth/me`)
   - Create items (POST `/items`)
   - List items (GET `/items`)
   - Update items (PUT `/items/{id}`)
   - Delete items (DELETE `/items/{id}`)

5. **Test authorization:**
   - Register a second user
   - Login as second user (get new token)
   - Try to access first user's items (should get 403 Forbidden)

---

## Tips

- Tokens expire after 30 minutes. Login again to get a new token.
- Each user can only see/modify their own items.
- Use the interactive docs at `http://localhost:8000/docs` for quick testing.
- For Postman, you can save the token as an environment variable.
