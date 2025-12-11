---
---

# ✅ **Dictionary Comprehension in Python**

Dictionary comprehension allows you to create **dictionaries** in a **clean, fast, and readable** way — similar to list comprehension, but for key–value pairs.

---

# 🔹 1. **Basic Syntax**

```
new_dict = { key_expression : value_expression  for item in iterable }
```

---

# 🔹 2. **Basic Example**

```python
nums = [1, 2, 3]
square_map = {n: n*n for n in nums}
print(square_map)
```

**Output**

```
{1: 1, 2: 4, 3: 9}
```

---

# 🔹 3. **Dictionary Comprehension With Condition**

```python
nums = [1, 2, 3, 4, 5]
even_squares = {n: n*n for n in nums if n % 2 == 0}
print(even_squares)
```

**Output**

```
{2: 4, 4: 16}
```

---

# 🔹 4. **If–Else Inside Dictionary Comprehension**

```python
nums = [1, 2, 3, 4]
labels = {n: ("Even" if n % 2 == 0 else "Odd") for n in nums}
print(labels)
```

**Output**

```
{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even'}
```

---

# 🔹 5. **Looping Through Dictionary Items**

```python
student_marks = {"Ali": 80, "Sara": 92, "Ahmed": 67}

result = {name: ("Pass" if marks >= 70 else "Fail")
          for name, marks in student_marks.items()}

print(result)
```

**Output**

```
{'Ali': 'Pass', 'Sara': 'Pass', 'Ahmed': 'Fail'}
```

---

# 🔥 REAL WORLD USE CASES

---

# ✅ **Use Case 1: Count Frequency of Characters**

```python
text = "banana"
freq = {char: text.count(char) for char in set(text)}
print(freq)
```

**Output**

```
{'b': 1, 'a': 3, 'n': 2}
```

---

# ✅ **Use Case 2: Convert List of Tuples Into Dictionary**

```python
data = [("name", "Ali"), ("age", 22), ("city", "Lahore")]
dict_data = {key: value for key, value in data}
print(dict_data)
```

**Output**

```
{'name': 'Ali', 'age': 22, 'city': 'Lahore'}
```

---

# ✅ **Use Case 3: Clean a Dictionary (Remove None Values)**

```python
info = {"name": "Ali", "age": None, "job": "Engineer"}
cleaned = {k: v for k, v in info.items() if v is not None}
print(cleaned)
```

**Output**

```
{'name': 'Ali', 'job': 'Engineer'}
```

---

# ✅ **Use Case 4: Reverse a Dictionary**

```python
data = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in data.items()}
print(reversed_dict)
```

---

# ✅ **Use Case 5: Transform Values (Useful in APIs / JSON)**

```python
prices_usd = {"apple": 1, "banana": 0.5, "milk": 2}

# Convert to PKR
prices_pkr = {item: price * 280 for item, price in prices_usd.items()}
print(prices_pkr)
```

---

# 🔥 Advanced Use Case

### Group words by their first letter

```python
words = ["apple", "ant", "ball", "bat", "cat"]

grouped = {
    letter: [w for w in words if w.startswith(letter)]
    for letter in set(w[0] for w in words)
}

print(grouped)
```

**Output**

```
{
 'a': ['apple', 'ant'],
 'b': ['ball', 'bat'],
 'c': ['cat']
}
```

---

# ⭐ Summary Table

| Task                | Example                                          |
| ------------------- | ------------------------------------------------ |
| Basic               | `{n: n*n for n in nums}`                         |
| With Condition      | `{n: n*n for n in nums if n%2==0}`               |
| If–Else             | `{n: 'Even' if n%2==0 else 'Odd' for n in nums}` |
| From dict items     | `{k:v for k,v in d.items()}`                     |
| Real-world cleaning | `{k:v for k,v in info.items() if v}`             |

---
