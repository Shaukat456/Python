Let’s move to the **NumPy Random Module** — one of the most powerful and fun parts of NumPy.
It’s super useful in **games, simulations, AI, data science, and testing**.

---

# 🎲 1. Random Numbers (Basic)

```python
import numpy as np

print("Random Float between 0 and 1:", np.random.rand())
print("5 Random Floats:", np.random.rand(5))
print("2x3 Matrix of Random Floats:\n", np.random.rand(2,3))
```

✅ Example Output:

```
Random Float between 0 and 1: 0.732
5 Random Floats: [0.12 0.98 0.45 0.67 0.23]
2x3 Matrix:
 [[0.43 0.65 0.12]
  [0.88 0.33 0.79]]
```

⚡ **Real World Use:**

- Simulating coin tosses or dice rolls.
- Creating random test data.

---

# 🎲 2. Random Integers

```python
print("Random Integer (0-10):", np.random.randint(0, 10))
print("5 Random Integers (1-100):", np.random.randint(1, 100, 5))
print("2x2 Random Integers:\n", np.random.randint(10, 50, (2,2)))
```

✅ Output:

```
Random Integer (0-10): 7
5 Random Integers: [34 98 21 65 43]
2x2 Random Integers:
 [[12 44]
  [25 33]]
```

⚡ **Real World Use:**

- Simulating lottery tickets.
- Generating random student roll numbers.

---

# 🎲 3. Random Choice (Picking from a List)

```python
students = ["Ali", "Sara", "John", "Fatima", "David"]

print("Random Student:", np.random.choice(students))
print("Pick 3 Students Randomly:", np.random.choice(students, 3, replace=False))
```

✅ Output:

```
Random Student: Fatima
Pick 3 Students Randomly: ['John' 'Ali' 'Sara']
```

⚡ **Real World Use:**

- Randomly selecting students for presentation.
- Picking a random sample from a dataset.

---

# 🎲 4. Random Seed (Reproducibility)

If you want **same random numbers every time**, set a seed:

<!-- Seed Explain -->

```python
np.random.seed(42)
print(np.random.randint(1, 10, 5))
```

✅ Output (always same):

```
[7 4 8 5 7]
```

⚡ **Real World Use:**

- Important in **machine learning experiments** so results are consistent.

---

# 🎲 5. Random Distributions

NumPy can generate data following **real-world probability distributions**.

## Normal Distribution (bell curve)

```python
data = np.random.normal(50, 10, 5)  # mean=50, std=10, size=5
print(data)
```

✅ Example Output:

```
[48.3 56.7 42.1 51.4 59.8]
```

⚡ **Real World Use:**

- Heights of people, exam scores, measurement errors usually follow normal distribution.

---

# 🎮 Real-World Example: Dice Game

```python
dice = np.random.randint(1, 7, 2)  # roll two dice
print("You rolled:", dice, "Total:", dice.sum())
```

✅ Output:

```
You rolled: [3 6] Total: 9
```

---

# 📝 Exercises for You

1. Simulate tossing a coin 10 times (Head = 1, Tail = 0).
2. Generate random exam scores for 30 students (out of 100). Find average & highest score.
3. Create a random 3x3 matrix of integers between 1 and 50.
4. Use `np.random.choice` to randomly select 5 winners from a list of 20 participants.
