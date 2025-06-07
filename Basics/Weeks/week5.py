# * ✅ Lists
# * ✅ Tuples
# * ✅ Dictionaries
# * ✅ Sets

# Each section has:

# * Concept-checking questions
# * Logical exercises
# * Real-world analogies
# * Bonus challenge for deeper thinking

# ---

# ### 🔢 **Lists**

# #### ✅ Concept Check

# 1. What is the difference between `append()` and `extend()`?
# 2. What happens if you use `list1 + list2`?
# 3. How do you remove all occurrences of an item from a list?

# #### 🧠 Logical Exercises

# 1. **Remove duplicates from a list without using `set()`**

data = [1, 2, 2, 3, 4, 4, 4, 5]

# 2. **Find the second largest number in a list**

#    ```python
numbers = [12, 45, 2, 10, 33, 45]
#    ```

# 3. **Reverse the list without using `reversed()` or slicing**

#    ```python
nums = [1, 2, 3, 4, 5]
#    ```

# #### 🔄 Real-world Analogy

# Think of a list as a **to-do list** where you can add, remove, or reorder items.

# ---

# ### 🔗 **Tuples**

# #### ✅ Concept Check

# 1. Can you modify a tuple? Why or why not?
# 2. What happens if you try to add items to a tuple?

# #### 🧠 Logical Exercises

# 1. **Convert a list of tuples to a dictionary**

#    ```python
pairs = [("a", 1), ("b", 2), ("c", 3)]
#    ```

# 2. **Swap two numbers without using a third variable using tuple unpacking**

#    ```python
a = 5
b = 10
#    ```

# 3. **Extract even-indexed elements from a tuple**

#    ```python
my_tuple = (10, 20, 30, 40, 50, 60)
#    ```

# #### 🧳 Real-world Analogy

# Tuples are like **items in a travel bag**: fixed once packed, and you can't change them mid-journey.

# ---

# ### 📒 **Dictionaries**

# #### ✅ Concept Check

# 1. What happens if you access a key that doesn’t exist?
# 2. What’s the difference between `get()` and direct key access?
# 3. How do you merge two dictionaries?

# #### 🧠 Logical Exercises

# 1. **Count the frequency of each element in a list using a dictionary**

#    ```python
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
#    ```

# 2. **Invert a dictionary** (swap keys and values)

#    ```python
data = {"a": 1, "b": 2, "c": 3}
#    ```

# 3. **Create a dictionary from two lists**

#    ```python
keys = ["name", "age", "gender"]
values = ["Ali", 25, "male"]
#    ```

# #### 📦 Real-world Analogy

# Dictionaries are like **contact lists** where each person (key) has details (value) — quick access by name, not position.

# ---

# ### 🎯 **Sets**

# #### ✅ Concept Check

# 1. Why can't sets have duplicate values?
# 2. What’s the difference between `set1 & set2`, `set1 | set2`, `set1 - set2`?

# #### 🧠 Logical Exercises

# 1. **Find unique elements in a list**

#    ```python
data = [1, 2, 2, 3, 4, 4, 5]
#    ```

# 2. **Find common elements between two lists**

#    ```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
#    ```

# 3. **Check if two sets are disjoint**

#    ```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
#    ```

# #### 🛑 Real-world Analogy

# Sets are like **guest entry lists**: no one’s name can appear twice.

# ---

# ### 💡 Bonus Challenge (All-in-One)

# > Given a list of student records:

# ```python
# students = [
#     {"name": "Ali", "marks": 87},
#     {"name": "Zara", "marks": 92},
#     {"name": "Ali", "marks": 95},
#     {"name": "Sara", "marks": 78}
# ]

# # **Tasks**:

# # * Remove duplicate names (keep highest marks).
# # * Convert the result into a list of tuples (name, marks).
# # * Sort the final list by marks (descending).


# ---

# ## 🧩 **Lists: Intermediate Exercises**

# ### 🔁 1. **Merge Two Lists Without Duplicates**

# ```python
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# # Output: [1, 2, 3, 4, 5, 6]
# ```

# **Real-world analogy**: Combining guest lists from two different events.

# ---

# ### 🧠 2. **Find All Pairs in a List That Sum Up to a Target**

# ```python
# nums = [1, 2, 3, 4, 5]
# target = 6

# # Output: [(1, 5), (2, 4)]
# ```

# **Use case**: Financial app matching two expenses that add up to a budget.

# ---

# ### 🛠️ 3. **Flatten a Nested List**

# ```python
# nested = [[1, 2], [3, 4], [5]]

# # Output: [1, 2, 3, 4, 5]
# ```

# **Real-world analogy**: Unpacking boxes inside boxes into one big box.

# ---

# ## 🪢 **Tuples: Intermediate Exercises**

# ### 🔄 1. **Group a List of Tuples by First Element**

# ```python
# data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]

# # Output: {"fruit": ["apple", "banana"], "vegetable": ["carrot"]}
# ```

# **Use case**: Grouping products by category.

# ---

# ### 🔄 2. **Convert Tuple of Lists to List of Tuples**

# ```python
# t = ([1, 2], [3, 4], [5, 6])

# # Output: [(1, 3, 5), (2, 4, 6)]
# ```

# Use `zip()` and unpacking — great exercise for understanding structure transformation.

# ---

# ## 📖 **Dictionaries: Intermediate Exercises**

# ### 🔁 1. **Merge Two Dictionaries (with Custom Conflict Resolution)**

# ```python
# a = {"x": 1, "y": 2}
# b = {"y": 3, "z": 4}

# # If keys overlap, keep the higher value
# # Output: {'x': 1, 'y': 3, 'z': 4}
# ```

# **Real-world analogy**: Combining stock data from two warehouses.

# ---

# ### 🔍 2. **Find the Key with the Maximum Value**

# ```python
# data = {"Ali": 87, "Zara": 92, "Sara": 78}

# # Output: Zara
# ```

# **Use case**: Finding top scorer from a class record.

# ---

# ### 🧮 3. **Count Word Frequency in a Sentence**

# ```python
# sentence = "this is a test this is only a test"

# # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
# ```

# **Real-world analogy**: Word cloud generator, search term counter.

# ---

# ## 🧂 **Sets: Intermediate Exercises**

# ### 🟰 1. **Check if Two Lists Have Same Elements (Ignoring Order & Duplicates)**

# ```python
# a = [1, 2, 3, 3]
# b = [3, 2, 1]

# # Use set to check equality
# ```

# ---

# ### ❌ 2. **Find Elements Present in One List but Not the Other**

# ```python
# a = [1, 2, 3]
# b = [2, 3, 4]

# # Output: [1] (in a but not in b)
# ```

# Use `set(a) - set(b)`

# ---

# ### 🔁 3. **Symmetric Difference of Two Sets**

# ```python
# # Elements in either set but not both
# a = {1, 2, 3}
# b = {3, 4, 5}

# # Output: {1, 2, 4, 5}
# ```

# **Use case**: Comparing inventory changes between two dates.

# ---

# ## 🎯 Bonus: **Integrated Challenge**

# ```python
# students = [
#     ("Ali", 85),
#     ("Zara", 90),
#     ("Sara", 78),
#     ("Ali", 95)
# ]
# ```

# 🔹 Remove duplicate names, keeping highest mark
# 🔹 Convert to dictionary
# 🔹 Sort the dictionary by marks (descending)
# 🔹 Convert it to a list of tuples
