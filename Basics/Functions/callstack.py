# Alright — let’s go **deep** into the **call stack**, starting from zero so you really understand how it works with *any* function, not just recursion.

# ---

# ## 🧠 1. What is the Call Stack?

# The **call stack** is:

# * A special area in memory
# * Used by Python (and other languages) to **keep track of function calls**
# * Works in a **Last In, First Out (LIFO)** way
#   → the last function called is the first to finish

# ---

# ## 🧱 2. Why Does Python Need It?

# When you call a function:

# 1. Python must **pause** the current work.
# 2. It **remembers**:

#    * Where to return after the function finishes
#    * The function’s local variables & parameters
# 3. It **pushes** this info onto the stack.

# When the function finishes:

# 1. Python **pops** it off the stack.
# 2. Goes back to the function underneath.

# ---

# ## 🍕 3. Real-Life Analogy

# Imagine you’re making a pizza:

# 1. You start **rolling dough**.
# 2. You stop because you need **tomato sauce** → start cooking sauce.
# 3. While cooking sauce, you remember you need to **cut tomatoes** → start cutting.
# 4. When tomatoes are done → go back to sauce → finish → go back to dough.

# Your brain **remembers tasks in reverse order**.
# That’s exactly what the call stack does.

# ---

# ## 🐍 4. Example in Python (No Recursion Yet)

# ```python
# def greet():
#     print("Hello!")

# def welcome():
#     greet()
#     print("Welcome!")

# def start():
#     welcome()
#     print("Let's begin!")

# start()
# ```

# ---

# ### **How the Call Stack Changes:**

# **Step 1:** Call `start()`

# ```
# Top → start()
# ```

# **Step 2:** Inside `start()`, call `welcome()`

# ```
# Top → welcome()
#        start()
# ```

# **Step 3:** Inside `welcome()`, call `greet()`

# ```
# Top → greet()
#        welcome()
#        start()
# ```

# **Step 4:** `greet()` prints "Hello!" → done → pop `greet()`

# ```
# Top → welcome()
#        start()
# ```

# **Step 5:** `welcome()` prints "Welcome!" → done → pop `welcome()`

# ```
# Top → start()
# ```

# **Step 6:** `start()` prints "Let's begin!" → done → pop `start()`

# ```
# [Stack is now empty]
# ```

# ---

# ## 🔄 5. In Short:

# * **Push** (add to top) when calling a function
# * **Pop** (remove from top) when function finishes
# * Only the **top function** is running at any moment

# ---

# ## ⚠️ 6. Common Pitfalls:

# * **Infinite recursion** → stack never pops → “RecursionError: maximum recursion depth exceeded”
# * Deeply nested function calls → memory heavy
# * Forgetting return paths → unexpected results

# ---
