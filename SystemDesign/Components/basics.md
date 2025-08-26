---

# 🟢 Step 3: System Components

## 1. **Load Balancer (LB)**

- Distributes traffic across multiple servers so no single server is overloaded.
- Ensures **high availability** and **fault tolerance**.

⚡ Example:
Imagine a **restaurant with multiple waiters**. A **host (LB)** assigns customers to free waiters.

👉 Tools: **Nginx, HAProxy, AWS ELB**

---

## 2. **Caching Layer**

- Stores **frequently accessed data in memory** (RAM) for super-fast retrieval.
- Reduces load on DB.

⚡ Example:
Like a **post-it note on your desk** — you don’t go to the library (DB) every time.

👉 Tools: **Redis, Memcached**

---

## 3. **Message Queues**

- Handle **asynchronous tasks** (background jobs).
- Decouples systems → sender doesn’t wait for receiver.

⚡ Example:
Like a **to-do list app**. You drop tasks in the list, workers pick them up when free.

👉 Tools: **RabbitMQ, Kafka, AWS SQS**

---

## 4. **CDN (Content Delivery Network)**

- Distributes **static content** (images, CSS, videos) across servers worldwide.
- Users get content from the nearest server → faster performance.

⚡ Example:
Like **ice cream shops in multiple cities** instead of one central shop.

👉 Tools: **Cloudflare, Akamai, AWS CloudFront**

---

## 5. **API Gateway**

- Single entry point for client requests.
- Handles **authentication, rate limiting, routing**.

⚡ Example:
Like a **receptionist at an office** — they check your ID, decide which department you should go to.

👉 Tools: **Kong, Nginx, AWS API Gateway**

---

## 6. **Microservices**

- Instead of one giant app (monolith), break into **smaller services** (User Service, Payment Service, Notification Service).
- Independent deployment, scaling, and failure handling.

⚡ Example:
Like a **company with separate departments** (HR, Finance, IT) instead of one person doing everything.

👉 Tools: **Docker, Kubernetes**

---

## 7. **Monitoring & Logging**

- Track health of the system (errors, performance).
- Alert before failure happens.

⚡ Example:
Like a **car dashboard** → shows speed, fuel, and warnings.

👉 Tools: **Prometheus, Grafana, ELK Stack (Elasticsearch + Logstash + Kibana)**

---

✅ These are the **core system design components** you’ll always see in large-scale apps.

---

👉 Next Step Options:

1. Deep dive into **each component** (e.g., how caching works in detail, cache eviction strategies, consistency problems).
2. Or, start building a **real system design case study** (e.g., WhatsApp, Instagram, or Netflix) using these components step by step.
