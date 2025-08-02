# lambda.py
# Lambda Functions and Other Types of Functions in Python

"""
COMPREHENSIVE GUIDE: LAMBDA AND OTHER FUNCTION TYPES

This file covers:
1. Lambda functions (anonymous functions)
2. Higher-order functions
3. Nested functions
4. Closures
5. Decorators
6. Generator functions
7. Async functions
8. When to use each type
"""

# ============================================================================
# LAMBDA FUNCTIONS AND OTHER FUNCTION TYPES
# ============================================================================

# ===== LAMBDA FUNCTIONS: THE BASICS =====
# Lambda functions are anonymous functions - small functions without a name
# They can have any number of arguments but only one expression
# Think of them like mathematical functions: f(x) = x²
#
# SYNTAX: lambda arguments: expression
# Example: lambda x: x * 2

# Regular function vs Lambda function comparison
# Both functions do the same thing - square a number
# But lambda is more concise for simple operations


# Regular function
def square_regular(x):
    return x**2


# Lambda function - same functionality, more concise
square_lambda = lambda x: x**2

# Test both functions with sample data
numbers = [1, 2, 3, 4, 5]
# Both produce identical results: [1, 4, 9, 16, 25]
regular_results = [square_regular(x) for x in numbers]
lambda_results = [square_lambda(x) for x in numbers]

# ===== LAMBDA FUNCTIONS WITH MULTIPLE ARGUMENTS =====
# Lambda functions can accept multiple parameters, separated by commas

# Lambda with two arguments - addition
add = lambda x, y: x + y

# Lambda with three arguments - multiplication
multiply = lambda x, y, z: x * y * z

# Examples: add(5, 3) returns 8, multiply(2, 3, 4) returns 24

# ===== LAMBDA WITH BUILT-IN FUNCTIONS =====
# Lambda functions shine when used with built-in functions like map(), filter(), sorted()

# LAMBDA WITH map() FUNCTION:
# map() applies a function to every item in an iterable
# Perfect for transforming data collections

numbers = [1, 2, 3, 4, 5]

# Using lambda with map() to square all numbers
squared = list(map(lambda x: x**2, numbers))
# Result: [1, 4, 9, 16, 25]


# Equivalent without lambda (more verbose)
def square_func(x):
    return x**2


squared_regular = list(map(square_func, numbers))
# Same result: [1, 4, 9, 16, 25]

# LAMBDA WITH filter() FUNCTION:
# filter() creates an iterator from elements for which a function returns True
# Excellent for data filtering and selection

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda with filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6, 8, 10]

# Using lambda for more complex filtering - numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
# Result: [6, 7, 8, 9, 10]

# LAMBDA WITH sorted() FUNCTION:
# sorted() can use lambda for custom sorting logic
# Key parameter accepts a function that extracts comparison key from each element

# Sorting student data by different criteria
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 92)]

# Sort by grade (second element of tuple) - ascending order
by_grade = sorted(students, key=lambda student: student[1])
# Result: [('Charlie', 78), ('Alice', 85), ('Bob', 90), ('Diana', 92)]

# Sort by name length - useful for organizing data by string properties
by_name_length = sorted(students, key=lambda student: len(student[0]))
# Result: [('Bob', 90), ('Alice', 85), ('Diana', 92), ('Charlie', 78)]

# LAMBDA WITH reduce() FUNCTION:
# reduce() applies a function cumulatively to items in a sequence
# Reduces a list to a single value through cumulative operations

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers using reduce and lambda
# Process: ((((1+2)+3)+4)+5) = 15
sum_result = reduce(lambda x, y: x + y, numbers)

# Find maximum using reduce and lambda
# Process: max(max(max(max(1,2),3),4),5) = 5
max_result = reduce(lambda x, y: x if x > y else y, numbers)

# ===== REAL-WORLD LAMBDA EXAMPLES =====

# EXAMPLE 1: DATA PROCESSING
# Employee data processing - common in HR and business applications

employees = [
    {"name": "Alice", "salary": 75000, "department": "Engineering"},
    {"name": "Bob", "salary": 65000, "department": "Marketing"},
    {"name": "Charlie", "salary": 80000, "department": "Engineering"},
    {"name": "Diana", "salary": 70000, "department": "Marketing"},
]

# Filter engineers using lambda - clean and readable
engineers = list(filter(lambda emp: emp["department"] == "Engineering", employees))
# Result: Alice and Charlie

# Sort by salary (descending) - useful for payroll analysis
by_salary = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
# Result: Charlie(80k), Alice(75k), Diana(70k), Bob(65k)

# EXAMPLE 2: E-COMMERCE CALCULATIONS
# Product pricing with discounts - typical e-commerce scenario

products = [
    {"name": "Laptop", "price": 999.99, "discount": 0.1},
    {"name": "Mouse", "price": 25.99, "discount": 0.05},
    {"name": "Keyboard", "price": 79.99, "discount": 0.15},
]

# Calculate final prices using lambda with map()
# Creates new structure with original and discounted prices
final_prices = list(
    map(
        lambda p: {
            "name": p["name"],
            "original": p["price"],
            "final": p["price"] * (1 - p["discount"]),
        },
        products,
    )
)

# Result: Laptop: $999.99 → $899.99, Mouse: $25.99 → $24.69, Keyboard: $79.99 → $67.99

# ===== HIGHER-ORDER FUNCTIONS =====
# Higher-order functions are functions that:
# 1. Take other functions as arguments, OR
# 2. Return functions as results
# They enable powerful functional programming patterns


# EXAMPLE 1: FUNCTION THAT TAKES FUNCTION AS ARGUMENT
def apply_operation(numbers, operation):
    """
    Higher-order function that applies an operation to a list of numbers
    The 'operation' parameter is a function (could be lambda or regular function)
    """
    return [operation(num) for num in numbers]


numbers = [1, 2, 3, 4, 5]

# Using different operations (lambdas) with the same higher-order function
doubled = apply_operation(numbers, lambda x: x * 2)  # [2, 4, 6, 8, 10]
squared = apply_operation(numbers, lambda x: x**2)  # [1, 4, 9, 16, 25]
negative = apply_operation(numbers, lambda x: -x)  # [-1, -2, -3, -4, -5]


# EXAMPLE 2: FUNCTION THAT RETURNS FUNCTION
# Factory function pattern - creates specialized functions
def create_multiplier(factor):
    """
    Higher-order function that returns a function
    Creates customized multiplier functions based on the factor
    """
    return lambda x: x * factor


# Create different multiplier functions
double = create_multiplier(2)  # Returns lambda x: x * 2
triple = create_multiplier(3)  # Returns lambda x: x * 3
times_ten = create_multiplier(10)  # Returns lambda x: x * 10

# Each returned function remembers its specific factor
# double(5) = 10, triple(5) = 15, times_ten(5) = 50

# ===== NESTED FUNCTIONS =====
# Nested functions are functions defined inside other functions
# Inner functions can access variables from the outer function's scope
# Useful for organization and encapsulation


def outer_function(message):
    """
    Outer function that contains inner functions
    Demonstrates how inner functions can access outer scope variables
    """

    def inner_function():
        """
        Inner function that can access outer function's variables
        """
        return f"Inner says: {message}"

    def another_inner():
        """
        Another inner function with access to the same outer variables
        """
        return f"Another inner says: {message.upper()}"

    # Outer function can call inner functions and return them
    # This demonstrates encapsulation and controlled access
    inner_result = inner_function()
    another_result = another_inner()

    return inner_function  # Returning the inner function itself


# Call outer function - it returns the inner function
returned_function = outer_function("Hello from nested function!")

# The returned inner function still remembers the message (closure behavior)
# This is the foundation for closures

# ===== CLOSURES =====
# A closure is a nested function that has access to variables
# from its enclosing (outer) function, even after the outer function returns
# This creates persistent local state - very powerful for state management


def create_counter(start=0):
    """
    Creates a counter function (closure)
    The inner function 'captures' the count variable from outer scope
    """
    count = start  # This variable is 'captured' by the closure

    def counter():
        nonlocal count  # Allows modification of outer variable
        count += 1
        return count

    return counter


# Create different counters - each maintains its own state
counter1 = create_counter(0)  # Starts from 0
counter2 = create_counter(100)  # Starts from 100

# Each counter maintains independent state:
# counter1() calls: 1, 2, 3, 4...
# counter2() calls: 101, 102...
# counter1() again: continues from where it left off

# ===== DECORATORS =====
# Decorators are a way to modify or extend functions without changing their code
# They use the @ symbol and are applied above function definitions
# Think of them as "wrappers" that add functionality to existing functions


def timing_decorator(func):
    """
    Decorator that measures how long a function takes to execute
    Useful for performance monitoring and optimization
    """
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # In practice, you might log this instead of printing
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


def logging_decorator(func):
    """
    Decorator that logs function calls
    Excellent for debugging and monitoring function usage
    """

    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


# Functions with decorators applied
# Multiple decorators can be stacked - they execute in reverse order
@timing_decorator
@logging_decorator
def calculate_sum(numbers):
    """
    Function decorated with both timing and logging decorators
    First logs the call, then times the execution
    """
    return sum(numbers)


@timing_decorator
def slow_calculation(n):
    """
    Function that simulates slow computation
    Only has timing decorator applied
    """
    import time

    time.sleep(0.1)  # Simulate delay
    return n**2


# When called, these functions automatically get the decorator behavior
# calculate_sum([1,2,3,4,5]) will log the call AND time the execution
# slow_calculation(10) will only time the execution

# ===== GENERATOR FUNCTIONS =====
# Generator functions use 'yield' instead of 'return'
# They produce values one at a time, saving memory
# Perfect for handling large datasets or infinite sequences


def countdown_generator(start):
    """
    Generator function that counts down from start to 1
    Yields values one at a time instead of creating entire list in memory
    """
    print(f"Starting countdown from {start}")
    while start > 0:
        yield start  # Produces value and pauses execution
        start -= 1
    print("Countdown finished!")


def fibonacci_generator(limit):
    """
    Generator function that produces Fibonacci sequence
    Memory-efficient - only calculates next value when requested
    """
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


# Generator usage examples:
# countdown = countdown_generator(5)
# for number in countdown: print(f"Count: {number}")
# Results: 5, 4, 3, 2, 1

# fib = fibonacci_generator(20)
# fib_list = list(fib)
# Results: [0, 1, 1, 2, 3, 5, 8, 13]

# ===== LAMBDA VS REGULAR FUNCTIONS: WHEN TO USE WHAT =====

# USE LAMBDA WHEN:
# ✅ Simple, one-line expressions
# ✅ Short-lived functions (used once)
# ✅ With map(), filter(), sorted(), etc.
# ✅ Simple mathematical operations
# ✅ Callback functions

# USE REGULAR FUNCTIONS WHEN:
# ✅ Complex logic (multiple lines)
# ✅ Functions used multiple times
# ✅ Need documentation (docstrings)
# ✅ Error handling required
# ✅ Multiple return statements

# COMPARISON EXAMPLES:

# Good use of lambda - simple, one-time use
data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_by_age = sorted(data, key=lambda person: person[1])
# Result: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

# Bad use of lambda (too complex)
# Don't do this - lambda becomes unreadable:
complex_lambda = lambda x: x * 2 if x > 0 else -x if x < 0 else 0


# Better as regular function - more readable and maintainable:
def process_number(x):
    """
    Process number based on its value
    - Positive: double it
    - Negative: make positive
    - Zero: return zero
    """
    if x > 0:
        return x * 2
    elif x < 0:
        return -x
    else:
        return 0


# ===== PRACTICAL LAMBDA EXAMPLES =====

# EXAMPLE 1: WEB DEVELOPMENT - SORTING SEARCH RESULTS
search_results = [
    {"title": "Python Tutorial", "relevance": 95, "date": "2024-01-15"},
    {"title": "Lambda Functions", "relevance": 88, "date": "2024-02-20"},
    {"title": "Python Basics", "relevance": 92, "date": "2024-01-10"},
]

# Sort by relevance (descending) - perfect lambda use case
by_relevance = sorted(search_results, key=lambda r: r["relevance"], reverse=True)
# Result: Python Tutorial(95%), Python Basics(92%), Lambda Functions(88%)

# EXAMPLE 2: DATA ANALYSIS - FILTERING AND TRANSFORMING
sales_data = [
    {"product": "Laptop", "price": 999, "quantity": 5},
    {"product": "Mouse", "price": 25, "quantity": 50},
    {"product": "Keyboard", "price": 75, "quantity": 20},
    {"product": "Monitor", "price": 300, "quantity": 8},
]

# Filter high-value items (price * quantity > 1000)
high_value = list(
    filter(lambda item: item["price"] * item["quantity"] > 1000, sales_data)
)
# Result: Laptop(4995), Mouse(1250), Keyboard(1500), Monitor(2400)

# Calculate total revenue for each product using map
revenues = list(
    map(
        lambda item: {
            "product": item["product"],
            "revenue": item["price"] * item["quantity"],
        },
        sales_data,
    )
)
# Result: [{"product": "Laptop", "revenue": 4995}, ...]

# ===== SUMMARY AND BEST PRACTICES =====

# FUNCTION TYPE SUMMARY:
# ======================

# 1. LAMBDA FUNCTIONS
#    • Anonymous, single-expression functions
#    • Perfect for: map(), filter(), sorted()
#    • Keep them simple and readable

# 2. HIGHER-ORDER FUNCTIONS
#    • Functions that work with other functions
#    • Great for: creating reusable operations
#    • Enable functional programming patterns

# 3. NESTED FUNCTIONS
#    • Functions inside other functions
#    • Good for: helper functions, organization
#    • Can access outer function variables

# 4. CLOSURES
#    • Nested functions that 'remember' outer variables
#    • Perfect for: state management, factory functions
#    • Create specialized function instances

# 5. DECORATORS
#    • Functions that modify other functions
#    • Excellent for: logging, timing, authentication
#    • Clean way to add functionality

# 6. GENERATORS
#    • Functions that yield values one at a time
#    • Memory-efficient for large datasets
#    • Great for: sequences, streaming data

# BEST PRACTICES:
# ===============
# • Use lambda for simple, one-line operations
# • Choose regular functions for complex logic
# • Use meaningful names even for lambda variables
# • Don't make lambdas too complex
# • Consider readability over cleverness
# • Use type hints for better code documentation
# • Test all function types thoroughly

# REMEMBER:
# Functions are tools. Choose the right tool for the job!
# Lambda functions are not always better - use them when they make code clearer.

# ============================================================================
# END OF LAMBDA AND FUNCTION TYPES GUIDE
# ============================================================================
