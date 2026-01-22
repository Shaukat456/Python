# ---

# # Big picture (one minute)

# \* **Synchronous (sync)**: do one thing at a time, in order. Simple, reliable.

# * **Asynchronous (asyncio)**: one worker that *switches\* between many waiting tasks (great for networking). Cooperative: tasks yield with `await`.

# \* **Threads**: many workers **inside one process** sharing memory. Good for I/O. In CPython, the **GIL** means only one thread runs Python bytecode at a time.

# \* **Processes**: many **separate Python interpreters** (separate memory). True parallel CPU work. Heavier but bypasses GIL.

# **Rule of thumb**

# \* Lots of waiting (network, disk, APIs)? → **Async** (or **Threads** if libraries aren’t async-friendly).

# \* Lots of CPU math (image/video/ML, big loops)? → **Processes**.

# \* Simple script / few tasks? → **Sync**.

# ---

# # 1) Synchronous (blocking) — “one queue, one clerk”

# **Analogy:** You stand in one line; the clerk serves you fully before the next person.

# ```python

# import time

# def task(name, secs):

# print(f"Start {name}")

# time.sleep(secs) # blocks here

# print(f"End {name}")

# task("A", 2)

# task("B", 2) # starts only after A finishes

# ```

# **When to use:** teaching basics, small scripts, or when you don’t need overlap.

# **Pros:** easiest to reason about.

# **Cons:** slow for many I/O tasks.

# ---

# # 2) Asynchronous (asyncio) — “token system; work overlaps while you wait”

# **Analogy:** At a fast-food counter you place an order (task gets a token). While your order cooks (waiting), the system serves others. One cook, but very efficient scheduling.

# Key ideas:

# \* `async def` defines a coroutine.

# \* `await` yields control so other tasks can run.

# \* Best with **non-blocking** libraries (e.g., `aiohttp`).

# ```python

# import asyncio

# async def task(name, secs):

# print(f"Start {name}")

# await asyncio.sleep(secs) # non-blocking wait

# print(f"End {name}")

# async def main():

# await asyncio.gather(

# task("A", 2),

# task("B", 2),

# task("C", 1),

# )

# asyncio.run(main())

# ```

# **When to use:** many concurrent **I/O-bound** jobs (HTTP requests, sockets, chat servers).

# **Pros:** huge concurrency with low overhead.

# **Cons:** needs async-friendly libs; blocking calls will freeze the loop.

# **Important:** If you _must_ call a blocking function, wrap it:

# ```python

# import asyncio, time

# def blocking_io():

# time.sleep(2) # blocks!

# return "done"

# async def main():

# result = await asyncio.to_thread(blocking_io) # run blocking in a thread

# print(result)

# asyncio.run(main())

# ```

# ---

# # 3) Threads — “many waiters in the same restaurant (shared kitchen)”

# **Analogy:** Several waiters (threads) serve customers. They share the same kitchen (memory). Great when most time is spent waiting on ovens (I/O).

# ```python

# import time

# from concurrent.futures import ThreadPoolExecutor

# def download(name, secs):

# print(f"Start {name}")

# time.sleep(secs) # simulates I/O wait

# print(f"End {name}")

# return name

# with ThreadPoolExecutor(max_workers=5) as pool:

# results = list(pool.map(download, ["A","B","C","D","E"], [2,2,1,3,1]))

# print(results)

# ```

# **When to use:** I/O-bound work with blocking libraries (e.g., `requests`, DB drivers).

# **Pros:** easy drop-in speed-up for I/O; simple API (`ThreadPoolExecutor`).

# **Cons:** CPython’s **GIL** limits CPU parallelism; need to guard shared data (locks).

# **Safety tools:** `queue.Queue`, `threading.Lock`, `concurrent.futures`.

# **Avoid pitfalls:** race conditions (two threads writing same variable), deadlocks (two threads waiting on each other). Use queues to pass data safely.

# ---

# # 4) Processes — “many kitchens (separate restaurants)”

# **Analogy:** Each process is its own restaurant with its own kitchen and staff. No shared memory by default → fewer accidental conflicts. Good for heavy cooking (CPU).

# ```python

# from concurrent.futures import ProcessPoolExecutor

# import math

# def cpu_heavy(n):

# # toy CPU work

# total = 0

# for i in range(1, n):

# total += math.sqrt(i)

# return total

# if **name** == "**main**": # important on Windows

# with ProcessPoolExecutor() as pool:

# results = list(pool.map(cpu_heavy, [5_000_00, 6_000_00, 7_000_00, 8_000_00]))

# print(len(results), "results")

# ```

# **When to use:** **CPU-bound** tasks (image filters, video transcoding, numerical loops).

# **Pros:** true parallelism; bypasses GIL.

# **Cons:** heavier start-up; data must be **pickled** to cross process boundaries; careful with large data copies (use shared memory or memory-mapped files if needed).

# ---

# ## Real-world scenarios (what to pick?)

# 1. **Web scraper hitting 1000 URLs**

# \* Use **asyncio + aiohttp** (best) or **threads + requests** (good).

# \* Avoid processes (network I/O won’t benefit much).

# 2. **Generate thumbnails for 2000 photos**

# \* Use **ProcessPoolExecutor** (CPU-bound imaging).

# \* Threads won’t help due to GIL (unless the image library releases GIL in C).

# 3. **Chat server / WebSockets**

# \* Use **asyncio** (thousands of sockets, minimal threads/processes).

# 4. **ETL pipeline: download → parse → compute-heavy transform → upload**

# \* **asyncio** for download/upload, then hand off transforms to a **process pool**, e.g. `await loop.run_in_executor(process_pool, heavy_fn, data)` or in modern Python combine with `asyncio.get_running_loop()` and `ProcessPoolExecutor`.

# ---

# ## Concurrency vs Parallelism (clear and crisp)

# * **Concurrency**: dealing with many things *at once\* (overlapping). Achieved by **async** or **threads** (even on one CPU).

# * **Parallelism**: doing many things *at the same instant\* on multiple CPUs. Achieved by **processes** (or C extensions that release GIL).

# ---

# ## Blocking vs Non-blocking

# \* **Blocking**: call doesn’t return until work is done (`time.sleep`, `requests.get`).

# \* **Non-blocking/awaitable**: call yields control and resumes later (`await asyncio.sleep`, `await session.get(...)` with aiohttp).

# ---

# ## Common pitfalls (and fixes)

# \* **Blocking inside async**: freezes the event loop.

# * **Fix:** `await asyncio.to_thread(blocking_fn, *args)` or use proper async libs.

# \* **Race conditions in threads**: unsafely shared state.

# \* **Fix:** use `queue.Queue`, `threading.Lock`, avoid sharing mutable state.

# \* **Pickling errors in processes**: functions not at top-level, lambda closures, unpicklable objects.

# \* **Fix:** define worker functions at module top; pass plain data.

# \* **Too many tasks**: 10k threads/processes will thrash.

# \* **Fix:** use bounded pools; batch work; for asyncio use semaphores.

# ---

# ## Quick decision guide

# \* **I/O, async-friendly libs available?** → **asyncio**

# \* **I/O, blocking libs only?** → **ThreadPoolExecutor**

# \* **CPU-bound?** → **ProcessPoolExecutor**

# \* **Tiny script / few tasks?** → **Sync** (keep it simple)

# ---

# ## Minimal templates to teach

# **Async HTTP (conceptual skeleton):**

# ```python

# # pip install aiohttp

# import asyncio, aiohttp

# async def fetch(session, url):

# async with session.get(url) as r:

# return await r.text()

# async def main(urls):

# async with aiohttp.ClientSession() as session:

# texts = await asyncio.gather(\*(fetch(session, u) for u in urls))

# print(len(texts))

# asyncio.run(main(["https://example.com"]\*10))

# ```

# **Threads with blocking I/O:**

# ```python

# from concurrent.futures import ThreadPoolExecutor

# import requests

# def fetch(url):

# return requests.get(url, timeout=10).text

# with ThreadPoolExecutor(max_workers=20) as pool:

# pages = list(pool.map(fetch, ["https://example.com"]\*10))

# print(len(pages))

# ```

# **Processes for CPU:**

# ```python

# from concurrent.futures import ProcessPoolExecutor

# def heavy(x):

# # CPU-bound work here

# return sum(i\*i for i in range(x))

# if **name** == "**main**":

# with ProcessPoolExecutor() as pool:

# results = list(pool.map(heavy, [2_000_000]\*4))

# print(sum(results))

# ```

# **Mixing async + threads (wrap blocking call):**

# ```python

# import asyncio, time

# def blocking():

# time.sleep(2)

# return "OK"

# async def main():

# # run 5 blocking tasks concurrently using threads

# results = await asyncio.gather(\*(asyncio.to*thread(blocking) for * in range(5)))

# print(results)

# asyncio.run(main())
