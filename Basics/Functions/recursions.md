# ## 🧠 What is Recursion?

# **Recursion** is when a function calls **itself** to solve a **smaller version** of the same problem.

# ### 🔁 Real-Life Analogy

# Imagine you're standing in front of a mirror that reflects another mirror behind you. You see **infinite reflections** — each one smaller than the last. That’s **recursion**: the same thing happening inside itself repeatedly, until a stop condition (called **base case**) is met.

# ---

# ## 📌 Basic Recursion Structure

# Every recursive function needs TWO parts:

# 1. **Base Case**: When to STOP (like reaching the ground floor)

# 2. **Recursive Case**: How to make the problem SMALLER

# TEMPLATE (Pseudocode):

def recursive_function(input): # BASE CASE: When to stop
if input_meets_stop_condition:
return simple_result

    # RECURSIVE CASE: Make problem smaller and call yourself
    return combine_result_with_recursive_function(smaller_input)

# Think of it like walking down stairs:

# - Base case: "Am I on the ground floor?" → Stop

# - Recursive case: "Take one step down" → Continue

# ---

# ## 🚦 Base Case and Recursive Case

# \* **Base Case:** When to stop calling the function.

# \* **Recursive Case:** The part where the function calls itself with a smaller input.

# ---

# ## 📚 Examples with Real-Life Analogies

# ---

# ### 🧮 1. **Factorial (n!)**

# **Problem:**

# `5! = 5 × 4 × 3 × 2 × 1 = 120`

# **Code:**

# ```python

# def factorial(n):

# if n == 0:

# return 1 # base case

# return n \* factorial(n - 1) # recursive case

# ```

# ---

# ## 🧮 Reminder: What is Factorial?

# ```

# factorial(4) = 4 × 3 × 2 × 1 = 24

# ```

# Recursive definition:

# ```

# factorial(n) = 1 if n == 1 (base case)

# factorial(n) = n × factorial(n-1) otherwise

# ```

# ---

# ## 🐍 Code

# ```python

# ## 📊 Dry Run of `factorial(4)`

# ### **Step 1**: Call `factorial(4)`

# \* `n = 4` → not base case

# _ Returns → `4 _ factorial(3)`

# ### **Step 2**: Call `factorial(3)`

# \* `n = 3` → not base case

# _ Returns → `3 _ factorial(2)`

# ### **Step 3**: Call `factorial(2)`

# \* `n = 2` → not base case

# _ Returns → `2 _ factorial(1)`

# ### **Step 4**: Call `factorial(1)`

# \* `n = 1` → base case hit

# \* Returns `1`

# ---

# ## 📤 Now Stack Starts Returning

# \* `factorial(1)` returns `1`

# _ `factorial(2)` returns `2 _ 1 = 2`

# _ `factorial(3)` returns `3 _ 2 = 6`

# _ `factorial(4)` returns `4 _ 6 = 24`

# Final Answer: **24**

# ## 🔄 Visualization of Calls

# **Going Down (Recursive Calls):**

# ```

# factorial(4)

# → 4 \* factorial(3)

# → 3 \* factorial(2)

# → 2 \* factorial(1)

# → return 1

# ```

# **Coming Up (Returning Values):**

# ```

# factorial(1) → 1

# factorial(2) → 2

# factorial(3) → 6

# factorial(4) → 24

## 🐍 Code

# def factorial(n):

# if n == 1: # base case

# return 1

# else: # recursive case

# return n \* factorial(n - 1)

# print(factorial(4))

# ```

# ---

# ## 🔎 Step-by-Step Explanation

# ### **Step 0 — Start of Program**

# \* Python reads the code.

# \* It sees `print(factorial(4))` → so it calls the function `factorial(4)`.

# ---

# ### **Step 1 — First Call: factorial(4)**

# \* Function is called with `n = 4`.

# \* Inside function:

# \* Is `n == 1`? → No (since `4 != 1`).

# \* So it goes to the **else part**.

# _ It says: “I need to return `4 _ factorial(3)`.”

# \* But wait! To return that, it must first **calculate `factorial(3)`**.

# \* So it **pauses** and makes a new function call: `factorial(3)`.

# ---

# ### **Step 2 — Second Call: factorial(3)**

# \* Function is called with `n = 3`.

# \* Is `n == 1`? → No.

# _ So it says: “I need to return `3 _ factorial(2)`.”

# \* But it doesn’t know `factorial(2)` yet → so it pauses and calls `factorial(2)`.

# ---

# ### **Step 3 — Third Call: factorial(2)**

# \* Function is called with `n = 2`.

# \* Is `n == 1`? → No.

# _ So it says: “I need to return `2 _ factorial(1)`.”

# \* Again, it doesn’t know `factorial(1)` yet → so it pauses and calls `factorial(1)`.

# ---

# ### **Step 4 — Fourth Call: factorial(1)**

# \* Function is called with `n = 1`.

# \* Is `n == 1`? → Yes!

# \* **Base case reached** → It returns `1` immediately.

# \* No more function calls now — recursion stops growing.

# ---

# ## 📤 Step 5 — Start Returning Values

# Now the functions that were paused will **resume one by one**, starting from the top of the stack.

# 1. `factorial(1)` returned `1`.

# \* So now `factorial(2)` can finish:

# _ `factorial(2) = 2 _ 1 = 2`

# \* Returns `2`.

# 2. Now `factorial(3)` can finish:

# _ `factorial(3) = 3 _ 2 = 6`

# \* Returns `6`.

# 3. Now `factorial(4)` can finish:

# _ `factorial(4) = 4 _ 6 = 24`

# \* Returns `24`.

# Finally, `print(factorial(4))` prints → **24**.

# ---

# ## 🖼 Visualizing the Call Stack

# **When calling (going down):**

# ```

# factorial(4) → waiting for factorial(3)

# factorial(3) → waiting for factorial(2)

# factorial(2) → waiting for factorial(1)

# factorial(1) → returns 1 (base case)

# ```

# **When returning (going up):**

# factorial(1) = 1

# factorial(2) = 2 \* 1 = 2

# factorial(3) = 3 \* 2 = 6

# factorial(4) = 4 \* 6 = 24

# ```

# ## 🧠 Key Idea

# \* Recursion works in **two phases**:

# 1. **Forward Phase (calls)**: Functions keep calling smaller versions until the base case is reached.

# 2. **Backward Phase (returns)**: Once base case returns, the paused functions **resume one by one** in reverse order.

# **Analogy:**

# You're stacking plates. You can’t pick up the bottom one until you've picked all above it. Once the bottom (base case) is reached, you return and multiply back upward.

# ---

# ### ➗ 2. **Fibonacci Series**

# **Problem:**

# `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`

# ```python

# def fibonacci(n):

# if n <= 1:

# return n # base cases: 0 or 1

# return fibonacci(n - 1) + fibonacci(n - 2)

# ```

# **Note:** This is simple but **inefficient** — we’ll discuss optimization with **memoization** later.

# ---

# ### 📁 3. **Sum of List Elements**

# ```python

# def list_sum(lst):

# if not lst: # empty list

# return 0

# return lst[0] + list_sum(lst[1:])

# ```

# **Analogy:**

# Imagine taking out coins from a piggy bank one by one, and adding them. You keep removing one (head of list) and add until the bank (list) is empty.

# ---

# ## 🧩 Common Interview Questions with Recursion

# ---

# ### ✅ 4. **Reverse a String**

# ```python

# def reverse(s):

# if len(s) == 0:

# return s

# return reverse(s[1:]) + s[0]

# ```

# ---

# ### ✅ 5. **Check Palindrome Recursively**

# ```python

# def is_palindrome(s):

# if len(s) <= 1:

# return True

# if s[0] != s[-1]:

# return False

# return is_palindrome(s[1:-1])

# ```

# ---

# ### ✅ 6. **Find GCD (Euclidean Algorithm)**

# The GCD (Greatest Common Divisor) of two numbers is the largest number that divides both of them without leaving a remainder.

# ```python

# def gcd(a, b):

# if b == 0:

# return a

# return gcd(b, a % b)

# ```

# ---

# ### ✅ 7. **Binary Search (Recursively)**

# ```python

# def binary_search(arr, target, left, right):

# if left > right:

# return -1

# mid = (left + right) // 2

# if arr[mid] == target:

# return mid

# elif arr[mid] > target:

# return binary_search(arr, target, left, mid - 1)

# else:

# return binary_search(arr, target, mid + 1, right)

# ```

# ---

# ## 🧠 Why Use Recursion?

# \* Naturally fits **problems with repetition** and **nested structures**.

# \* Elegant and short.

# \* Works well in:

# \* Tree Traversals

# \* Graph Algorithms

# \* Divide and Conquer Algorithms (e.g., Merge Sort, Quick Sort)

# ---

# ## ⚠️ When **NOT** to Use Recursion

# \* For large input sizes → it may cause a **stack overflow** (too many nested calls).

# \* Use **iteration** or **memoization** instead.

# ---

# ## 🧰 Optimize Recursion: Memoization

# ```python

# memo = {}

# def fib(n):

# if n in memo:

# return memo[n]

# if n <= 1:

# return n

# memo[n] = fib(n - 1) + fib(n - 2)

# return memo[n]

# ```

# ---

# ## 🎯 Simple Warm-up Examples (Start Here!)

# ### 🔢 1. **Countdown Timer**

# Like counting down before a rocket launch: 5, 4, 3, 2, 1, Blast off!

def countdown(n):
if n == 0:
print("Blast off! 🚀")
return
print(n)
countdown(n - 1)

# Usage: countdown(5)

# Output: 5, 4, 3, 2, 1, Blast off! 🚀

# ### 📊 2. **Sum from 1 to N**

# Like adding up your daily savings: Day 1: $1, Day 2: $2, etc.

def sum_to_n(n):
if n == 1:
return 1 # Base case: sum of 1 is just 1
return n + sum_to_n(n - 1)

# Usage: sum_to_n(5) = 5 + 4 + 3 + 2 + 1 = 15

# ### 🌟 3. **Print Stars Pattern**

# Like building a pyramid, one row at a time

def print*stars(n):
if n == 0:
return
print("*" \_ n)
print_stars(n - 1)

# Usage: print_stars(4)

# Output:

# \*\*\*\*

# \*\*\*

# \*\*

# \*

# ### 🔤 4. **Print Each Character**

# Like reading a book letter by letter

def print_chars(word):
if not word: # Empty string
return
print(word[0]) # Print first character
print_chars(word[1:]) # Recursive call with rest of string

# Usage: print_chars("HELLO")

# Output: H, E, L, L, O (each on new line)

# ---

# ## 🏠 Real-World Use Cases

# ### 📱 5. **Phone Number Digits Counter**

# Count how many digits are in a phone number

def count_digits(number): # Convert to positive if negative # abs function explain: abs() returns the absolute value of a number
number = abs(number)

    if number == 0:
        return 1  # Special case: 0 has 1 digit
    if number < 10:
        return 1  # Single digit
    return 1 + count_digits(number // 10)

# Usage: count_digits(1234567890) = 10 digits

# ### 💰 6. **Calculate Compound Interest**

# Like money growing in your savings account year by year

def compound_interest(principal, years, rate=0.05):
if years == 0:
return principal # Each year, money grows by the interest rate
new_amount = principal \* (1 + rate)
return compound_interest(new_amount, years - 1, rate)

# Usage: compound_interest(1000, 3, 0.05)

# Year 1: $1050, Year 2: $1102.50, Year 3: $1157.63

# ### 🍕 7. **Pizza Slice Distribution**

# Divide pizza slices equally among friends

def distribute_slices(total_slices, people):
if people == 1:
return total_slices # Last person gets remaining slices

    slices_per_person = total_slices // people
    remaining_slices = total_slices - slices_per_person

    print(f"Person gets {slices_per_person} slices")
    return distribute_slices(remaining_slices, people - 1)

# Usage: distribute_slices(8, 3)

# Shows how slices are distributed among 3 people

# ### 📚 8. **Book Pages Reading Tracker**

# Track daily reading progress

def pages_read_total(pages_per_day, days):
if days == 0:
return 0
if days == 1:
return pages_per_day
return pages_per_day + pages_read_total(pages_per_day, days - 1)

# Usage: pages_read_total(20, 7) = 140 pages in a week

# ---

# ## 🎮 Interactive Examples

# ### 🎲 9. **Dice Roll Simulator**

# Keep rolling until you get a 6

import random

def roll_until_six(rolls=0):
rolls += 1
result = random.randint(1, 6)
print(f"Roll {rolls}: Got {result}")

    if result == 6:
        print(f"🎉 Got 6 in {rolls} rolls!")
        return rolls

    return roll_until_six(rolls)

# Usage: roll_until_six()

# Keeps rolling until you get a 6

# ### 🛒 10. **Shopping Cart Total**

# Calculate total price of items in nested categories

def calculate_cart_total(cart):
if not cart:
return 0

    item = cart[0]
    rest_of_cart = cart[1:]

    # If item has subcategory (nested list), calculate its total
    if isinstance(item, list):
        return calculate_cart_total(item) + calculate_cart_total(rest_of_cart)
    else:
        return item + calculate_cart_total(rest_of_cart)

# Usage: calculate_cart_total([10, 20, [5, 15], 30]) = 80

# ---

# ## 🧮 Mathematical Examples Made Simple

# ### ➕ 11. **Digital Root**

# Keep adding digits until single digit (like finding your lucky number!)

def digital_root(n):
if n < 10:
return n

    # Sum all digits
    digit_sum = sum_digits(n)
    return digital_root(digit_sum)

def sum_digits(n):
if n == 0:
return 0
return (n % 10) + sum_digits(n // 10)

# Usage: digital_root(987) → 9+8+7=24 → 2+4=6

# ### 🔄 12. **Number Reverser**

# Reverse a number like looking in a mirror

def reverse_number(n, reversed_n=0):
if n == 0:
return reversed_n

    last_digit = n % 10
    reversed_n = reversed_n * 10 + last_digit

    return reverse_number(n // 10, reversed_n)

# Usage: reverse_number(1234) = 4321

# ### 🏆 13. **Find Maximum in List**

# Like finding the tallest person in a line

def find_max(lst): # Base case: single element
if len(lst) == 1:
return lst[0]

    # Compare first element with max of rest
    max_of_rest = find_max(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest

# Usage: find_max([3, 7, 2, 9, 1]) = 9

# ---

# ## 🌳 Tree-like Structure Examples

# ### 📁 14. **Folder Size Calculator**

# Calculate total size of files in folders and subfolders

def folder_size(structure):
"""
structure can be: - A number (file size) - A list (folder containing files/subfolders)
"""
if isinstance(structure, (int, float)):
return structure # It's a file

    total_size = 0
    for item in structure:
        total_size += folder_size(item)

    return total_size

# Usage: folder_size([100, 200, [50, 75], 300]) = 725 MB

# ### 👨‍👩‍👧‍👦 15. **Family Tree Age Sum**

# Add up ages in a family tree

def family_age_sum(family_member):
"""
family_member format: [age, [child1, child2, ...]]
or just age if no children
"""
if isinstance(family_member, (int, float)):
return family_member # Just an age

    age = family_member[0]
    children = family_member[1] if len(family_member) > 1 else []

    total_age = age
    for child in children:
        total_age += family_age_sum(child)

    return total_age

# Usage: family_age_sum([45, [20, 18, [25, [2]]]])

# Parent(45) + Child1(20) + Child2(18) + Grandchild(25) + Great-grandchild(2) = 110

# ---

# ## 🚀 Challenge Problems (Try These!)

# ### 🎯 Easy Challenges

# 1. **Step Counter**: Count steps going up stairs (each step adds 1)

def count_steps(stairs):
if stairs == 0:
return 0
return 1 + count_steps(stairs - 1)

# 2. **Birthday Countdown**: Count days until birthday

def birthday_countdown(days):
if days == 0:
print("🎉 Happy Birthday!")
return
print(f"{days} days until birthday!")
birthday_countdown(days - 1)

# 3. **Allowance Calculator**: Calculate total allowance over weeks

def total_allowance(weekly_amount, weeks):
if weeks == 0:
return 0
return weekly_amount + total_allowance(weekly_amount, weeks - 1)

# ### 🎯 Medium Challenges

# 4. **Password Strength Checker**: Check each character recursively

def check_password_strength(password, index=0):
if index >= len(password):
return True # Checked all characters

    char = password[index]
    if not (char.isalnum() or char in "!@#$%"):
        return False  # Invalid character

    return check_password_strength(password, index + 1)

# 5. **Binary Converter**: Convert decimal to binary

def decimal_to_binary(n):
if n == 0:
return "0"
if n == 1:
return "1"
return decimal_to_binary(n // 2) + str(n % 2)

# 6. **List Flattener**: Flatten nested lists

def flatten_list(nested_list):
result = []
for item in nested_list:
if isinstance(item, list):
result.extend(flatten_list(item))
else:
result.append(item)
return result

# Usage: flatten_list([1, [2, 3], [4, [5, 6]]]) = [1, 2, 3, 4, 5, 6]

# ---

# ## 💡 Key Tips for Students

# 1. **Start Small**: Always identify the simplest case (base case)

# 2. **Trust the Process**: Assume the recursive call works for smaller inputs

# 3. **Draw It Out**: Visualize the function calls like a tree

# 4. **Check Your Base Case**: Make sure it actually stops the recursion

# 5. **Practice Daily**: Try one simple recursive problem each day

# ---

# ## 🏃‍♂️ Practice Exercises

# **Week 1**: Master countdown, sum_to_n, print_stars

# **Week 2**: Try factorial, fibonacci, reverse_string

# **Week 3**: Attempt tree-like problems (folder_size, family_tree)

# **Week 4**: Challenge yourself with optimization (memoization)

# Remember: Recursion is like learning to ride a bike - confusing at first,

# but once it clicks, you'll wonder why it seemed so hard! 🚴‍♂️
