# 📘 LESSON 3: Time Complexity (Big-O Notation)

---

## 1️⃣ First Class Question (Hook)

Ask students 👇

> “If two programs give the SAME output, which one is better?”

Expected answer:

> **The faster one**

➡️ This “fast or slow” idea = **Time Complexity**

---

## 2️⃣ What is Time Complexity? (Simple Language)

> **Time Complexity** tells us
> **how the running time of an algorithm grows as input size increases**

Important:

- ❌ Not actual seconds
- ✅ Growth pattern

---

## 3️⃣ Real-World Analogy (VERY IMPORTANT)

### Example: Checking Attendance

👨‍🏫 Situation:

- Class of **10 students** → fast
- Class of **10,000 students** → slow

Same method
Different input size

➡️ This is time complexity

---

## 4️⃣ Why We Don’t Measure Actual Time

Because:

- Different computers
- Different CPUs
- Different Python versions

So we measure:

> **Number of operations**

---

## 5️⃣ Input Size (n)

Tell students:

> `n = number of elements`

Examples:

- List size
- Number of students
- Length of string

---

## 6️⃣ Big-O Notation (No Fear)

Big-O answers:

> “If input becomes very large, how does time grow?”

---

## 7️⃣ Most Common Big-O Types (EXAM + PRACTICAL)

### 🟢 O(1) – Constant Time

### Example:

```python
def get_first(arr):
    return arr[0]
```

Real-World:

- Lift button
- Phone unlock

➡️ Input size doesn’t matter

---

### 🟡 O(n) – Linear Time

### Example:

```python
def print_all(arr):
    for x in arr:
        print(x)
```

Real-World:

- Roll call
- Searching name in unsorted list

---

### 🔴 O(n²) – Quadratic Time

### Example:

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

Real-World:

- Everyone shaking hands
- Round-robin matches

---

## 8️⃣ Visual Growth Comparison

Explain on board:

| n    | O(1) | O(n) | O(n²)     |
| ---- | ---- | ---- | --------- |
| 10   | 1    | 10   | 100       |
| 100  | 1    | 100  | 10,000    |
| 1000 | 1    | 1000 | 1,000,000 |

➡️ n² explodes 🔥

---

## 9️⃣ Rule of Thumb (VERY IMPORTANT)

Tell students to memorize this **thinking**, not table:

> One loop → O(n)
> Nested loop → O(n²)
> Loop inside loop inside loop → O(n³)

---

## 🔟 Ignoring Constants (Key Concept)

### Example:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Operations = 2n
Big-O = **O(n)** (ignore constants)

---

## 1️⃣1️⃣ Worst Case, Best Case, Average Case

### Example: Search

- Best case: item found first
- Worst case: item found last
- Average case: middle

👉 Big-O usually considers **worst case**

---

## 1️⃣2️⃣ Time Complexity ≠ Space Complexity

| Time     | Space           |
| -------- | --------------- |
| How fast | How much memory |
| CPU      | RAM             |

(We’ll study space later)

---

## 1️⃣3️⃣ Common Student Mistakes

❌ Counting lines
❌ Counting print statements
❌ Using stopwatch

Correct method:

> Count loops and nesting

---

## 1️⃣4️⃣ Class Exercise (Very Important)

Ask students:
What is the time complexity?

```python
def example(arr):
    for i in range(len(arr)):
        print(arr[i])
```

Answer: **O(n)**

---

```python
def example2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
```

Answer: **O(n²)**

---

## 1️⃣5️⃣ Homework (Conceptual + Coding)

1. Explain O(1), O(n), O(n²) in your own words
2. Write one real-world example for each
3. Find time complexity:

```python
for i in range(n):
    print("Hello")
```

---

## ✅ LESSON 3 COMPLETE

---
