# ## 🧠 What is a Module?

# A **module** is just a **file** that contains Python code — **functions**, **variables**, and **classes** — which you can use in other programs by importing it.

# > 📂 Any Python file with a `.py` extension is a module.

# ---

# ## 📦 Why use modules?

# ### Real-world analogy:

# Imagine a **toolbox**. Instead of keeping every tool (screwdriver, hammer, etc.) in your pocket, you organize them in a toolbox.

# In coding:

# * You keep your tools (functions, classes) in a **module**
# * Then you **import** only what you need

# ---

# ## ✅ Built-in Modules

# Python comes with many built-in modules like:

# | Module     | Purpose                        |
# | ---------- | ------------------------------ |
# | `math`     | Math operations                |
# | `random`   | Generate random numbers        |
# | `datetime` | Deal with dates and times      |
# | `os`       | Interact with operating system |
# | `sys`      | Access system-specific params  |

# ### Example:

# ```python
import math

print(math.sqrt(16))  # 4.0
# ```

# ---

# ## 🧩 Custom Modules (your own .py file)

# ### Step-by-step:

# 1. **Create a Python file** called `utils.py`

# ```python
# # utils.py

def greet(name):
    return f"Hello, {name}!"
# ```

# 2. **Use it in another file**

# ```python
# # main.py

import utils

print(utils.greet("Ali"))  # Output: Hello, Ali!
# ```

# > This is how teams separate code into modules like `auth.py`, `db.py`, `email.py`, etc.

# ---

# ## 🎯 Ways to Import

# | Syntax                         | Use Case                               |
# | ------------------------------ | -------------------------------------- |
# | `import module`                | General usage                          |
# | `import module as alias`       | Shorter reference                      |
# | `from module import something` | Import specific part                   |
# | `from module import *`         | Imports everything (⚠ not recommended) |

# ### Example:

# ```python
# from math import pi, sqrt

print(pi)        # 3.14159
print(sqrt(9))   # 3.0
# ```

# ---

# ## 📁 Organizing Modules in Folders (Packages)

# If you have a folder:

# ```
# project/
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py
# ```

# You can import like this:

# ```python
# from project.math_utils import add
# ```

# > `__init__.py` turns the folder into a "package" Python can recognize.

# ---

# ## 🛠 Real-world Use Case: Calculator Project

# 1. `math_utils.py` → basic math functions
# 2. `main.py` → imports `math_utils` and uses it

# ---

# ## 🧪 Practice Task for You

# ### Create your own module:

# 1. File: `shapes.py`

# ```python
def area_square(side):
    return side * side

def area_circle(radius):
    import math
    return math.pi * radius * radius
# ```

# 2. File: `main.py`

# ```python
import shapes

print(shapes.area_square(4))
print(shapes.area_circle(5))
# ```

# ---


# importing modules in Python is a way to organize and reuse code effectively. Here’s a quick guide on how to create and use modules, along with some practical examples.


# ```python
if __name__ == "__main__":
# ```

# Let’s break it down in simple terms — with **clear explanation, analogy, and use cases**.

# ---

# ## 🧠 What is `__name__ == "__main__"` in Python?

# In Python, every file (module) has a built-in variable called `__name__`.

# * If the file is **being run directly**, `__name__` is set to `"__main__"`.
# * If the file is **being imported as a module**, `__name__` is set to the **module name** (i.e., filename without `.py`).

# ---

# ## 🧩 Analogy

# Think of Python files as **TV channels**.

# * When you're **watching directly**, it says: "You're watching *Live Now*" → `__name__ == "__main__"`
# * When you're **recording the show to use later**, it doesn't say *Live Now*. It's just part of another collection → `__name__ != "__main__"`

# ---

# ## 💡 Why Use It?

# ### ✅ To prevent some code from running **when the file is imported**.

# Here’s a small example:

# ```python
# # file: math_utils.py

def add(a, b):
    return a + b

# print("This runs no matter what")

if __name__ == "__main__":
    print("This runs only when this file is executed directly")
    print(add(2, 3))
# ```

# Now:

# ### ✔ When you run this file directly:

# ```bash
# $ python math_utils.py
# ```

# Output:

# ```
# This runs no matter what
# This runs only when this file is executed directly
# 5
# ```

# ### ❌ When you import it in another file:

# ```python
# # file: main.py
# import math_utils
# ```

# Output:

# ```
# This runs no matter what
# ```

# But it **does not run**:

# ```
# This runs only when this file is executed directly
# ```

# ---

# ## 🧰 Use Cases

# 1. ✅ Testing the script independently (e.g., testing functions)
# 2. ✅ Creating reusable modules without unwanted execution
# 3. ✅ Preventing side effects during imports
# 4. ✅ Good practice for CLI (command-line interface) scripts

# ---

# ## 🛠 Real Project Use Example

# ```python
# # file: utils/logger.py

# def log_info(msg):
#     print(f"[INFO]: {msg}")

# if __name__ == "__main__":
#     print("Testing logger...")
#     log_info("This is a test log")
# ```

# Now `logger.py` can be reused across projects, and still be tested alone.

# ---

# ## 🧠 Summary

# | Action                    | `__name__` value |
# | ------------------------- | ---------------- |
# | File run directly         | `"__main__"`     |
# | File imported as a module | `"module_name"`  |

# ```python
# if __name__ == "__main__":
#     # this block only runs if the file is executed directly
# ```

# ---
