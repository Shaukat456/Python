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
