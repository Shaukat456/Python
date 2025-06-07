# A list is an ordered, mutable (changeable) collection of elements in Python. It is created using square brackets []. Lists can contain different data types, such as numbers, strings, and even other lists. Lists support indexing, slicing, and various operations like adding, removing, and updating elements.

s = "hello"


# Extract "ell" (from index 1 to index 4)
print(s[0:2])  # Output: "ell"

# Extract "hello" (from start to end)
print(s[:])  # Output: "hello"

# Extract "hel" (from start to index 3)
print(s[:3])  # Output: "hel"

# Extract "lo" (from index 3 to end)
print(s[3:])  # Output: "lo"

# Reverse the string
print(s[::-1])  # Output: "olleh"


my_list = [1, 2, 3, "apple", "banana"]
print(my_list)  # Output: [1, 2, 3, 'apple', 'banana']


# 📌 Key Features of Lists
# ✅ Ordered – Elements maintain their position.
# ✅ Mutable – Values can be changed after creation.
# ✅ Can contain different data types – Integers, strings, etc.
# ✅ Supports indexing and slicing – Like tuples.


#  Shopping List (Dynamic Data)
# A shopping list is modifiable, so a list is the best choice.
shopping_list = ["Milk", "Eggs", "Bread", "Butter"]
shopping_list.append("Cheese")  # Adding an item
shopping_list.remove("Eggs")  # Removing an item
print(shopping_list)


#  Why use a list?
# The list changes when we add or remove items.


# To-Do List
# A to-do list keeps track of tasks that change over time.


# tasks = ["Complete project", "Go to gym", "Read book"]
# tasks.append("Call mom")  # Adding a new task
# tasks.pop(1)  # Removing 'Go to gym'
# print(tasks)


# Student Marks in a Class
# A teacher stores students' marks in a list because they need to be updated.

marks = [85, 90, 78, 92, 88]
marks[2] = 80  # Updating a student's marks
print(marks)


# Social Media Notifications
# A social media app stores notifications in a list, adding new ones at the end.

notifications = ["New friend request", "Message from Alice", "New comment on your post"]
notifications.append("Someone liked your post")
print(notifications)


#  Queue of Customers in a Bank
# A bank uses a list to track customers in a queue.

queue = ["Customer1", "Customer2", "Customer3"]
queue.pop(0)  # First customer is served
print(queue)


#  Inventory Management in a Store
# A store tracks stock in a list and updates it when items are sold or restocked.


inventory = ["Laptop", "Mouse", "Keyboard"]
inventory.append("Monitor")  # New item added
inventory.remove("Mouse")  # Item sold out
print(inventory)


# Feature	List	Tuple
# Mutable?	✅ Yes (Can be modified)	❌ No (Cannot be modified)
# Faster?	❌ No (More memory)	✅ Yes (Less memory)
# Use Case	Changing data (tasks, notifications)	Fixed data (coordinates, RGB values)


# Using a for Loop with Lists
# Example 1: Print Each Item in a List (Basic Example)

fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit)


# tasks = ["Wake up", "Exercise", "Study", "Work"]

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")


# Filtering Even Numbers from a List
numbers = [10, 15, 20, 25, 30, 35, 40]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
# Filtering Names Starting with 'A'
names = ["Alice", "Bob", "Charlie", "Anna", "David"]

names_starting_with_a = []
for name in names:
    if name.startswith("A"):
        names_starting_with_a.append(name)

print("Names starting with 'A':", names_starting_with_a)


# List Comprehension Example
# Example: Create a List of Squares of Even Numbers
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]

print("Squares of even numbers:", squares_of_evens)

# List Comprehension with Strings

# Example: Create a List of Lengths of Each Word in a Sentence
sentence = "Python is fun and powerful"
word_lengths = [len(word) for word in sentence.split()]
print("Lengths of each word:", word_lengths)

# List Comprehension with Nested Lists
# Example: Flatten a List of Lists

nested_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = [item for sublist in nested_list for item in sublist]

print("Flattened list:", flattened_list)

# List Comprehension with Conditional Logic
# Example: Create a List of Odd Numbers from 1 to 20
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]

print("Odd numbers from 1 to 20:", odd_numbers)
# List Comprehension with String Manipulation

# Example: Create a List of Uppercase Words from a Sentence
sentence = "Python is fun and powerful"
uppercase_words = [word.upper() for word in sentence.split() if len(word) > 2]
print("Uppercase words with more than 2 letters:", uppercase_words)

# List Comprehension with Functions
# Example: Create a List of Square Roots of Numbers from 1 to 10

import math

square_roots = [math.sqrt(x) for x in range(1, 11)]
print("Square roots of numbers from 1 to 10:", square_roots)

# List Comprehension with Multiple Conditions
# Example: Create a List of Numbers from 1 to 50 that are Divisible by 3 and 5

divisible_by_3_and_5 = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print("Numbers from 1 to 50 divisible by 3 and 5:", divisible_by_3_and_5)
