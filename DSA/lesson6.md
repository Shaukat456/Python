# 📘 LESSON 6: Binary Search (Fast Searching)

---

## 1️⃣ First Rule (VERY IMPORTANT)

### ❗ Binary Search ONLY works on **sorted data**

Ask students:

> “Can you open a dictionary from any random page and still find a word?”

❌ No
➡️ Because dictionary is **sorted**

---

## 2️⃣ Real-World Analogy (BEST ONE)

### 📘 Dictionary Example

Steps:

1. Open middle page
2. Compare word
3. Decide left or right
4. Repeat

➡️ Divide problem into **half each time**

This idea = **Divide & Conquer**

---

## 3️⃣ Binary Search Definition

> Binary Search repeatedly **divides the search space into half**
> until the element is found or space becomes empty.

---

## 4️⃣ Why Binary Search is FAST

- Linear search → n comparisons
- Binary search → log₂(n) comparisons

Example:

- 1,000 elements → ~10 steps
- 1,000,000 elements → ~20 steps

🔥 Massive difference

---

## 5️⃣ Binary Search Algorithm (English)

1. Set low = 0, high = n-1
2. Find middle index
3. If middle == target → found
4. If target < middle → search left
5. If target > middle → search right
6. Repeat until low > high

---

## 6️⃣ Python Implementation (Iterative)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

---

## 7️⃣ Dry Run (Board Work)

Array: `[10, 20, 30, 40, 50]`
Target: `40`

Steps:

- mid = 2 → 30 < 40 → right
- mid = 3 → 40 == target → found

---

## 8️⃣ Time Complexity Analysis

| Case    | Time     |
| ------- | -------- |
| Best    | O(1)     |
| Worst   | O(log n) |
| Average | O(log n) |

---

## 9️⃣ Why Logarithmic is Powerful

Explain on board:

| n    | Steps |
| ---- | ----- |
| 8    | 3     |
| 16   | 4     |
| 32   | 5     |
| 1024 | 10    |

Each step → divide by 2

---

## 🔟 Space Complexity

- Iterative: **O(1)**
- Recursive: **O(log n)** (call stack)

---

## 1️⃣1️⃣ Recursive Binary Search (Optional)

```python
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid+1, high, target)
    else:
        return binary_search_recursive(arr, low, mid-1, target)
```

---

## 1️⃣2️⃣ Common Student Mistakes

❌ Using binary search on unsorted list
❌ Wrong mid calculation
❌ Infinite loop (low/high not updated)

---

## 1️⃣3️⃣ Linear vs Binary Search (Comparison)

| Feature     | Linear | Binary   |
| ----------- | ------ | -------- |
| Sorted data | ❌     | ✅       |
| Speed       | Slow   | Fast     |
| Complexity  | O(n)   | O(log n) |

---

## 1️⃣4️⃣ Real-World Applications

- Phone contacts
- Database indexing
- Searching IDs
- Gaming leaderboards

---

## 1️⃣5️⃣ Homework (IMPORTANT)

1. Implement binary search without using Python functions
2. Find first occurrence of element
3. Find last occurrence

---

### Example: First Occurrence (Hint)

- Modify binary search
- Continue searching left

---

## ✅ LESSON 6 COMPLETE

---

# 🔜 NEXT LESSON

## 📘 LESSON 7: Sorting Algorithms (Bubble Sort – Step by Step)
