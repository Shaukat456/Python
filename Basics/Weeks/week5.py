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

# ----------------------------------------------------------

# Solutions
# ---

# ## ✅ **LISTS**

# ### 🔁 1. Merge Two Lists Without Duplicates

# ```python
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# merged = list(set(a + b))
# print(merged)
# ```

# **Explanation:**

# * `a + b` → combines two lists.
# * `set()` → removes duplicates.
# * `list()` → converts the result back to a list.

# 🧠 **Real-world analogy**: Merging contact lists without repeating names.

# ---

# ### 🧠 2. Find All Pairs That Sum Up to a Target

# ```python
# nums = [1, 2, 3, 4, 5]
# target = 6
# pairs = []

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             pairs.append((nums[i], nums[j]))

# print(pairs)
# ```

# **Explanation:**

# * Loop through all unique pairs using nested loop.
# * Check if sum of each pair equals target.

# 🔧 **Use case**: Finding expense combinations that match a budget.

# ---

# ### 🛠️ 3. Flatten a Nested List

# ```python
# nested = [[1, 2], [3, 4], [5]]
# flattened = []

# for sublist in nested:
#     for item in sublist:
#         flattened.append(item)

# print(flattened)
# ```

# **Explanation:**

# * Two loops: one for each sublist, one for each item inside.

# 🧠 **Analogy**: Flattening folders into one folder.

# ---

# ## ✅ **TUPLES**

# ### 🔄 1. Group Tuples by First Element

# ```python
# data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
# grouped = {}

# for category, item in data:
#     if category not in grouped:
#         grouped[category] = []
#     grouped[category].append(item)

# print(grouped)
# ```

# **Explanation:**

# * Use a dictionary to group values by their first element (key).

# 🔧 **Use case**: Grouping products by category in inventory.

# ---

# ### 🔄 2. Convert Tuple of Lists to List of Tuples

# ```python
# t = ([1, 2], [3, 4], [5, 6])

# result = list(zip(*t))
# print(result)
# ```

# **Explanation:**

# * `zip(*t)` → transposes rows into columns.
# * Converts structure from:

#   * `([1, 2], [3, 4], [5, 6])` → `[(1, 3, 5), (2, 4, 6)]`

# 🧠 **Analogy**: Turning columns into rows in a spreadsheet.

# ---

# ## ✅ **DICTIONARIES**

# ### 🔁 1. Merge Two Dictionaries with Custom Conflict Resolution

# ```python
# a = {"x": 1, "y": 2}
# b = {"y": 3, "z": 4}

# merged = {}

# for key in set(a) | set(b):  # union of all keys
#     merged[key] = max(a.get(key, 0), b.get(key, 0))

# print(merged)
# ```

# **Explanation:**

# * Union of keys.
# * Use `.get()` with default value.
# * Choose higher value if key exists in both.

# 🧠 **Use case**: Choosing best values from two data sources.

# ---

# ### 🔍 2. Key with Maximum Value

# ```python
# data = {"Ali": 87, "Zara": 92, "Sara": 78}
# topper = max(data, key=data.get)
# print(topper)
# ```

# **Explanation:**

# * `data.get` fetches value for each key.
# * `max()` compares based on that.

# 🧠 **Use case**: Finding highest score.

# ---

# ### 🧮 3. Word Frequency Counter

# ```python
# sentence = "this is a test this is only a test"
# words = sentence.split()
# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print(freq)
# ```

# **Explanation:**

# * `.split()` breaks string into list of words.
# * `.get()` handles missing keys.

# 🧠 **Use case**: Search engine indexing or keyword analysis.

# ---

# ## ✅ **SETS**

# ### 🟰 1. Compare Two Lists (Ignore Order + Duplicates)

# ```python
# a = [1, 2, 3, 3]
# b = [3, 2, 1]

# print(set(a) == set(b))  # Output: True
# ```

# **Explanation:**

# * Sets remove duplicates and are unordered.
# * Comparing sets is ideal here.

# ---

# ### ❌ 2. Elements in A But Not in B

# ```python
# a = [1, 2, 3]
# b = [2, 3, 4]

# difference = list(set(a) - set(b))
# print(difference)  # Output: [1]
# ```

# **Explanation:**

# * Subtracting sets gives unique elements in one set.

# ---

# ### 🔁 3. Symmetric Difference

# ```python
# a = {1, 2, 3}
# b = {3, 4, 5}

# sym_diff = a ^ b
# print(sym_diff)  # Output: {1, 2, 4, 5}
# ```

# **Explanation:**

# * `^` operator gives items not in both sets.

# ---

# ## ✅ **BONUS INTEGRATED CHALLENGE**

# ```python
# students = [
#     ("Ali", 85),
#     ("Zara", 90),
#     ("Sara", 78),
#     ("Ali", 95)
# ]

# # 1. Remove duplicates, keep highest mark
# student_dict = {}

# for name, mark in students:
#     if name not in student_dict or mark > student_dict[name]:
#         student_dict[name] = mark

# # 2. Sort dictionary by marks (descending)
# sorted_students = sorted(student_dict.items(), key=lambda x: x[1], reverse=True)

# print(sorted_students)
# ```

# **Explanation:**

# * Use a dictionary to filter highest mark per student.
# * Sort with `lambda` for descending order.

# 🧠 **Use case**: Final leaderboard from raw submission logs.

# ---
