# 📘 LESSON 8: STACK (Data Structure)

---

## 1️⃣ First Question (Hook)

Ask students 👇

> “What happens when you place plates on top of each other?”

Expected:

- Last plate placed is taken first

➡️ This idea = **STACK**

---

## 2️⃣ What is a Stack?

### Definition (Simple):

> A **Stack** is a linear data structure that follows
> **LIFO – Last In, First Out**

---

## 3️⃣ Real-World Analogies (VERY IMPORTANT)

| Real World      | Stack Concept            |
| --------------- | ------------------------ |
| Plates stack    | Last plate removed first |
| Undo button     | Last action undone       |
| Browser history | Back button              |

---

## 4️⃣ Stack Operations

| Operation | Meaning            |
| --------- | ------------------ |
| push      | Insert element     |
| pop       | Remove top element |
| peek      | View top element   |
| isEmpty   | Check empty        |

---

## 5️⃣ Visual Representation

Stack:

```
| 30 |  ← top
| 20 |
| 10 |
```

---

## 6️⃣ Implement Stack Using Python List

### Push

```python
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
```

---

### Pop

```python
stack.pop()
```

---

### Peek

```python
top = stack[-1]
```

---

### isEmpty

```python
if not stack:
    print("Stack is empty")
```

---

## 7️⃣ Time Complexity

| Operation | Time |
| --------- | ---- |
| push      | O(1) |
| pop       | O(1) |
| peek      | O(1) |

---

## 8️⃣ Real-World Applications of Stack

- Undo / Redo
- Function calls (Call Stack)
- Expression evaluation
- Parenthesis checking
- Backtracking

---

## 9️⃣ Example: Reverse a String (Using Stack)

### Problem:

> Reverse `"HELLO"`

---

### Code:

```python
def reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str
```

---

## 🔟 Example: Valid Parentheses

```python
def is_valid_parentheses(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
```

---

## 1️⃣1️⃣ Common Student Mistakes

❌ Using pop on empty stack
❌ Confusing stack with queue
❌ Using wrong end as top

---

## 1️⃣2️⃣ Class Exercise

Ask students:

- What is output?

```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()
stack.append(3)
print(stack)
```

Answer:
`[1, 3]`

---

## 1️⃣3️⃣ Homework

1. Implement stack using class
2. Reverse number using stack
3. Check balanced `{[()]}`

---

## ✅ STACK COMPLETE

---

# 🔜 NEXT DATA STRUCTURE

## 📘 LESSON 9: QUEUE (FIFO – Line System)
