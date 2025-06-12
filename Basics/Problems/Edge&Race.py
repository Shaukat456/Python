# Great question! Let's break this down in simple, practical terms so even a beginner can understand.

# ---

# ## ✅ **What are Edge Cases?**

# **Edge cases** are **rare or extreme situations** that your program might face — usually at the "edges" or limits of what’s expected.

# Think of it like stress-testing your program to see if it can **handle the unexpected**.

# ---

# ### 🔍 Real-World Analogy:

# Imagine you’re testing a vending machine.

# * **Normal case:** Someone inserts 50 rupees and buys chips.
# * **Edge case:** What if someone inserts 0 rupees?
# * **Edge case:** What if someone inserts 10,000 rupees?
# * **Edge case:** What if the item is out of stock?

# > Edge cases are the things that **don’t happen often**, but when they do, your program should be ready.

# ---

# ### 🧪 Common Edge Cases in Python

# | Scenario                      | Example                                    |
# | ----------------------------- | ------------------------------------------ |
# | Empty input                   | `[]`, `''`, `{}`                           |
# | Extremely large input         | A list with millions of items              |
# | All items are the same        | `[1,1,1,1]`                                |
# | All items are different       | `[1,2,3,4]`                                |
# | Negative numbers              | `[-5, -10]`                                |
# | Special characters in strings | `"Hello@123"`                              |
# | Division by zero              | `x / 0` (causes error)                     |
# | Incorrect data types          | Passing a string when a number is expected |

# ---

# ## 🚨 What is a Race Condition?

# A **race condition** happens **when two or more operations happen at the same time** and the outcome **depends on the order** in which they complete.

# ---

# ### 🏁 Real-World Analogy:

# Imagine two people trying to **withdraw money from the same bank account** at the exact same time.

# * The balance is \$100.
# * Person A checks: sees \$100.
# * Person B also checks: sees \$100.
# * Both withdraw \$100.
# * The system ends up allowing \$200 withdrawal from a \$100 account. ❌

# > This is a **race condition** – two processes race to do something, and the outcome is **unpredictable**.

# ---

# ### 🧠 In Python (usually with threads):

# ```python
# import threading

# balance = 100

# def withdraw():
#     global balance
#     for _ in range(100000):
#         balance -= 1

# t1 = threading.Thread(target=withdraw)
# t2 = threading.Thread(target=withdraw)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(balance)  # Expected 0, might not be due to race condition
# ```

# ---

# ## 🛡️ How to Handle These?

# * **Edge cases:** Use if/else, input validation, testing.
# * **Race conditions:** Use `threading.Lock()`, `synchronization`, `atomic operations`, or switch to `async` if needed.
