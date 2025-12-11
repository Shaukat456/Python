---
---

# 🧠 **What is Recursion?**

**Recursion** is when a function **calls itself** to solve a **smaller version** of the same problem.

---

# 🔁 **Real-Life Analogy**

Imagine you’re standing between two mirrors.
You see **infinite smaller reflections**.

That’s recursion:
**the same thing happening inside itself repeatedly** until a stop condition (called the **base case**) is met.

---

# 📌 **Basic Recursion Structure**

Every recursive function needs **two parts**:

1. **Base Case** → When to STOP
2. **Recursive Case** → How to make the problem SMALLER

### Template (Pseudocode)

```python
def recursive_function(input):
    # BASE CASE: When to stop
    if input_meets_stop_condition:
        return simple_result

    # RECURSIVE CASE: Make problem smaller and call yourself
    return combine_result_with_recursive_function(smaller_input)
```

---

# 🚶 **Stairs Analogy**

- Base case → "Am I on the ground floor?" → Stop
- Recursive case → "Take one step down" → Continue

---

# 🚦 **Base Case vs Recursive Case**

- **Base Case:** When recursion stops
- **Recursive Case:** Function calls itself with smaller input

---

# 🧮 **Example 1 — Factorial (n!)**

### What is factorial?

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Recursive Code

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case
```

---

# 📊 **Dry Run of factorial(4)**

### Going down (recursive calls)

1. `factorial(4)` → returns `4 * factorial(3)`
2. `factorial(3)` → returns `3 * factorial(2)`
3. `factorial(2)` → returns `2 * factorial(1)`
4. `factorial(1)` → **base case reached**, returns `1`

---

### Coming back up (returning values)

- `factorial(1)` → 1
- `factorial(2)` → 2×1 = **2**
- `factorial(3)` → 3×2 = **6**
- `factorial(4)` → 4×6 = **24**

---

### Visualization

**Going Down**

```
factorial(4)
→ factorial(3)
→ factorial(2)
→ factorial(1)
→ return 1
```

**Coming Up**

```
1
2
6
24
```

---

# 🧠 **Key Idea**

Recursion happens in two phases:

1. **Forward Phase** (calls) → Go down until base case
2. **Backward Phase** (returns) → Values bubble back up

**Analogy:**
Like stacking plates — you must remove top plates first.

---

# ➗ **Example 2 — Fibonacci**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

# 📁 **Example 3 — Sum of List Elements**

```python
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])
```

---

# 🧩 **Common Interview Recursion Questions**

## ✔ Reverse a string

```python
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]
```

---

## ✔ Palindrome check

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```

---

## ✔ GCD (Euclid’s Algorithm)

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

---

## ✔ Binary Search

```python
def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, mid + 1, right)
```

---

# 🧠 Why Use Recursion?

- Elegant + clean
- Fits naturally for:

  - Trees
  - Graphs
  - Divide & conquer
  - Nested structures

---

# ⚠️ When NOT to Use Recursion

- Large inputs → **Stack overflow**
- Use iteration or memoization

---

# ⚙️ **Optimizing Recursion — Memoization**

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

---

# 🎯 **Simple Examples**

## 1️⃣ Countdown

```python
def countdown(n):
    if n == 0:
        print("Blast off! 🚀")
        return
    print(n)
    countdown(n - 1)
```

---

## 2️⃣ Sum from 1 to N

```python
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)
```

---

## 3️⃣ Print Stars Pattern

```python
def print_stars(n):
    if n == 0:
        return
    print("*" * n)
    print_stars(n - 1)
```

---

## 4️⃣ Print Each Character

```python
def print_chars(word):
    if not word:
        return
    print(word[0])
    print_chars(word[1:])
```

---

# 🏠 **Real-World Use Cases**

## 5️⃣ Count digits of a phone number

```python
def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1
    if number < 10:
        return 1
    return 1 + count_digits(number // 10)
```

---

## 6️⃣ Compound Interest Recursively

```python
def compound_interest(principal, years, rate=0.05):
    if years == 0:
        return principal
    new_amount = principal * (1 + rate)
    return compound_interest(new_amount, years - 1, rate)
```

---

## 7️⃣ Distribute Pizza Slices

```python
def distribute_slices(total_slices, people):
    if people == 1:
        return total_slices

    slices_per_person = total_slices // people
    remaining_slices = total_slices - slices_per_person

    print(f"Person gets {slices_per_person} slices")
    return distribute_slices(remaining_slices, people - 1)
```

---

## 8️⃣ Reading Tracker

```python
def pages_read_total(pages_per_day, days):
    if days == 0:
        return 0
    if days == 1:
        return pages_per_day
    return pages_per_day + pages_read_total(pages_per_day, days - 1)
```

---

# 🎲 **Interactive Examples**

## 9️⃣ Roll Dice Until 6

```python
import random

def roll_until_six(rolls=0):
    rolls += 1
    result = random.randint(1, 6)
    print(f"Roll {rolls}: Got {result}")

    if result == 6:
        print(f"🎉 Got 6 in {rolls} rolls!")
        return rolls

    return roll_until_six(rolls)
```

---

## 🔟 Shopping Cart Total (Nested Lists)

```python
def calculate_cart_total(cart):
    if not cart:
        return 0

    item = cart[0]
    rest_of_cart = cart[1:]

    if isinstance(item, list):
        return calculate_cart_total(item) + calculate_cart_total(rest_of_cart)
    else:
        return item + calculate_cart_total(rest_of_cart)
```

---

# 🧮 **More Math Problems**

## 11️⃣ Digital Root

```python
def digital_root(n):
    if n < 10:
        return n

    digit_sum = sum_digits(n)
    return digital_root(digit_sum)

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
```

---

## 12️⃣ Reverse a Number

```python
def reverse_number(n, reversed_n=0):
    if n == 0:
        return reversed_n

    last_digit = n % 10
    reversed_n = reversed_n * 10 + last_digit

    return reverse_number(n // 10, reversed_n)
```

---

## 13️⃣ Find Max in List

```python
def find_max(lst):
    if len(lst) == 1:
        return lst[0]

    max_of_rest = find_max(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest
```

---

# 🌳 **Tree-Style Recursion**

## 14️⃣ Folder Size Calculator

```python
def folder_size(structure):
    if isinstance(structure, (int, float)):
        return structure

    total_size = 0
    for item in structure:
        total_size += folder_size(item)
    return total_size
```

---

## 15️⃣ Family Tree Age Sum

```python
def family_age_sum(member):
    if isinstance(member, (int, float)):
        return member

    age = member[0]
    children = member[1] if len(member) > 1 else []

    total_age = age
    for child in children:
        total_age += family_age_sum(child)

    return total_age
```

---

# 🎯 **Challenge Problems**

### Easy

```python
def count_steps(stairs):
    if stairs == 0:
        return 0
    return 1 + count_steps(stairs - 1)
```

```python
def birthday_countdown(days):
    if days == 0:
        print("🎉 Happy Birthday!")
        return
    print(f"{days} days left")
    birthday_countdown(days - 1)
```

```python
def total_allowance(amount, weeks):
    if weeks == 0:
        return 0
    return amount + total_allowance(amount, weeks - 1)
```

---

### Medium

```python
def check_password_strength(password, index=0):
    if index >= len(password):
        return True

    char = password[index]
    if not (char.isalnum() or char in "!@#$%"):
        return False

    return check_password_strength(password, index + 1)
```

```python
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)
```

```python
def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
```

---

# 💡 Key Tips

- Find the **smallest possible input** → base case
- Assume recursion works → trust the process
- Draw recursion trees
- Confirm base case exists
- Practice every day

---
