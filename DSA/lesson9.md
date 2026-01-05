# 📘 LESSON 9: QUEUE (Data Structure)

---

## 1️⃣ First Question (Hook)

Ask students 👇

> “When people stand in a line at a bank, who is served first?”

Expected:

> **The person who came first**

➡️ This is exactly how a **QUEUE** works.

---

## 2️⃣ What is a Queue?

### Definition (Simple):

> A **Queue** is a linear data structure that follows
> **FIFO – First In, First Out**

---

## 3️⃣ Real-World Analogies (VERY IMPORTANT)

| Real World     | Queue                       |
| -------------- | --------------------------- |
| Bank line      | First customer served first |
| Printer jobs   | First job printed first     |
| Traffic signal | Cars move in order          |
| Call center    | First call answered first   |

---

## 4️⃣ Queue Operations

| Operation | Meaning                   |
| --------- | ------------------------- |
| enqueue   | Insert element at rear    |
| dequeue   | Remove element from front |
| front     | View first element        |
| isEmpty   | Check empty               |

---

## 5️⃣ Visual Representation

```
Front → | 10 | 20 | 30 | ← Rear
```

- Insert from **rear**
- Remove from **front**

---

## 6️⃣ Queue Implementation (IMPORTANT)

### ❌ Problem with Python List

```python
queue = []
queue.append(10)     # enqueue
queue.pop(0)         # dequeue ❌ O(n)
```

Why bad?

- Shifting elements → slow

---

## 7️⃣ Correct Way: Using `deque`

```python
from collections import deque

queue = deque()

queue.append(10)      # enqueue
queue.append(20)
queue.append(30)

queue.popleft()       # dequeue
```

---

## 8️⃣ Time Complexity

| Operation | Time |
| --------- | ---- |
| enqueue   | O(1) |
| dequeue   | O(1) |
| front     | O(1) |

---

## 9️⃣ Real-World Applications of Queue

- CPU scheduling
- Task scheduling
- Web server requests
- BFS (graphs)
- Customer service systems

---

## 🔟 Queue vs Stack (EXAM FAVORITE)

| Feature | Stack | Queue |
| ------- | ----- | ----- |
| Order   | LIFO  | FIFO  |
| Insert  | Top   | Rear  |
| Remove  | Top   | Front |
| Example | Undo  | Line  |

---

## 1️⃣1️⃣ Example: Ticket Counter Simulation

```python
from collections import deque

queue = deque()

queue.append("Ali")
queue.append("Sara")
queue.append("Ahmed")

while queue:
    person = queue.popleft()
    print(person, "is served")
```

---

## 1️⃣2️⃣ Common Student Mistakes

❌ Using list for queue
❌ Confusing enqueue & dequeue
❌ Removing from wrong end

---

## 1️⃣3️⃣ Circular Queue (Concept Only)

Problem:

- Normal queue wastes space

Solution:

> Circular queue connects end back to start

Used in:

- Memory management
- Buffers

(We’ll code later if needed)

---

## 1️⃣4️⃣ Class Exercise

Ask students:
Output?

```python
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()
queue.append(3)
print(queue)
```

Answer:
`deque([2, 3])`

---

## 1️⃣5️⃣ Homework

1. Implement queue using class
2. Simulate printer queue
3. Compare stack vs queue in real life

---

## ✅ QUEUE COMPLETE

---

# 🔜 NEXT DATA STRUCTURE

## 📘 LESSON 10: LINKED LIST (Why Arrays Fail)
