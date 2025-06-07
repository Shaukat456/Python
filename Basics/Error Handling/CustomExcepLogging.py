# ## 🧨 1. Custom Exception Classes

# ### 🔍 Why create custom exceptions?

# Built-in exceptions (like `ValueError`, `ZeroDivisionError`, etc.) are powerful, but sometimes you want more **specific** and **meaningful** error messages for your app.

# ### 🎯 Real-world Analogy:

# In a library system:

# * "Book not found" is more specific than just "Error".
# * You’d prefer to raise a **`BookNotFoundError`** rather than a generic `Exception`.

# ---

# ### ✅ Syntax of a Custom Exception

# ```python
# class MyCustomError(Exception):
#     """Custom error for special conditions."""
#     pass

# # Example usage
# def check_age(age):
#     if age < 0:
#         raise MyCustomError("Age can't be negative!")

# try:
#     check_age(-5)
# except MyCustomError as e:
#     print("Custom Error Caught:", e)
# ```

# ---

# ### 🧩 Real-World Example: Banking App

# ```python
# class InsufficientFundsError(Exception):
#     pass

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError("You don’t have enough money.")
#     return balance - amount

# try:
#     print(withdraw(500, 1000))
# except InsufficientFundsError as e:
#     print("Transaction failed:", e)
# ```

# ---

# ## 📜 2. Logging in Python

# ### 🔍 Why logging?

# In real apps, **print statements** aren’t good enough. You need a permanent, timestamped record of what happened — this is where **logging** comes in.

# ---

# ### 🧠 Analogy:

# Imagine a **security camera log** at a bank. It records:

# * When someone enters
# * If something goes wrong
# * Whether a transaction failed

# You don’t “print” it — you **log** it.

# ---

# ### ✅ Basic Logging Setup

# ```python
# import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("App started")
# logging.warning("This is a warning")
# logging.error("This is an error")
# ```

# ---

# ### 🗂 Log Levels

# | Level      | When to Use                                    |
# | ---------- | ---------------------------------------------- |
# | `DEBUG`    | Detailed info for debugging                    |
# | `INFO`     | General events (e.g., app started, logged in)  |
# | `WARNING`  | Something might go wrong                       |
# | `ERROR`    | Something went wrong                           |
# | `CRITICAL` | Serious errors (app crashing, service failure) |

# ---

# ### 📄 Logging to a File

# ```python
# logging.basicConfig(filename="app.log", level=logging.INFO)

# logging.info("User logged in")
# logging.warning("Low disk space")
# logging.error("Database not found")
# ```

# It creates a file called `app.log` with the logs inside.

# ---

# ### 🧩 Real-World Example: API Logging

# ```python
# def get_user_data(user_id):
#     try:
#         if user_id != 123:
#             raise ValueError("User not found")
#         return {"name": "Alice", "id": user_id}
#     except ValueError as e:
#         logging.error(f"Error: {e}")
#         return None

# get_user_data(404)
# ```

# ---

# ## 🧪 Capstone Task

# Create a simple **User Registration System**:

# * Raise a `UserAlreadyExistsError` if the user exists
# * Use `logging` to record every registration attempt
