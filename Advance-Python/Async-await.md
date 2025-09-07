# ---

# # 🧠 1. Why `async` / `await`?

# Normally, Python runs code **synchronously** → one task at a time.

# But what if you’re doing tasks that **wait a lot** (like downloading files, making API requests, reading from a database)?
# 👉 You don’t want your whole program to pause.
# 👉 That’s where **asynchronous programming** comes in.

# ---

# # 🔑 2. `async` Function (a.k.a *coroutine*)

# * In Python, you define an **async function** using `async def`.
# * This tells Python: *“Hey, this function can pause in the middle and let other tasks run.”*

# ### Example

# ```python
# import asyncio

# async def greet():
#     print("Hello...")
#     await asyncio.sleep(2)  # pause here, let others run
#     print("...World!")
# ```

# 👉 This function won’t block the whole program while sleeping.

# ---

# # 🔑 3. `await`

# * You use `await` to **pause** at an async operation (like waiting for a file, API, or timer).
# * While waiting, Python can run something else.
# * But ❌ you can only use `await` **inside** an `async` function.

# ---

# # ⚙️ 4. Running Async Functions

# Async functions don’t run directly — you need an **event loop** to manage them.

# ```python
# async def main():
#     await greet()

# # Start the event loop
# asyncio.run(main())
# ```

# ✅ Output:

# ```
# Hello...
# ...World!
# ```

# ---

# # 🎬 5. Multiple Async Tasks (Parallel Feel)

# Here’s the real power: run multiple tasks at once.

# ```python
# import asyncio


# async def task(name, delay):
#     print(f"Task {name} started")
#     await asyncio.sleep(delay)  # simulate waiting
#     print(f"Task {name} finished")

# async def main():
#     # Run 3 tasks "together"
#     await asyncio.gather(
#         task("A", 2),
#         task("B", 3),
#         task("C", 1),
#     )

# asyncio.run(main())
# ```

# ✅ Output:

# ```
# Task A started
# Task B started
# Task C started
# Task C finished
# Task A finished
# Task B finished
# ```

# 👉 Notice: they **overlap** instead of running one by one.
# 👉 Total time = 3s (max delay), instead of 6s (sum of all delays).

# ---

# # 🛠️ 6. Real-World Example

# ### Synchronous Downloader (bad)

# ```python
# import time

# def download(file):
#     print(f"Downloading {file}")
#     time.sleep(3)
#     print(f"Finished {file}")

# def main():
#     download("file1")
#     download("file2")
#     download("file3")

# main()
# ```

# ⏳ Takes 9 seconds.

# ---

# ### Asynchronous Downloader (good)

# ```python
# import asyncio

# async def download(file):
#     print(f"Downloading {file}")
#     await asyncio.sleep(3)
#     print(f"Finished {file}")

# async def main():
#     await asyncio.gather(
#         download("file1"),
#         download("file2"),
#         download("file3"),
#     )

# asyncio.run(main())
# ```

# ⏳ Takes only 3 seconds (all “downloading” overlaps).

# ---

# # 🔄 7. Key Takeaways

# * **`async def`** → define coroutine (special function).
# * **`await`** → pause and let other work run.
# * **`asyncio.run()`** → start the event loop.
# * **`asyncio.gather()`** → run many async tasks together.
