# 📘 LESSON 7: Sorting Algorithms — Bubble Sort

---

## 1️⃣ Why Do We Need Sorting?

Ask students 👇

> “Why are exam results always displayed in sorted order?”

Reasons:

- Rank calculation
- Quick searching
- Comparisons become easy

➡️ Sorting = **foundation for efficiency**

---

## 2️⃣ What is Sorting?

> Sorting means **arranging data in a specific order**
> (ascending or descending)

Example:

- Marks: `[55, 90, 72]`
- Sorted: `[55, 72, 90]`

---

## 3️⃣ Real-World Analogy (BEST ONE)

### 🫧 Bubble Analogy

Imagine:

- Light bubbles go down
- Heavy bubbles rise to top

In array:

- Largest element moves to end in each pass

➡️ That’s **Bubble Sort**

---

## 4️⃣ Bubble Sort Idea (Very Simple)

1. Compare adjacent elements
2. Swap if they are in wrong order
3. Repeat passes
4. After each pass, **largest element is fixed**

---

## 5️⃣ Dry Run (BOARD WORK)

Array: `[5, 3, 4, 1]`

### Pass 1:

- (5,3) → swap → `[3,5,4,1]`
- (5,4) → swap → `[3,4,5,1]`
- (5,1) → swap → `[3,4,1,5]`

Largest `5` fixed ✔

---

### Pass 2:

- (3,4) → ok
- (4,1) → swap → `[3,1,4,5]`

---

### Pass 3:

- (3,1) → swap → `[1,3,4,5]`

Sorted ✅

---

## 6️⃣ Python Implementation

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

## 7️⃣ Time Complexity Analysis

| Case    | Time             |
| ------- | ---------------- |
| Best    | O(n) (optimized) |
| Worst   | O(n²)            |
| Average | O(n²)            |

Explain:

- Nested loops → n²

---

## 8️⃣ Space Complexity

- In-place sorting
- **O(1)** extra space

---

## 9️⃣ Optimized Bubble Sort (IMPORTANT)

Stop if already sorted:

```python
def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
```

---

## 🔟 When to Use Bubble Sort?

✅ Teaching & learning
❌ Large datasets
❌ Real-world systems

---

## 1️⃣1️⃣ Common Student Mistakes

❌ Forgetting `- i - 1`
❌ Confusing passes
❌ Assuming bubble sort is fast

---

## 1️⃣2️⃣ Class Exercise

Ask students:
What happens after **first pass**?

Array: `[8, 2, 6, 4]`

Answer:
`[2, 6, 4, 8]`

---

## 1️⃣3️⃣ Homework

1. Implement bubble sort for descending order
2. Count number of swaps
3. Explain bubble sort in your own words

---

## 1️⃣4️⃣ Important Teaching Tip

Tell students:

> “Bubble sort is NOT used in real systems, but it teaches thinking.”

---

## ✅ LESSON 7 COMPLETE

---

# 🔜 NEXT LESSON
