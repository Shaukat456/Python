---

# 🔹 What is an API Request?

When you call an API, you send a request to a server and get a response back.
A request usually includes:

* **URL (endpoint)** → The address of the API resource.
* **Method (verb)** → Defines the action: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
* **Headers** → Extra metadata like authentication or content type.
* **Body (payload)** → Data you send (for `POST`, `PUT`, etc.).
* **Response** → Data returned by the server (JSON, XML, text, etc.).

---

# 🔹 Common HTTP Methods

### 1. **GET** → Retrieve data

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status:", response.status_code)  # 200 means OK
print("Headers:", response.headers)     # Metadata about response
print("Body:", response.json())         # Parsed JSON data
```

---

### 2. **POST** → Create new data

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "foo", "body": "bar", "userId": 1}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())  # Returns the created resource
```

---

### 3. **PUT** → Replace existing data

```python
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"id": 1, "title": "updated", "body": "new content", "userId": 1}

response = requests.put(url, json=payload)

print(response.status_code)
print(response.json())
```

---

### 4. **PATCH** → Update part of a resource

```python
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"title": "patched title"}

response = requests.patch(url, json=payload)

print(response.status_code)
print(response.json())
```

---

### 5. **DELETE** → Remove a resource

```python
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print(response.status_code)  # 200/204 means success
```

---

# 🔹 Key Concepts Explained

### **1. Headers**

Headers are metadata about the request/response.
Examples:

- `Content-Type`: tells the server the format of your request body (e.g., `application/json`, `application/x-www-form-urlencoded`).
- `Authorization`: sends authentication info (API keys, tokens).
- `User-Agent`: identifies the client (browser, app, script).

```python
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}
```

---

### **2. Content Types**

This tells the API **what kind of data you’re sending**:

- `application/json` → JSON (most common for APIs).
- `application/x-www-form-urlencoded` → Form-style key=value pairs.
- `multipart/form-data` → For file uploads.

---

### **3. Response Object**

When you call `requests.get()`, you get a `Response` object with:

- `response.status_code` → HTTP status (200=OK, 404=Not Found, 500=Server error).
- `response.headers` → Metadata about the response.
- `response.text` → Raw response as a string.
- `response.json()` → Converts JSON response to Python dictionary.

---

# 🔹 Authentication Examples

### API Key in Header

```python
url = "https://api.example.com/data"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(url, headers=headers)
```

### API Key in Query Params

```python
url = "https://api.example.com/data?apikey=YOUR_API_KEY"
response = requests.get(url)
```

---

# 🔹 Example with File Upload

```python
url = "https://httpbin.org/post"
files = {"file": open("example.txt", "rb")}

response = requests.post(url, files=files)

print(response.json())
```

---

# 🔹 Example with Timeout and Error Handling

```python
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    response.raise_for_status()  # Raises error for 4xx/5xx
    print(response.json())
except requests.exceptions.Timeout:
    print("Request timed out!")
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

---

✅ With this, you can:

- Fetch data (`GET`)
- Send data (`POST`, `PUT`, `PATCH`)
- Delete data (`DELETE`)
- Work with headers, authentication, files, and errors.

---

# 🔹 1. Query Parameters

**What they are:**
Extra info added to a URL to refine or filter results. They follow a `?` and are written as `key=value`. Multiple parameters are joined with `&`.

**Why they’re used:**

- Filter data (`?status=active`)
- Sort results (`?sort=asc`)
- Control pagination (`?page=2&limit=50`)

**Example:**

```python
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1, "_limit": 3}
response = requests.get(url, params=params)
print(response.url)   # https://.../posts?userId=1&_limit=3
print(response.json())
```

---

# 🔹 2. Path Parameters

**What they are:**
Dynamic parts of the URL path. They uniquely identify a resource.

**Why they’re used:**
When you need a specific item by ID, slug, or name.
Example: `/users/42` → fetch user with ID 42.

**Example:**

```python
user_id = 42
url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
response = requests.get(url)
print(response.json())
```

---

# 🔹 3. Status Codes

**What they are:**
Numeric codes from the server telling you how the request went.

**Categories:**

- **2xx (Success)** → Everything worked.
- **3xx (Redirect)** → You’re being redirected elsewhere.
- **4xx (Client Error)** → Something wrong in your request.
- **5xx (Server Error)** → API server had a problem.

**Common examples:**

- `200 OK` → success
- `201 Created` → new resource made
- `204 No Content` → success but nothing to return
- `400 Bad Request` → request formatted wrong
- `401 Unauthorized` → missing/invalid login/token
- `404 Not Found` → resource doesn’t exist
- `500 Internal Server Error` → API broke

---

# 🔹 4. Pagination

**What it is:**
APIs rarely return _all_ data at once. Instead, they break results into pages.

**Why:**

- Performance: large datasets are too heavy.
- Usability: you may only need 20 items per request.

**How it’s done:**

- Query params (`?page=2&limit=20`)
- Cursor-based (`?after=abc123`)

**Example:**

```python
url = "https://jsonplaceholder.typicode.com/posts"
params = {"_page": 2, "_limit": 5}
r = requests.get(url, params=params)
print(r.json())
```

---

# 🔹 5. Rate Limiting

**What it is:**
APIs often cap how many requests you can make per minute/hour/day.

**Why:**

- Prevent abuse or server overload.
- Ensure fairness among users.

**How it’s signaled:**
In response headers, like:

- `X-RateLimit-Limit` → max allowed
- `X-RateLimit-Remaining` → how many left
- `Retry-After` → wait before retry

```python
print(r.headers.get("X-RateLimit-Remaining"))
```

---

# 🔹 6. Authentication Methods

APIs often require you to prove your identity. Common methods:

- **API Key:** A unique string, often passed in headers.

  ```python
  headers = {"Authorization": "Bearer YOUR_KEY"}
  requests.get(url, headers=headers)
  ```

- **Basic Auth:** Uses username + password.

  ```python
  from requests.auth import HTTPBasicAuth
  requests.get(url, auth=HTTPBasicAuth("user", "pass"))
  ```

- **OAuth2 / Bearer Token:** Login flow → get a temporary token.

---

# 🔹 7. Sessions

**What it is:**
A persistent connection that remembers things like headers or cookies across multiple requests.

**Why use it:**

- Fewer repeated setups.
- Required if API uses login + cookies.

**Example:**

```python
s = requests.Session()
s.headers.update({"Authorization": "Bearer token123"})
r1 = s.get("https://api.example.com/data1")
r2 = s.get("https://api.example.com/data2")
```

---

# 🔹 8. Cookies

**What they are:**
Small pieces of data stored by the server to maintain session state.

**Why:**
Used in web logins. Example: after logging in, server sets a session cookie to remember you.

**Example:**

```python
cookies = {"session_id": "abc123"}
r = requests.get("https://httpbin.org/cookies", cookies=cookies)
print(r.json())
```

---

# 🔹 9. Streaming Large Responses

**What it is:**
Downloading files or very large data without loading everything into memory.

**Why:**
Prevents your script from crashing on big files.

**Example:**

```python
url = "https://example.com/bigfile.zip"
with requests.get(url, stream=True) as r:
    with open("file.zip", "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
```

---

# 🔹 10. Error Handling

**Why:**
APIs are not always reliable. You need to handle:

- Network issues
- Timeouts
- 4xx or 5xx errors

**Example:**

```python
try:
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    r.raise_for_status()  # throws error if status >=400
    print(r.json())
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Other error:", e)
```

---

# 🔹 11. GraphQL APIs

**What it is:**
A newer way of working with APIs. Instead of multiple REST endpoints, you send a _query_ that describes exactly what you want.

**Why:**

- Get only the fields you need.
- Avoid multiple requests.

**Example:**

```python
url = "https://countries.trevorblades.com/"
query = """
{
  country(code: "US") {
    name
    capital
    currency
  }
}
"""
r = requests.post(url, json={"query": query})
print(r.json())
```

---

# 🔹 12. Webhooks

**What they are:**
Instead of _you_ calling the API, the API calls _your server_ when an event happens.

**Why:**

- Real-time notifications (e.g., Stripe payment success).
- Efficient: no need to poll the API.

**How in Python:**
Set up a small web server (Flask/FastAPI) that listens for incoming webhook events.

---

✅ By now you know:

- How APIs _work_ (endpoints, verbs, params, headers, auth).
- How to _handle real-world issues_ (pagination, rate limits, streaming, errors).
- How APIs differ (REST vs GraphQL vs Webhooks).
