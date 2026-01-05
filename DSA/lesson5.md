---
# 📘 LESSON 5: Searching Algorithms — Linear Search
---

## 1️⃣ Why Searching is Important?

Ask students 👇

> “If you have 1,000 student records, how will you find **Ali’s marks**?”

Options:

- Check one by one ❌ (slow)
- Smart searching ✅

➡️ Searching is **core problem** in programming.

---

## 2️⃣ What is Searching?

> Searching means **finding the position or existence of an element** in data.

Output can be:

- Index (position)
- True / False

---

## 3️⃣ Linear Search (Basic & Universal)

### Definition:

> Linear Search checks **each element one by one** until target is found.

---

## 4️⃣ Real-World Analogy (VERY IMPORTANT)

### 🧾 Attendance Register

- Names not sorted
- Teacher starts from top
- Stops when name found

➡️ Linear Search

---

## 5️⃣ When to Use Linear Search?

✅ Data is **unsorted**
✅ Small dataset
✅ Simple implementation

❌ Large datasets (slow)

---

## 6️⃣ Linear Search Algorithm (English)

1. Start from first element
2. Compare with target
3. If match → stop
4. Else → move next
5. If end reached → not found

---

## 7️⃣ Python Implementation

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

## 8️⃣ Dry Run (Board Work)

Array: `[10, 25, 30, 45]`
Target: `30`

Steps:

- Compare 10 ❌
- Compare 25 ❌
- Compare 30 ✅ → found at index 2

---

## 9️⃣ Time Complexity Analysis

| Case    | Time |
| ------- | ---- |
| Best    | O(1) |
| Worst   | O(n) |
| Average | O(n) |

Explain:

- Best: element at first position
- Worst: element at last or not present

---

## 🔟 Space Complexity

- No extra memory used
- **O(1)**

---

## 1️⃣1️⃣ Common Student Mistakes

❌ Forgetting to return -1
❌ Comparing index instead of value
❌ Using break without return

Example ❌:

```python
if i == target:   # wrong
```

Correct ✅:

```python
if arr[i] == target:
```

---

## 1️⃣2️⃣ Linear Search Variations

### Search Boolean

```python
def exists(arr, target):
    for x in arr:
        if x == target:
            return True
    return False
```

---

## 1️⃣3️⃣ Real-World Use Cases

- Small apps
- Searching in unsorted data
- Early prototyping
- Debugging

---

## 1️⃣4️⃣ Class Exercise

Ask students:
Find time complexity:

```python
for i in range(len(arr)):
    if arr[i] == x:
        break
```

Answer: **O(n)**

---

## 1️⃣5️⃣ Homework (Very Important)

1. Implement linear search for strings
2. Count how many times target appears
3. Find index of last occurrence

---

### Example: Count Occurrences

```python
def count_occurrences(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count
```

---

## ✅ LESSON 5 COMPLETE

---

# 🔜 NEXT LESSON

## 📘 LESSON 6: Binary Search (Fast Searching 🔥)
