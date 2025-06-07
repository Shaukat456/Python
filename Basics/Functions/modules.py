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
# import math

# print(math.sqrt(16))  # 4.0
# ```

# ---

# ## 🧩 Custom Modules (your own .py file)

# ### Step-by-step:

# 1. **Create a Python file** called `utils.py`

# ```python
# # utils.py

# def greet(name):
#     return f"Hello, {name}!"
# ```

# 2. **Use it in another file**

# ```python
# # main.py

# import utils

# print(utils.greet("Ali"))  # Output: Hello, Ali!
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

# print(pi)        # 3.14159
# print(sqrt(9))   # 3.0
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
# def area_square(side):
#     return side * side

# def area_circle(radius):
#     import math
#     return math.pi * radius * radius
# ```

# 2. File: `main.py`

# ```python
# import shapes

# print(shapes.area_square(4))
# print(shapes.area_circle(5))
# ```

# ---
