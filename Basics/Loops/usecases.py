# usecases.py
# When to Use While Loop vs For Loop - Comprehensive Guide

"""
WHILE LOOP vs FOR LOOP DECISION GUIDE

This file covers:
1. When to use while loops vs for loops
2. Scenarios where only while loops work
3. Scenarios where only for loops work
4. Comparative examples with both approaches
5. Performance considerations
6. Best practices and decision flowchart
"""

print("=" * 80)
print("WHILE LOOP vs FOR LOOP: WHEN TO USE WHAT")
print("=" * 80)
print()

# ===== FUNDAMENTAL DIFFERENCES =====
print("🔸 FUNDAMENTAL DIFFERENCES")
print("-" * 50)
print()

print("FOR LOOP CHARACTERISTICS:")
print("✓ Used for iterating over sequences (lists, strings, ranges)")
print("✓ Number of iterations usually known in advance")
print("✓ Automatic iteration management")
print("✓ Built-in iterator protocol")
print("✓ More Pythonic for collection processing")
print()

print("WHILE LOOP CHARACTERISTICS:")
print("✓ Used when condition-based iteration is needed")
print("✓ Number of iterations unknown in advance")
print("✓ Manual iteration control")
print("✓ Flexible exit conditions")
print("✓ Better for event-driven or state-based logic")
print()

# ===== WHEN TO USE FOR LOOPS =====
print("🔸 WHEN TO USE FOR LOOPS")
print("-" * 50)
print()

print("SCENARIO 1: Iterating Over Collections")
print("-" * 30)
print("✅ USE FOR LOOP when you have a collection to process")

# Good use of for loop
fruits = ["apple", "banana", "cherry", "date"]
print("Processing fruits with FOR loop:")
for fruit in fruits:
    print(f"Processing: {fruit}")
print()

# Awkward with while loop
print("Same task with WHILE loop (awkward):")
fruits_copy = fruits.copy()
index = 0
while index < len(fruits_copy):
    fruit = fruits_copy[index]
    print(f"Processing: {fruit}")
    index += 1
print("→ FOR loop is clearly better for this scenario")
print()

print("SCENARIO 2: Range-Based Iteration")
print("-" * 30)
print("✅ USE FOR LOOP for counting or range-based tasks")

print("Counting with FOR loop:")
for i in range(1, 6):
    print(f"Count: {i}")
print()

print("Same with WHILE loop (more verbose):")
i = 1
while i <= 5:
    print(f"Count: {i}")
    i += 1
print("→ FOR loop is more concise and less error-prone")
print()

print("SCENARIO 3: Dictionary and Set Processing")
print("-" * 30)
print("✅ USE FOR LOOP for dictionary/set iteration")

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print("Processing grades with FOR loop:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
print()

print("Same with WHILE loop (complex and inefficient):")
items = list(student_grades.items())
index = 0
while index < len(items):
    name, grade = items[index]
    print(f"{name}: {grade}")
    index += 1
print("→ FOR loop is natural and efficient for this")
print()

print("SCENARIO 4: File Processing")
print("-" * 30)
print("✅ USE FOR LOOP for line-by-line file processing")

# Create sample file
sample_content = "Line 1\nLine 2\nLine 3\nLine 4"
with open("sample.txt", "w") as f:
    f.write(sample_content)

print("Reading file with FOR loop:")
with open("sample.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")
print()

print("Same with WHILE loop (more complex):")
with open("sample.txt", "r") as file:
    line_num = 1
    while True:
        line = file.readline()
        if not line:  # End of file
            break
        print(f"Line {line_num}: {line.strip()}")
        line_num += 1
print("→ FOR loop handles file iteration automatically")
print()

# Clean up
import os

os.remove("sample.txt")

# ===== WHEN TO USE WHILE LOOPS =====
print("🔸 WHEN TO USE WHILE LOOPS")
print("-" * 50)
print()

print("SCENARIO 1: Unknown Number of Iterations")
print("-" * 30)
print("✅ USE WHILE LOOP when you don't know how many iterations needed")

import random

random.seed(42)  # For reproducible results

print("Guessing game with WHILE loop:")
target = random.randint(1, 10)
attempts = 0
guessed_numbers = []

# Simulate guessing
guesses = [5, 8, 3, 7, 2, 9, 4]  # Predefined guesses for demo
guess_index = 0

while True:
    if guess_index >= len(guesses):
        break

    guess = guesses[guess_index]
    guess_index += 1
    attempts += 1
    guessed_numbers.append(guess)

    print(f"Attempt {attempts}: Guessing {guess}")

    if guess == target:
        print(f"🎉 Correct! Found {target} in {attempts} attempts")
        break
    elif guess < target:
        print("Too low!")
    else:
        print("Too high!")

print(f"Numbers guessed: {guessed_numbers}")
print("→ FOR loop cannot handle this unknown iteration scenario")
print()

print("SCENARIO 2: Condition-Based Processing")
print("-" * 30)
print("✅ USE WHILE LOOP for condition-based logic")

print("Processing until condition met with WHILE loop:")
balance = 1000
transactions = [50, -200, 100, -75, -300, -150, 25]
transaction_index = 0

print(f"Starting balance: ${balance}")

while balance > 500 and transaction_index < len(transactions):
    transaction = transactions[transaction_index]
    balance += transaction
    transaction_index += 1

    print(f"Transaction: ${transaction:+}, New balance: ${balance}")

    if balance <= 500:
        print("⚠️ Balance dropped to warning level!")

print(f"Final balance: ${balance}")
print("→ FOR loop cannot easily handle dynamic exit conditions")
print()

print("SCENARIO 3: User Input Validation")
print("-" * 30)
print("✅ USE WHILE LOOP for input validation")


def simulate_user_input():
    """Simulate user input for demonstration"""
    inputs = ["abc", "150", "0", "25"]
    for inp in inputs:
        yield inp


input_simulator = simulate_user_input()

print("Input validation with WHILE loop:")
while True:
    try:
        user_input = next(input_simulator)
        print(f"User entered: '{user_input}'")

        age = int(user_input)
        if age <= 0:
            print("❌ Age must be positive. Try again.")
            continue
        elif age > 120:
            print("❌ Age seems unrealistic. Try again.")
            continue
        else:
            print(f"✅ Valid age: {age}")
            break
    except ValueError:
        print("❌ Please enter a valid number. Try again.")
    except StopIteration:
        print("Demo ended")
        break

print("→ FOR loop cannot handle indefinite input validation")
print()

print("SCENARIO 4: Server/Event Loop Simulation")
print("-" * 30)
print("✅ USE WHILE LOOP for continuous monitoring")

print("Server monitoring simulation with WHILE loop:")
server_running = True
requests_processed = 0
max_requests = 5  # For demo purposes

# Simulate incoming requests
incoming_requests = [
    "GET /home",
    "POST /login",
    "GET /dashboard",
    "PUT /profile",
    "DELETE /account",
]

while server_running and requests_processed < max_requests:
    if requests_processed < len(incoming_requests):
        request = incoming_requests[requests_processed]
        print(f"Processing request {requests_processed + 1}: {request}")
        requests_processed += 1

        # Simulate processing time and conditions
        if "DELETE" in request:
            print("⚠️ Critical operation detected")

        if requests_processed >= max_requests:
            print("🛑 Max requests reached, shutting down")
            server_running = False
    else:
        print("No more requests to process")
        break

print(f"Total requests processed: {requests_processed}")
print("→ FOR loop cannot handle continuous monitoring scenarios")
print()

print("SCENARIO 5: Mathematical Convergence")
print("-" * 30)
print("✅ USE WHILE LOOP for mathematical algorithms")

print("Finding square root using Newton's method with WHILE loop:")
number = 25
guess = number / 2  # Initial guess
tolerance = 0.0001
iterations = 0

print(f"Finding square root of {number}")
print(f"Starting guess: {guess}")

while True:
    iterations += 1
    better_guess = (guess + number / guess) / 2
    error = abs(better_guess - guess)

    print(f"Iteration {iterations}: guess = {better_guess:.6f}, error = {error:.6f}")

    if error < tolerance:
        print(f"✅ Converged! Square root ≈ {better_guess:.6f}")
        break

    guess = better_guess

    if iterations > 20:  # Safety check
        print("Max iterations reached")
        break

print(f"Actual square root: {number ** 0.5:.6f}")
print("→ FOR loop cannot handle convergence-based algorithms")
print()

# ===== SCENARIOS WHERE NEITHER CAN EASILY REPLACE THE OTHER =====
print("🔸 SCENARIOS WHERE ONE CANNOT REPLACE THE OTHER")
print("-" * 50)
print()

print("WHERE FOR LOOP CANNOT BE REPLACED BY WHILE:")
print("-" * 30)

print("1. ITERATOR PROTOCOL USAGE")
print("For loops automatically handle iterators, while loops cannot:")


class CustomIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current**2
        raise StopIteration


print("Custom iterator with FOR loop (natural):")
for square in CustomIterator(5):
    print(f"Square: {square}")
print()

print("Same with WHILE loop (complex and error-prone):")
iterator = CustomIterator(5)
while True:
    try:
        square = next(iterator)
        print(f"Square: {square}")
    except StopIteration:
        break
print("→ FOR loop handles iterator protocol automatically")
print()

print("2. MULTIPLE SEQUENCE ITERATION WITH ZIP")
print("For loops with zip() are natural, while loops are awkward:")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "London", "Tokyo"]

print("Multiple sequences with FOR loop:")
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
print()

print("Same with WHILE loop (verbose and error-prone):")
index = 0
while index < min(len(names), len(ages), len(cities)):
    print(f"{names[index]}, {ages[index]}, {cities[index]}")
    index += 1
print("→ FOR loop with zip() is much cleaner")
print()

print("WHERE WHILE LOOP CANNOT BE REPLACED BY FOR:")
print("-" * 30)

print("1. INFINITE LOOPS WITH DYNAMIC CONDITIONS")
print("While loops can run indefinitely, for loops cannot:")

print("Simulating infinite loop with break condition:")
counter = 0
threshold = 7

print("WHILE loop for infinite processing:")
while True:  # Infinite loop
    counter += 1
    print(f"Processing cycle {counter}")

    # Dynamic condition that might never be known in advance
    if counter**2 > threshold * 10:
        print(f"Dynamic condition met: {counter}² > {threshold * 10}")
        break

    if counter > 10:  # Safety break for demo
        print("Safety break activated")
        break

print("→ FOR loop cannot create true infinite loops with dynamic exits")
print()

print("2. STATE MACHINE IMPLEMENTATION")
print("While loops excel at state-based logic:")

print("Traffic light state machine with WHILE loop:")
states = ["RED", "GREEN", "YELLOW"]
current_state = 0
cycles_completed = 0
max_cycles = 3

while cycles_completed < max_cycles:
    state = states[current_state]
    print(f"Traffic light: {state}")

    # State-specific logic
    if state == "RED":
        print("  Cars stop")
        duration = 3
    elif state == "GREEN":
        print("  Cars go")
        duration = 5
    else:  # YELLOW
        print("  Cars prepare to stop")
        duration = 2
        cycles_completed += 1  # Count cycles at yellow

    # Simulate duration (in demo, just print)
    print(f"  Duration: {duration} seconds")

    # Move to next state
    current_state = (current_state + 1) % len(states)

print("→ FOR loop cannot handle state-based transitions naturally")
print()

print("3. REAL-TIME DATA PROCESSING")
print("While loops handle continuous data streams:")

import time

print("Real-time data monitoring simulation:")
data_stream = [10, 15, 25, 30, 45, 35, 20, 8, 12, 18]
stream_index = 0
alert_threshold = 40
monitoring = True

while monitoring and stream_index < len(data_stream):
    # Simulate real-time data arrival
    current_value = data_stream[stream_index]
    stream_index += 1

    print(f"Sensor reading: {current_value}")

    if current_value > alert_threshold:
        print(f"🚨 ALERT: Value {current_value} exceeds threshold {alert_threshold}")
        print("Initiating emergency protocol...")
        monitoring = False  # Dynamic condition to stop monitoring

    # Simulate processing delay
    print("  Processing...")

print("Monitoring stopped" if not monitoring else "Stream ended")
print("→ FOR loop cannot handle real-time conditional monitoring")
print()

# ===== COMPARATIVE EXAMPLES =====
print("🔸 COMPARATIVE EXAMPLES: BOTH APPROACHES")
print("-" * 50)
print()

print("EXAMPLE 1: Sum of Numbers")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Using FOR loop (natural choice):")
total_for = 0
for num in numbers:
    total_for += num
print(f"Sum using FOR loop: {total_for}")

print("\nUsing WHILE loop (possible but verbose):")
total_while = 0
index = 0
while index < len(numbers):
    total_while += numbers[index]
    index += 1
print(f"Sum using WHILE loop: {total_while}")

print("\nBest choice: FOR loop (built-in: sum(numbers))")
print(f"Built-in sum(): {sum(numbers)}")
print()

print("EXAMPLE 2: Finding First Match")
print("-" * 30)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
target = "Charlie"

print("Using FOR loop with break:")
found_for = False
for i, name in enumerate(names):
    print(f"Checking: {name}")
    if name == target:
        print(f"Found {target} at index {i}")
        found_for = True
        break

if not found_for:
    print(f"{target} not found")

print(f"\nUsing WHILE loop:")
found_while = False
index = 0
while index < len(names) and not found_while:
    name = names[index]
    print(f"Checking: {name}")
    if name == target:
        print(f"Found {target} at index {index}")
        found_while = True
    index += 1

if not found_while:
    print(f"{target} not found")

print("\nBoth work well, but FOR loop with enumerate is more Pythonic")
print()

print("EXAMPLE 3: Menu System")
print("-" * 30)


def show_menu():
    print("\n--- Menu ---")
    print("1. View Profile")
    print("2. Edit Settings")
    print("3. Help")
    print("4. Exit")


# Simulate user choices
user_choices = ["1", "2", "invalid", "3", "4"]
choice_index = 0

print("Menu system - WHILE loop is natural choice:")
while True:
    show_menu()

    # Simulate user input
    if choice_index < len(user_choices):
        choice = user_choices[choice_index]
        choice_index += 1
    else:
        choice = "4"  # Auto-exit for demo

    print(f"User choice: {choice}")

    if choice == "1":
        print("📄 Displaying profile...")
    elif choice == "2":
        print("⚙️ Opening settings...")
    elif choice == "3":
        print("❓ Showing help...")
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")

print("\nMenu systems naturally use WHILE loops")
print("FOR loop would be awkward for this scenario")
print()

# ===== PERFORMANCE CONSIDERATIONS =====
print("🔸 PERFORMANCE CONSIDERATIONS")
print("-" * 50)
print()

import time

print("Performance comparison for same task:")
test_data = list(range(100000))

# FOR loop performance
start_time = time.time()
sum_for = 0
for num in test_data:
    sum_for += num
for_time = time.time() - start_time

# WHILE loop performance
start_time = time.time()
sum_while = 0
index = 0
while index < len(test_data):
    sum_while += test_data[index]
    index += 1
while_time = time.time() - start_time

# Built-in function performance
start_time = time.time()
sum_builtin = sum(test_data)
builtin_time = time.time() - start_time

print(f"FOR loop time: {for_time:.6f}s, result: {sum_for}")
print(f"WHILE loop time: {while_time:.6f}s, result: {sum_while}")
print(f"Built-in sum() time: {builtin_time:.6f}s, result: {sum_builtin}")
print(f"\nPerformance ratio (FOR:WHILE): {for_time/while_time:.2f}")
print("FOR loops are generally faster for iteration over collections")
print()

# ===== DECISION FLOWCHART =====
print("🔸 DECISION FLOWCHART")
print("-" * 50)
print()

print(
    """
CHOOSING BETWEEN FOR AND WHILE LOOPS:

START HERE
    ↓
Do you have a collection to iterate over?
    ├─ YES → Do you need to process each element?
    │           ├─ YES → Use FOR LOOP
    │           └─ NO → Consider list comprehension or built-in functions
    └─ NO → Continue
        ↓
Do you know the number of iterations in advance?
    ├─ YES → Can you express it as a range?
    │           ├─ YES → Use FOR LOOP with range()
    │           └─ NO → Use WHILE LOOP
    └─ NO → Continue
        ↓
Is the loop condition dynamic or complex?
    ├─ YES → Use WHILE LOOP
    └─ NO → Continue
        ↓
Do you need an infinite loop with break conditions?
    ├─ YES → Use WHILE LOOP
    └─ NO → Continue
        ↓
Are you implementing a state machine or event loop?
    ├─ YES → Use WHILE LOOP
    └─ NO → Use FOR LOOP (default choice)

SPECIAL CASES:
- File processing: FOR LOOP
- User input validation: WHILE LOOP
- Mathematical convergence: WHILE LOOP
- Data transformation: FOR LOOP (or comprehensions)
- Real-time monitoring: WHILE LOOP
"""
)
print()

# ===== BEST PRACTICES SUMMARY =====
print("🔸 BEST PRACTICES SUMMARY")
print("-" * 50)
print()

print("USE FOR LOOPS WHEN:")
print("✅ Iterating over collections (lists, tuples, dictionaries)")
print("✅ Processing files line by line")
print("✅ Working with ranges of numbers")
print("✅ Using enumerate() for index access")
print("✅ Using zip() for multiple sequences")
print("✅ Number of iterations is known or bounded")
print("✅ You want cleaner, more Pythonic code")
print()

print("USE WHILE LOOPS WHEN:")
print("✅ Number of iterations is unknown")
print("✅ Loop condition is complex or dynamic")
print("✅ Implementing infinite loops with break conditions")
print("✅ Building state machines or event loops")
print("✅ Validating user input")
print("✅ Implementing mathematical algorithms (convergence)")
print("✅ Real-time monitoring or continuous processing")
print()

print("AVOID:")
print("❌ Using WHILE loops for simple collection iteration")
print("❌ Using FOR loops for condition-based logic")
print("❌ Complex index management in WHILE loops")
print("❌ Modifying collection size during FOR loop iteration")
print("❌ Infinite FOR loops (use WHILE instead)")
print()

print("PERFORMANCE TIPS:")
print("💡 FOR loops are generally faster for collection iteration")
print("💡 Use built-in functions (sum, max, min) when possible")
print("💡 List comprehensions are often faster than explicit loops")
print("💡 Avoid repeated calculations inside loops")
print("💡 Consider generators for memory-efficient processing")
print()

print("=" * 80)
print("CONCLUSION:")
print("FOR loops are for iteration over known collections or ranges.")
print("WHILE loops are for condition-based, dynamic, or indefinite iteration.")
print("Choose based on the problem structure, not personal preference.")
print("When in doubt, FOR loop is usually the more Pythonic choice.")
print("=" * 80)
