# for-loop.py
# Comprehensive Guide to For Loops in Python

"""
COMPLETE FOR LOOP GUIDE

This file covers:
1. Basic for loop syntax and concepts
2. For loops with different data types
3. Real-world examples and use cases
4. Advanced for loop techniques
5. Performance considerations
6. Best practices and common patterns
"""

print("=" * 80)
print("COMPREHENSIVE GUIDE TO FOR LOOPS IN PYTHON")
print("=" * 80)
print()

# ===== BASIC FOR LOOP CONCEPTS =====
print("🔸 BASIC FOR LOOP CONCEPTS")
print("-" * 50)
print()

print("CONCEPT 1: Basic For Loop Structure")
print("-" * 30)
print("Syntax: for variable in iterable:")
print("        # code block")
print()

# Simple range-based loop
print("Basic counting with range():")
for i in range(5):
    print(f"Count: {i}")
print()

# Range with start, stop, step
print("Range with start, stop, step:")
for i in range(2, 10, 2):  # Start=2, Stop=10, Step=2
    print(f"Even number: {i}")
print()

print("CONCEPT 2: How For Loops Work Internally")
print("-" * 30)
print("For loops use the iterator protocol:")

# Manual iteration to show what happens behind the scenes
numbers = [1, 2, 3, 4, 5]
print("Manual iteration (what Python does internally):")
iterator = iter(numbers)  # Create iterator
try:
    while True:
        item = next(iterator)  # Get next item
        print(f"Processing: {item}")
except StopIteration:
    print("Iterator exhausted")
print()

print("Same result with for loop:")
for item in numbers:
    print(f"Processing: {item}")
print()

# ===== FOR LOOPS WITH DIFFERENT DATA TYPES =====
print("🔸 FOR LOOPS WITH DIFFERENT DATA TYPES")
print("-" * 50)
print()

print("DATA TYPE 1: Lists")
print("-" * 30)

# Basic list iteration
fruits = ["apple", "banana", "cherry", "date"]
print("Iterating through fruits:")
for fruit in fruits:
    print(f"I like {fruit}")
print()

# List with index using enumerate()
print("Getting index and value with enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print()

# List with custom start index
print("Custom start index with enumerate():")
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")
print()

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Iterating through nested lists (2D matrix):")
for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        print(f"matrix[{row_index}][{col_index}] = {value}")
print()

print("DATA TYPE 2: Tuples")
print("-" * 30)

# Basic tuple iteration
coordinates = (10, 20, 30)
print("Iterating through tuple coordinates:")
for coord in coordinates:
    print(f"Coordinate: {coord}")
print()

# Tuple of tuples (like database records)
employees = (
    ("Alice", "Engineer", 75000),
    ("Bob", "Designer", 65000),
    ("Charlie", "Manager", 85000),
)
print("Processing employee records:")
for name, position, salary in employees:  # Tuple unpacking
    print(f"{name} is a {position} earning ${salary:,}")
print()

print("DATA TYPE 3: Dictionaries")
print("-" * 30)

# Dictionary with different iteration methods
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}

print("Iterating through dictionary keys:")
for name in student_grades:  # Default: iterate over keys
    print(f"Student: {name}")
print()

print("Iterating through dictionary values:")
for grade in student_grades.values():
    print(f"Grade: {grade}")
print()

print("Iterating through key-value pairs:")
for name, grade in student_grades.items():
    print(f"{name} scored {grade}")
print()

# Nested dictionary
company_data = {
    "employees": {
        "Alice": {"department": "IT", "salary": 75000},
        "Bob": {"department": "HR", "salary": 65000},
    },
    "departments": {
        "IT": {"budget": 500000, "head": "Alice"},
        "HR": {"budget": 200000, "head": "Bob"},
    },
}

print("Iterating through nested dictionary:")
for category, data in company_data.items():
    print(f"\n{category.upper()}:")
    for key, value in data.items():
        print(f"  {key}: {value}")
print()

print("DATA TYPE 4: Strings")
print("-" * 30)

# Character iteration
message = "Python"
print("Iterating through string characters:")
for char in message:
    print(f"Character: '{char}'")
print()

# String with index
print("String characters with positions:")
for index, char in enumerate(message):
    print(f"Position {index}: '{char}'")
print()

# Multiple strings
languages = ["Python", "Java", "JavaScript"]
print("Iterating through multiple strings:")
for language in languages:
    print(f"Language: {language}")
    for char in language:
        print(f"  Character: '{char}'")
    print()

print("DATA TYPE 5: Sets")
print("-" * 30)

# Basic set iteration
unique_colors = {"red", "green", "blue", "yellow"}
print("Iterating through set (unordered):")
for color in unique_colors:
    print(f"Color: {color}")
print()

# Set operations in loops
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Processing set operations:")
for num in set_a & set_b:  # Intersection
    print(f"Common number: {num}")
print()

print("DATA TYPE 6: Files")
print("-" * 30)

# Create a sample file for demonstration
sample_content = """Line 1: Python is awesome
Line 2: For loops are powerful
Line 3: File processing is easy"""

# Write sample file
with open("sample.txt", "w") as f:
    f.write(sample_content)

print("Reading file line by line:")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")
print()

# Clean up
import os

os.remove("sample.txt")

# ===== REAL-WORLD EXAMPLES =====
print("🔸 REAL-WORLD EXAMPLES AND USE CASES")
print("-" * 50)
print()

print("EXAMPLE 1: E-commerce Order Processing")
print("-" * 30)

orders = [
    {"id": 1001, "customer": "Alice", "items": ["laptop", "mouse"], "total": 1299.99},
    {"id": 1002, "customer": "Bob", "items": ["phone", "case"], "total": 899.50},
    {"id": 1003, "customer": "Charlie", "items": ["tablet"], "total": 399.99},
]

print("Processing orders:")
total_revenue = 0
for order in orders:
    print(f"Order #{order['id']} - Customer: {order['customer']}")
    print(f"  Items: {', '.join(order['items'])}")
    print(f"  Total: ${order['total']:.2f}")
    total_revenue += order["total"]

    # Apply discount for large orders
    if order["total"] > 1000:
        discount = order["total"] * 0.1
        print(f"  Discount applied: ${discount:.2f}")
    print()

print(f"Total Revenue: ${total_revenue:.2f}")
print()

print("EXAMPLE 2: Student Grade Analysis")
print("-" * 30)

class_grades = {
    "Math": [85, 92, 78, 96, 88, 74, 91],
    "Science": [89, 84, 92, 88, 79, 95, 87],
    "English": [91, 88, 85, 94, 82, 89, 93],
}

print("Grade analysis by subject:")
for subject, grades in class_grades.items():
    print(f"\n{subject}:")
    print(f"  Grades: {grades}")
    print(f"  Average: {sum(grades) / len(grades):.1f}")
    print(f"  Highest: {max(grades)}")
    print(f"  Lowest: {min(grades)}")

    # Count grade ranges
    a_grades = sum(1 for grade in grades if grade >= 90)
    b_grades = sum(1 for grade in grades if 80 <= grade < 90)
    c_grades = sum(1 for grade in grades if grade < 80)

    print(f"  A grades (90+): {a_grades}")
    print(f"  B grades (80-89): {b_grades}")
    print(f"  C grades (<80): {c_grades}")
print()

print("EXAMPLE 3: Web Server Log Analysis")
print("-" * 30)

# Simulated web server logs
server_logs = [
    "192.168.1.1 - GET /home - 200 - 1.2s",
    "192.168.1.2 - POST /login - 401 - 0.5s",
    "192.168.1.1 - GET /dashboard - 200 - 2.1s",
    "192.168.1.3 - GET /api/data - 500 - 5.0s",
    "192.168.1.2 - POST /login - 200 - 0.8s",
]

print("Analyzing server logs:")
status_codes = {}
ip_addresses = {}
slow_requests = []

for log_entry in server_logs:
    parts = log_entry.split(" - ")
    ip = parts[0]
    method_path = parts[1]
    status = parts[2]
    response_time = float(parts[3].replace("s", ""))

    # Count status codes
    status_codes[status] = status_codes.get(status, 0) + 1

    # Count IP addresses
    ip_addresses[ip] = ip_addresses.get(ip, 0) + 1

    # Track slow requests
    if response_time > 2.0:
        slow_requests.append((method_path, response_time))

    print(f"IP: {ip}, Request: {method_path}, Status: {status}, Time: {response_time}s")

print(f"\nStatus Code Summary:")
for code, count in status_codes.items():
    print(f"  {code}: {count} requests")

print(f"\nIP Address Activity:")
for ip, count in ip_addresses.items():
    print(f"  {ip}: {count} requests")

print(f"\nSlow Requests (>2s):")
for request, time in slow_requests:
    print(f"  {request}: {time}s")
print()

print("EXAMPLE 4: Financial Data Processing")
print("-" * 30)

# Monthly expenses by category
monthly_expenses = {
    "January": {"rent": 1200, "food": 400, "utilities": 150, "transport": 200},
    "February": {"rent": 1200, "food": 380, "utilities": 160, "transport": 180},
    "March": {"rent": 1200, "food": 420, "utilities": 140, "transport": 220},
}

print("Monthly expense analysis:")
category_totals = {}
monthly_totals = {}

for month, expenses in monthly_expenses.items():
    monthly_total = 0
    print(f"\n{month}:")

    for category, amount in expenses.items():
        print(f"  {category.capitalize()}: ${amount}")
        monthly_total += amount

        # Track category totals
        category_totals[category] = category_totals.get(category, 0) + amount

    print(f"  Monthly Total: ${monthly_total}")
    monthly_totals[month] = monthly_total

print(f"\nCategory Totals (3 months):")
for category, total in category_totals.items():
    average = total / 3
    print(f"  {category.capitalize()}: ${total} (Avg: ${average:.2f}/month)")

print(f"\nMonthly Comparison:")
for month, total in monthly_totals.items():
    print(f"  {month}: ${total}")
print()

print("EXAMPLE 5: Data Validation and Cleaning")
print("-" * 30)

# Raw user data that needs validation
user_data = [
    {
        "name": "Alice Johnson",
        "email": "alice@email.com",
        "age": "28",
        "phone": "123-456-7890",
    },
    {"name": "", "email": "invalid-email", "age": "not-a-number", "phone": "555-0123"},
    {"name": "Bob Smith", "email": "bob@company.com", "age": "35", "phone": ""},
    {
        "name": "Charlie Brown",
        "email": "charlie@test.org",
        "age": "22",
        "phone": "999-888-7777",
    },
]

print("Validating and cleaning user data:")
valid_users = []
validation_errors = []

for index, user in enumerate(user_data):
    print(f"\nValidating user {index + 1}:")
    errors = []
    cleaned_user = {}

    # Validate name
    if user["name"].strip():
        cleaned_user["name"] = user["name"].strip()
        print(f"  Name: ✓ '{cleaned_user['name']}'")
    else:
        errors.append("Name is empty")
        print(f"  Name: ✗ Empty name")

    # Validate email
    if "@" in user["email"] and "." in user["email"]:
        cleaned_user["email"] = user["email"].lower()
        print(f"  Email: ✓ '{cleaned_user['email']}'")
    else:
        errors.append("Invalid email format")
        print(f"  Email: ✗ Invalid format")

    # Validate age
    try:
        age = int(user["age"])
        if 18 <= age <= 120:
            cleaned_user["age"] = age
            print(f"  Age: ✓ {age}")
        else:
            errors.append("Age out of valid range")
            print(f"  Age: ✗ Out of range")
    except ValueError:
        errors.append("Age is not a number")
        print(f"  Age: ✗ Not a number")

    # Validate phone (optional)
    if user["phone"].strip():
        # Simple phone validation
        phone_digits = "".join(filter(str.isdigit, user["phone"]))
        if len(phone_digits) == 10:
            cleaned_user["phone"] = user["phone"]
            print(f"  Phone: ✓ '{cleaned_user['phone']}'")
        else:
            errors.append("Invalid phone format")
            print(f"  Phone: ✗ Invalid format")
    else:
        print(f"  Phone: - Not provided")

    # Store results
    if not errors:
        valid_users.append(cleaned_user)
        print(f"  Status: ✓ Valid user")
    else:
        validation_errors.append({"user_index": index + 1, "errors": errors})
        print(f"  Status: ✗ {len(errors)} error(s)")

print(f"\nValidation Summary:")
print(f"Valid users: {len(valid_users)}")
print(f"Invalid users: {len(validation_errors)}")

if validation_errors:
    print(f"\nValidation Errors:")
    for error_info in validation_errors:
        print(f"  User {error_info['user_index']}: {', '.join(error_info['errors'])}")
print()

# ===== ADVANCED FOR LOOP TECHNIQUES =====
print("🔸 ADVANCED FOR LOOP TECHNIQUES")
print("-" * 50)
print()

print("TECHNIQUE 1: List Comprehensions")
print("-" * 30)
print("Traditional for loop vs list comprehension:")

# Traditional approach
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_traditional = []
for num in numbers:
    if num % 2 == 0:  # Only even numbers
        squares_traditional.append(num**2)

print("Traditional approach result:", squares_traditional)

# List comprehension
squares_comprehension = [num**2 for num in numbers if num % 2 == 0]
print("List comprehension result:", squares_comprehension)
print()

print("TECHNIQUE 2: Dictionary Comprehensions")
print("-" * 30)

# Traditional approach
word_lengths_traditional = {}
words = ["python", "java", "javascript", "go", "rust"]
for word in words:
    word_lengths_traditional[word] = len(word)

print("Traditional approach:", word_lengths_traditional)

# Dictionary comprehension
word_lengths_comprehension = {word: len(word) for word in words}
print("Dict comprehension:", word_lengths_comprehension)
print()

print("TECHNIQUE 3: Multiple Iterables with zip()")
print("-" * 30)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("Iterating multiple lists simultaneously:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
print()

# Handling unequal length lists
names_short = ["Alice", "Bob"]
ages_long = [25, 30, 35, 40]

print("zip() stops at shortest list:")
for name, age in zip(names_short, ages_long):
    print(f"{name}: {age}")
print()

# Using zip_longest for unequal lists
from itertools import zip_longest

print("zip_longest() fills missing values:")
for name, age in zip_longest(names_short, ages_long, fillvalue="Unknown"):
    print(f"{name}: {age}")
print()

print("TECHNIQUE 4: Nested Loops and Loop Control")
print("-" * 30)

# Break and continue in nested loops
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
print("Finding first zero in matrix:")

found_zero = False
for row_idx, row in enumerate(matrix):
    for col_idx, value in enumerate(row):
        print(f"Checking [{row_idx}][{col_idx}] = {value}")
        if value == 0:
            print(f"Found zero at position [{row_idx}][{col_idx}]")
            found_zero = True
            break  # Break inner loop
    if found_zero:
        break  # Break outer loop

print()

print("TECHNIQUE 5: Generator Expressions")
print("-" * 30)

# Memory-efficient iteration for large datasets
print("Generator vs List for large data:")

# List comprehension (creates entire list in memory)
large_squares_list = [x**2 for x in range(1000)]
print(f"List comprehension: {len(large_squares_list)} items in memory")

# Generator expression (lazy evaluation)
large_squares_gen = (x**2 for x in range(1000))
print(f"Generator expression: One item at a time")

# Using generator
print("First 5 squares from generator:")
for i, square in enumerate(large_squares_gen):
    if i >= 5:
        break
    print(f"Square: {square}")
print()

# ===== PERFORMANCE CONSIDERATIONS =====
print("🔸 PERFORMANCE CONSIDERATIONS")
print("-" * 50)
print()

print("PERFORMANCE TIP 1: Avoid Repeated Calculations")
print("-" * 30)

import time

# Inefficient - repeated calculation
data = list(range(1000))
print("Inefficient approach (repeated len() calls):")
start_time = time.time()
for i in range(len(data)):  # len() called every iteration
    if i < len(data) // 2:  # Another len() call
        pass
inefficient_time = time.time() - start_time

# Efficient - calculate once
print("Efficient approach (calculate once):")
start_time = time.time()
data_len = len(data)  # Calculate once
half_len = data_len // 2
for i in range(data_len):
    if i < half_len:
        pass
efficient_time = time.time() - start_time

print(f"Inefficient time: {inefficient_time:.6f}s")
print(f"Efficient time: {efficient_time:.6f}s")
print(f"Improvement: {inefficient_time/efficient_time:.1f}x faster")
print()

print("PERFORMANCE TIP 2: Use Built-in Functions")
print("-" * 30)

numbers = list(range(10000))

# Manual loop
start_time = time.time()
total_manual = 0
for num in numbers:
    total_manual += num
manual_time = time.time() - start_time

# Built-in function
start_time = time.time()
total_builtin = sum(numbers)
builtin_time = time.time() - start_time

print(f"Manual loop time: {manual_time:.6f}s, result: {total_manual}")
print(f"Built-in sum() time: {builtin_time:.6f}s, result: {total_builtin}")
print(f"Built-in is {manual_time/builtin_time:.1f}x faster")
print()

# ===== COMMON PATTERNS AND BEST PRACTICES =====
print("🔸 COMMON PATTERNS AND BEST PRACTICES")
print("-" * 50)
print()

print("PATTERN 1: Processing with Index")
print("-" * 30)

items = ["apple", "banana", "cherry"]

# Good: Use enumerate()
print("Good practice - using enumerate():")
for index, item in enumerate(items):
    print(f"{index}: {item}")
print()

# Avoid: Manual index tracking
print("Avoid - manual index tracking:")
index = 0
for item in items:
    print(f"{index}: {item}")
    index += 1
print()

print("PATTERN 2: Filtering and Processing")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Good: Clear and readable
print("Good practice - clear filtering:")
for num in numbers:
    if num % 2 == 0:  # Clear condition
        result = num**2
        print(f"Even number {num} squared: {result}")
print()

# Even better: List comprehension for simple cases
even_squares = [num**2 for num in numbers if num % 2 == 0]
print("List comprehension result:", even_squares)
print()

print("PATTERN 3: Error Handling in Loops")
print("-" * 30)

mixed_data = ["123", "456", "abc", "789", "def"]
print("Processing mixed data with error handling:")

for item in mixed_data:
    try:
        number = int(item)
        print(f"Converted: {item} -> {number}")
    except ValueError:
        print(f"Skipped: '{item}' is not a number")
print()

print("PATTERN 4: Early Exit with else Clause")
print("-" * 30)

# Loop with else clause (executes if loop completes without break)
search_list = [1, 3, 5, 7, 9]
target = 6

print(f"Searching for {target} in {search_list}:")
for num in search_list:
    print(f"Checking: {num}")
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list")
print()

# ===== SUMMARY AND BEST PRACTICES =====
print("🔸 SUMMARY AND BEST PRACTICES")
print("-" * 50)
print()

print("BEST PRACTICES:")
print("1. Use enumerate() when you need both index and value")
print("2. Use zip() to iterate multiple sequences together")
print("3. Use list/dict comprehensions for simple transformations")
print("4. Use generators for memory-efficient processing of large data")
print("5. Avoid modifying lists while iterating over them")
print("6. Use built-in functions (sum, max, min) instead of manual loops")
print("7. Handle exceptions appropriately in loops")
print("8. Use meaningful variable names in loop iterations")
print("9. Consider loop complexity and optimize when necessary")
print("10. Use the else clause with loops when appropriate")
print()

print("COMMON PITFALLS TO AVOID:")
print("1. Don't use range(len(list)) when you can iterate directly")
print("2. Don't modify list size during iteration")
print("3. Don't ignore performance implications of nested loops")
print("4. Don't use loops when list comprehensions are clearer")
print("5. Don't forget to handle edge cases (empty lists, None values)")
print()

print("WHEN TO USE FOR LOOPS:")
print("✓ Iterating through collections (lists, tuples, dictionaries)")
print("✓ Processing files line by line")
print("✓ Performing operations on each element")
print("✓ Counting or accumulating values")
print("✓ Data validation and transformation")
print("✓ Generating sequences with specific patterns")
print()

print("=" * 80)
print("For loops are fundamental to Python programming and are used")
print("extensively in data processing, web development, automation,")
print("and scientific computing. Master these patterns and you'll")
print("write more efficient and readable Python code!")
print("=" * 80)
