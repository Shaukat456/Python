# Approaching problems—especially in programming—can be intimidating for beginners. But with the right mindset and structured steps, it becomes easier and even fun. Here's a **step-by-step approach** that helps build logic, avoid confusion, and eventually write clean, working code.

# ---

# ### 🧭 1. **Understand the Problem**

# Before you touch the keyboard, **read the problem carefully**.

# 🔍 Ask:

# * What is the input?
# * What is the expected output?
# * Are there any constraints or edge cases?
# * Can I visualize this problem with a real-life example?

# 📌 Example:
# Problem: "Return the second largest number from a list."

# * Input: `[4, 1, 7, 3, 9]`
# * Output: `7`

# ---

# ### 🧱 2. **Break It Down (Decompose)**

# Split the problem into **smaller subproblems**.

# 🧩 Example (second largest):

# * Sort the list.
# * Remove the largest.
# * Return the next one.

# ---

# ### 🧠 3. **Think in Logic, Not Code First**

# Don’t start writing code yet. Think how **you’d solve this manually**.

# ✏️ Write a rough logic in plain English or pseudocode:

# ```
# 1. Sort the list in descending order.
# 2. Return the second element.
# ```

# ---

# ### 🔄 4. **Start With Simple Inputs**

# Try dry-running your logic on paper with **simple inputs**.

# 📋 Example:
# List: `[3, 8, 1, 6]`
# Sorted: `[8, 6, 3, 1]`
# Second largest: `6`

# ---

# ### 🧪 5. **Code a Basic Version First**

# Once you're confident, write a **working, even if ugly, version**.

# ```python
# numbers = [3, 8, 1, 6]
# numbers.sort(reverse=True)
# print(numbers[1])  # Output: 6
# ```

# ---

# ### 🛡️ 6. **Handle Edge Cases**

# Test your code with special inputs:

# * Empty list?
# * All numbers are the same?
# * Only one number?

# ---

# ### 🧼 7. **Optimize & Clean**

# * Can you make it faster?
# * Can it use less memory?
# * Make your code **readable** and **comment** where needed.

# ---

# ### 🔁 8. **Practice with Similar Problems**

# Once you solve one, solve 3 more similar problems. This builds **muscle memory**.

# ---

# ### Real-Life Analogy:

# Imagine solving a **puzzle**:

# * First, look at the picture (problem).
# * Then group similar pieces (subproblems).
# * Build the border (simple logic).
# * Fit the tricky pieces (edge cases).
# * Admire your work (optimize).


## ✅ **Problem**

# You’re given a list of items (could be numbers or strings). Return the item that appears the most.

# ### Example:

# ```python
# Input: [1, 3, 2, 1, 4, 1, 3, 3, 3]
# Output: 3  # appears 4 times
# ```

# ---

# ## 🧭 Step-by-Step Breakdown (Real-World Style)

# ### 🔍 Step 1: **Understand the Problem**

# * You have a list (like a survey of favorite fruits).
# * You want to know which fruit was picked the most.

# Think of a real case:

# > Your teacher asked 10 students their favorite color. Now you need to figure out which color was chosen the most.

# ---

# ### 🧩 Step 2: **Break it Down**

# * Count how many times each item appears.
# * Keep track of the highest count and its item.
# * Return that item.

# ---

# ### 🧠 Step 3: **Think in Plain Language (Pseudocode)**

# ```
# 1. Create an empty dictionary to store counts.
# 2. For each element in the list:
#    - If it's already in the dictionary, increase the count.
#    - Otherwise, set its count to 1.
# 3. Find the item with the highest count.
# 4. Return that item.
# ```

# ---

# ## 💻 Step 4: Code It!

# ```python
# def most_frequent_element(lst):
#     frequency = {}

#     for item in lst:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1

#     max_count = 0
#     most_frequent = None

#     for item, count in frequency.items():
#         if count > max_count:
#             max_count = count
#             most_frequent = item

#     return most_frequent

# # Example usage
# print(most_frequent_element([1, 3, 2, 1, 4, 1, 3, 3, 3]))
# ```

# ---

# ## 💡 Real-World Analogy

# > Imagine you’re running a fast-food chain. Every order has a list of items. You want to know which item is most frequently ordered. You keep a notebook and tally each item. At the end of the day, you look for the one with the highest tally.

# ---

# ## 🛡️ Edge Cases to Think About

# 1. What if the list is empty?
# 2. What if multiple items have the same highest frequency?
# 3. What if all items appear once?

# You can modify the function to handle those later as an improvement.

# ---


# simplest way to add two lists element-wise in Python with named indices

# Define lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
indices = ["A", "B", "C", "D", "E"]

# Perform element-wise addition
result = {}
for i in range(len(list1)):
    result[indices[i]] = list1[i] + list2[i]

# Print the result
print(result)

# Prime Number using for loop

num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")

# Prime Number using while loop

num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False

else:
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")


def is_prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")

# Prime Number using for loop


# Factorial of a number

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}.")


#  Factorial of a number using while loop

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is {factorial}.")


#  Factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}.")


#  Fibonacci series using for loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#  Fibonacci series using while loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1

i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1


#  Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i), end=" ")


#  Sum of natural numbers using for loop
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i


# Largest Number in a List
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")

# Smallest Number in a List
numbers = [10, 20, 30, 40, 50]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(f"The smallest number is {smallest}.")


#  Sum of natural numbers using while loop
n = int(input("Enter a number: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"The sum of natural numbers up to {n} is {total}.")


#  Sum of natural numbers using recursion
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


num = int(input("Enter a number: "))
result = sum_natural(num)
print(f"The sum of natural numbers up to {num} is {result}.")

#  Sum of natural numbers using formula
num = int(input("Enter a number: "))
total = num * (num + 1) // 2
print(f"The sum of natural numbers up to {num} is {total}.")


# Sorting a list using for loop (Bubble Sort Algorithm)

# Bubble sort algorithm
# Bubble Sort is a simple algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the
# list is repeated until the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

#  Bubble Sort Algorithm
# 1. Start with the first element in the list.
# 2. Compare the current element with the next element.
# 3. If the current element is greater than the next element, swap them.
# 4. Move to the next element and repeat steps 2 and 3.
# 5. Continue this process until the list is sorted.


numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


print("Sorted list:", numbers)

# step 1: [34, 25, 12, 22, 11, 64, 90]
# step 2: [25, 12, 22, 11, 34, 64, 90]
# step 3: [12, 22, 11, 25, 34, 64, 90]
# step 4: [12, 11, 22, 25, 34, 64, 90]
# step 5: [11, 12, 22, 25, 34, 64, 90]
# step 6: [11, 12, 22, 25, 34, 64, 90]
# step 7: [11, 12, 22, 25, 34, 64, 90]


#  Sorting a list using while loop (Bubble Sort Algorithm)
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        j += 1
    i += 1

print("Sorted list:", numbers)


# Length of a string using for loop

text = input("Enter a string: ")
length = 0
for char in text:
    length += 1
print(f"The length of the string is: {length}")


# Length of a string using while loop
text = input("Enter a string: ")
length = 0
i = 0

while i < len(text):
    length += 1
    i += 1

print(f"The length of the string is: {length}")
