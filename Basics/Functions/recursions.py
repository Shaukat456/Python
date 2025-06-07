# Let’s break down **recursion in Python** with a detailed, beginner-to-intermediate guide — using real-world analogies, visual examples, common interview problems, and logic-building exercises.

# ---

# ## 🧠 What is Recursion?

# **Recursion** is when a function calls **itself** to solve a **smaller version** of a problem.

# ### 🔁 Real-Life Analogy

# Imagine you're standing in front of a mirror that reflects another mirror behind you. You see **infinite reflections** — each one smaller than the last. That’s **recursion**: the same thing happening inside itself repeatedly, until a stop condition (called **base case**) is met.

# ---

# ## 📌 Basic Recursion Structure

# ```python
# def recursive_function():
#     if base_case_condition:
#         return result
#     else:
#         return recursive_function(smaller_input)
# ```

# ---

# ## 🚦 Base Case and Recursive Case

# * **Base Case:** When to stop calling the function.
# * **Recursive Case:** The part where the function calls itself with a smaller input.

# ---

# ## 📚 Examples with Real-Life Analogies

# ---

# ### 🧮 1. **Factorial (n!)**

# **Problem:**
# `5! = 5 × 4 × 3 × 2 × 1 = 120`

# **Code:**

# ```python
# def factorial(n):
#     if n == 0:
#         return 1  # base case
#     return n * factorial(n - 1)  # recursive case
# ```

# **Analogy:**
# You're stacking plates. You can’t pick up the bottom one until you've picked all above it. Once the bottom (base case) is reached, you return and multiply back upward.

# ---

# ### ➗ 2. **Fibonacci Series**

# **Problem:**
# `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`

# ```python
# def fibonacci(n):
#     if n <= 1:
#         return n  # base cases: 0 or 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# ```

# **Note:** This is simple but **inefficient** — we’ll discuss optimization with **memoization** later.

# ---

# ### 📁 3. **Sum of List Elements**

# ```python
# def list_sum(lst):
#     if not lst:  # empty list
#         return 0
#     return lst[0] + list_sum(lst[1:])
# ```

# **Analogy:**
# Imagine taking out coins from a piggy bank one by one, and adding them. You keep removing one (head of list) and add until the bank (list) is empty.

# ---

# ## 🧩 Common Interview Questions with Recursion

# ---

# ### ✅ 4. **Reverse a String**

# ```python
# def reverse(s):
#     if len(s) == 0:
#         return s
#     return reverse(s[1:]) + s[0]
# ```

# ---

# ### ✅ 5. **Check Palindrome Recursively**

# ```python
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
# ```

# ---

# ### ✅ 6. **Find GCD (Euclidean Algorithm)**

# ```python
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# ```

# ---

# ### ✅ 7. **Binary Search (Recursively)**

# ```python
# def binary_search(arr, target, left, right):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr, target, left, mid - 1)
#     else:
#         return binary_search(arr, target, mid + 1, right)
# ```

# ---

# ## 🧠 Why Use Recursion?

# * Naturally fits **problems with repetition** and **nested structures**.
# * Elegant and short.
# * Works well in:

#   * Tree Traversals
#   * Graph Algorithms
#   * Divide and Conquer Algorithms (e.g., Merge Sort, Quick Sort)

# ---

# ## ⚠️ When **NOT** to Use Recursion

# * For large input sizes → it may cause a **stack overflow** (too many nested calls).
# * Use **iteration** or **memoization** instead.

# ---

# ## 🧰 Optimize Recursion: Memoization

# ```python
# memo = {}

# def fib(n):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fib(n - 1) + fib(n - 2)
#     return memo[n]
# ```

# ---

# ## 🚀 Mini Challenges

# 1. Write a recursive function to:

#    * Count digits in a number
#    * Convert a decimal to binary
#    * Print a pattern of stars
#    * Sum digits of a number: `123 → 6`
#    * Flatten a nested list
