# ## 🔁 Functions – Logic Building & Interview Questions

# ### 🧠 1. **Write a function to check if a number is prime.**

# ```python
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# ```

# > ✅ *Tests iteration, conditionals, and return values.*

# ---

# ### 🧠 2. **Write a function that returns the factorial of a number (recursive and iterative).**

# **Recursive version:**

# ```python
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# ```

# **Iterative version:**

# ```python
# def factorial_iter(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# ```

# > ✅ *Builds understanding of recursion vs iteration.*

# ---

# ### 🧠 3. **Function to return the maximum of three numbers.**

# ```python
# def max_of_three(a, b, c):
#     return max(a, b, c)
# ```

# > ✅ *Teaches parameter handling and use of built-ins.*

# ---

# ### 🧠 4. **Write a function to count the number of vowels in a string.**

# ```python
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in text if char in vowels)
# ```

# > ✅ *Good string manipulation and iteration practice.*

# ---

# ### 🧠 5. **Write a function that reverses a string without using built-in methods.**

# ```python
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str
# ```

# ---

# ### 🧠 6. **Function with default and keyword arguments.**

# ```python
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# print(greet("Ali"))
# print(greet("Ali", greeting="Salam"))
# ```

# > ✅ *Teaches parameter types and flexibility in calling.*

# ---

# ## 📦 Modules – Interview & Use Case Based Questions

# ### 🧩 7. **What is the difference between `import module` and `from module import func`?**

# * `import module` imports the whole module.
# * `from module import func` imports only the specified function, saving memory.

# > ✅ *Common theory question in interviews.*

# ---

# ### 🧩 8. **How do you structure a project using modules?**

# Give a small structure like:

# ```
# project/
# ├── main.py
# ├── math_utils.py
# ├── string_utils.py
# ```

# You can import like:

# ```python
# from math_utils import add
# ```

# > ✅ *Tests real-world understanding of modular code.*

# ---

# ### 🧩 9. **Write your own module and import it.**

# `math_tools.py`:

# ```python
# def square(n):
#     return n * n
# ```

# `main.py`:

# ```python
# import math_tools

# print(math_tools.square(4))
# ```

# ---

# ### 🧠 10. **Create a module that calculates the area of a rectangle and circle.**

# `geometry.py`:

# ```python
# def area_rectangle(length, width):
#     return length * width

# def area_circle(radius):
#     import math
#     return math.pi * radius * radius
# ```

# ---

# ### 🧠 11. **Write a module `text_utils` with function to count words, remove punctuation, and check palindromes.**

# > Encourages code reusability and project structure.

# ---

# ### 🧠 12. **Write a function that returns both min and max from a list (as a tuple).**

# ```python
# def min_max(nums):
#     return (min(nums), max(nums))
# ```

# > ✅ *Teaches return multiple values and tuple unpacking.*

# ---

# ### 🧠 13. **Write a function that merges two dictionaries.**

# ```python
# def merge_dicts(dict1, dict2):
#     return {**dict1, **dict2}
# ```

# ---

# ### 🧠 14. **Function to find duplicates in a list.**

# ```python
# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()
#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return list(duplicates)
# ```

# ---

# ## 🧪 Challenge (Capstone)

# **Build a `calculator` module** with functions:

# * `add(a, b)`
# * `subtract(a, b)`
# * `multiply(a, b)`
# * `divide(a, b)`
# * `square(n)`
# * `power(a, b)`

# Then create a `main.py` file to test each.


# Recusions Exercises
# Write a recursive function to:

# Count digits in a number

# Convert a decimal to binary

# Print a pattern of stars

# Sum digits of a number: 123 → 6

# Flatten a nested list


# ---------------------------------
# Solutions


# ---

# # ✅ Solutions to Mini Recursive Challenges

# ---

# ### 🧮 1. **Count Digits in a Number**

# ```python
# def count_digits(n):
#     if n == 0:
#         return 0
#     return 1 + count_digits(n // 10)
# ```

# **Example:**
# `count_digits(12345)` → `5`

# ---

# ### 🔁 2. **Convert Decimal to Binary (as String)**

# ```python
# def decimal_to_binary(n):
#     if n == 0:
#         return ''
#     return decimal_to_binary(n // 2) + str(n % 2)
# ```

# **Example:**
# `decimal_to_binary(10)` → `'1010'`

# ---

# ### ⭐ 3. **Print Pattern of Stars (Right Triangle)**

# ```python
# def print_stars(n):
#     if n == 0:
#         return
#     print_stars(n - 1)
#     print('*' * n)
# ```

# **Example Output for `n=4`:**

# ```
# *
# **
# ***
# ****
# ```

# ---

# ### 🔢 4. **Sum of Digits**

# ```python
# def sum_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits(n // 10)
# ```

# **Example:**
# `sum_digits(123)` → `6`

# ---

# ### 🔂 5. **Flatten a Nested List**

# ```python
# def flatten(lst):
#     flat = []
#     for item in lst:
#         if isinstance(item, list):
#             flat.extend(flatten(item))
#         else:
#             flat.append(item)
#     return flat
# ```

# **Example:**
# `flatten([1, [2, [3, 4], 5]])` → `[1, 2, 3, 4, 5]`

# ---

# # 🔄 Iteration vs Recursion

# | Feature        | Recursion                       | Iteration                        |
# | -------------- | ------------------------------- | -------------------------------- |
# | **Definition** | Function calls itself           | Looping using `for` or `while`   |
# | **Use Case**   | Tree, graph, nested structures  | Linear sequences                 |
# | **Memory**     | More (uses call stack)          | Less (no function call overhead) |
# | **Speed**      | Slower (stack usage)            | Faster                           |
# | **Code Size**  | Compact, elegant                | Verbose but more efficient       |
# | **Risk**       | Stack overflow if not optimized | Less risky                       |

# ### 📌 Example: Factorial – Recursion vs Iteration

# **Recursive:**

# ```python
# def factorial_recursive(n):
#     if n == 0:
#         return 1
#     return n * factorial_recursive(n - 1)
# ```

# **Iterative:**

# ```python
# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# ```

# ✅ **Use Recursion when**:

# * Problem has a natural recursive structure (e.g., trees)
# * Code clarity is more important than performance

# ✅ **Use Iteration when**:

# * Performance or large inputs matter
# * You want lower memory usage


# When dealing with nested JSON from an API, recursion helps to:

# * Extract keys/values
# * Count nested elements
