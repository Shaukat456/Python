# ## 🧠 What is Error Handling?

# When your program encounters something unexpected — like a wrong input, a missing file, or a math error — it stops (crashes) and shows a **traceback**.

# But with **error handling**, you can catch those errors and decide what to do next — like showing a message instead of crashing.

# ---

# ## 🔍 Real-Life Analogy

# Imagine you're withdrawing cash from an ATM.

# If there's **no internet**, it **doesn't crash** — it shows:

# > "Sorry, the transaction cannot be completed right now."

# Python’s error handling works similarly — instead of crashing, you **gracefully handle** errors.

# ---

# ## ✅ The Basic Structure: `try` / `except`

# ```python

# try:

# # risky code here

# x = int(input("Enter a number: "))

# result = 10 / x

# print("Result:", result)

# except ZeroDivisionError:

# print("You can't divide by zero!")

# except ValueError:

# print("Please enter a valid number!")

# ```

# ### 🔁 Explanation:

# \* `try`: Run the code that **might** cause an error.

# \* `except`: Catch a specific error and handle it.

# \* You can catch **multiple** types of errors.

# ---

# ## 📚 Common Exceptions in Python

# | Error | When It Happens |

# | ------------------- | ----------------------------------------------------- |

# | `ZeroDivisionError` | Dividing by zero |

# | `ValueError` | Wrong type of value (e.g., converting `"abc"` to int) |

# | `TypeError` | Incompatible types (e.g., `"5" + 2`) |

# | `IndexError` | List index out of range |

# | `KeyError` | Accessing a missing key in a dictionary |

# | `FileNotFoundError` | Trying to open a file that doesn’t exist |

# ---

# ## 🛠 Real-World Example: Handling File Read

# ```python

# try:

# with open("data.txt", "r") as file:

# content = file.read()

# print(content)

# except FileNotFoundError:

# print("The file was not found. Please check the name.")

# ```

# ### 🧠 Analogy:

# Just like a librarian tells you a book isn’t available rather than quitting their job, Python tells you the file isn't there instead of crashing.

# ---

# ## 🔁 Using `else` and `finally`

# ```python

# try:

# num = int(input("Enter a number: "))

# print("You entered:", num)

# except ValueError:

# print("That's not a number.")

# else:

# print("No error occurred!")

# finally:

# print("This will run no matter what.")

# ```

# ### ✅ Summary:

# \* `try`: code that might break

# \* `except`: what to do if it breaks

# \* `else`: runs **if no exception**

# \* `finally`: **always** runs (cleanup, closing files, etc.)

# ---

# ## 🧪 Raising Your Own Errors (Advanced)

# ```python

# age = -5

# if age < 0:

# raise ValueError("Age cannot be negative")

# ```

# You can use `raise` to throw an error if **your custom rule is violated**.

# 🧠 Use case: Web forms, authentication systems, scientific inputs, etc.

# ---

# ## 🧩 Capstone Challenge (All Concepts)

# ```python

# def divide(a, b):

# try:

# result = a / b

# except ZeroDivisionError:

# return "Error: Cannot divide by zero"

# except TypeError:

# return "Error: Invalid types"

# else:

# return f"Success: {result}"

# finally:

# print("End of operation")

# print(divide(10, 2)) # Success

# print(divide(10, 0)) # Division error

# print(divide("10", "2")) # Type error

# ```

# ---
