# Interview.py
# Python Functions Interview Questions and Answers

"""
COMPREHENSIVE GUIDE: PYTHON FUNCTIONS INTERVIEW QUESTIONS

This file covers:
1. Basic Function Concepts
2. Parameters and Arguments
3. Return Values and Scope
4. Lambda Functions
5. Higher-Order Functions
6. Decorators and Closures
7. Advanced Function Topics
8. Practical Coding Problems
9. Tricky Interview Scenarios
"""

# ============================================================================
# SECTION 1: BASIC FUNCTION CONCEPTS
# ============================================================================

# Q1: What is a function in Python? Why do we use functions?
"""
ANSWER:
A function is a reusable block of code that performs a specific task.
We use functions for:
- Code reusability (DRY principle)
- Modularity and organization
- Easier testing and debugging
- Abstraction of complex operations
"""


def greet(name):
    """Example function demonstrating basic structure"""
    return f"Hello, {name}!"


# Q2: What are the different types of functions in Python?
"""
ANSWER:
1. Built-in functions: print(), len(), type(), etc.
2. User-defined functions: Functions we create
3. Lambda functions: Anonymous functions
4. Methods: Functions defined inside classes
5. Generator functions: Functions that yield values
"""

# Built-in function example
print(len("Hello"))  # Built-in function


# User-defined function example
def add_numbers(a, b):
    return a + b


# Lambda function example
multiply = lambda x, y: x * y

# Q3: What is the difference between parameters and arguments?
"""
ANSWER:
- Parameters: Variables in function definition (placeholders)
- Arguments: Actual values passed when calling the function

def function_name(parameter1, parameter2):  # These are parameters
    pass

function_name(argument1, argument2)  # These are arguments
"""


def calculate_area(length, width):  # length, width are parameters
    return length * width


result = calculate_area(5, 3)  # 5, 3 are arguments

# ============================================================================
# SECTION 2: PARAMETERS AND ARGUMENTS
# ============================================================================

# Q4: What are the different types of arguments in Python?
"""
ANSWER:
1. Positional arguments: Order matters
2. Keyword arguments: Name specified
3. Default arguments: Have default values
4. Variable-length arguments: *args and **kwargs
"""


def demo_arguments(pos_arg, default_arg="default", *args, **kwargs):
    """Demonstrates all argument types"""
    print(f"Positional: {pos_arg}")
    print(f"Default: {default_arg}")
    print(f"Variable args: {args}")
    print(f"Keyword args: {kwargs}")


# Usage examples:
# demo_arguments("required")
# demo_arguments("required", "custom", 1, 2, 3, name="John", age=25)

# Q5: What is *args and **kwargs? Provide examples.
"""
ANSWER:
*args: Allows function to accept variable number of positional arguments
**kwargs: Allows function to accept variable number of keyword arguments
"""


def sum_all(*args):
    """Sum variable number of arguments"""
    return sum(args)


def print_info(**kwargs):
    """Print variable number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def flexible_function(*args, **kwargs):
    """Accepts both types of variable arguments"""
    print("Positional args:", args)
    print("Keyword args:", kwargs)


# Usage:
# sum_all(1, 2, 3, 4, 5) → 15
# print_info(name="John", age=30, city="NYC")
# flexible_function(1, 2, 3, name="Alice", job="Engineer")

# Q6: What is the difference between local and global scope?
"""
ANSWER:
- Local scope: Variables defined inside a function
- Global scope: Variables defined outside all functions
- Local variables shadow global variables with same name
"""

global_var = "I'm global"


def scope_demo():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    print(local_var)
    print(global_var)


# Q7: What are the LEGB rules in Python?
"""
ANSWER:
LEGB stands for:
L - Local (inside function)
E - Enclosing (inside enclosing function)
G - Global (module level)
B - Built-in (built-in names)

Python searches for variables in this order.
"""

x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # Prints "local"

    inner()
    print(x)  # Prints "enclosing"


# ============================================================================
# SECTION 3: RETURN VALUES AND ADVANCED CONCEPTS
# ============================================================================

# Q8: Can a function return multiple values? How?
"""
ANSWER:
Yes, Python functions can return multiple values using tuples.
Python automatically packs multiple return values into a tuple.
"""


def get_name_age():
    return "Alice", 25  # Returns a tuple


def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers), len(numbers)


# Usage:
name, age = get_name_age()  # Tuple unpacking
min_val, max_val, total, count = calculate_stats([1, 2, 3, 4, 5])

# Q9: What is the difference between return and print?
"""
ANSWER:
- return: Sends a value back to the caller, exits function
- print: Displays output to console, function continues

return allows function results to be used in expressions
print only shows output but doesn't provide usable values
"""


def function_with_return(x):
    return x * 2


def function_with_print(x):
    print(x * 2)


# result1 = function_with_return(5)  # result1 = 10
# result2 = function_with_print(5)   # result2 = None (prints 10)

# Q10: What happens if a function doesn't have a return statement?
"""
ANSWER:
If a function doesn't explicitly return a value, it returns None.
"""


def no_return():
    x = 5 + 3


def explicit_none():
    return None


# Both functions return None
# result1 = no_return()      # None
# result2 = explicit_none()  # None

# ============================================================================
# SECTION 4: LAMBDA FUNCTIONS
# ============================================================================

# Q11: What are lambda functions? When should you use them?
"""
ANSWER:
Lambda functions are anonymous functions with single expressions.
Use them for:
- Short, simple operations
- With map(), filter(), sorted()
- Callback functions
- Functional programming patterns

Don't use for complex logic or multiple statements.
"""

# Lambda examples
square = lambda x: x**2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

# With built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Q12: What's the difference between lambda and regular functions?
"""
ANSWER:
Lambda functions:
- Anonymous (no name required)
- Single expression only
- Return expression result automatically
- Cannot contain statements
- Often used inline

Regular functions:
- Named functions
- Multiple statements allowed
- Explicit return needed
- Can have docstrings
- Better for complex logic
"""

# Lambda
multiply_lambda = lambda x, y: x * y


# Regular function
def multiply_regular(x, y):
    """Multiply two numbers"""
    return x * y


# Q13: Can you write a lambda function with multiple arguments?
"""
ANSWER:
Yes, lambda functions can take multiple arguments separated by commas.
"""

# Multiple arguments in lambda
max_of_three = lambda a, b, c: max(a, max(b, c))
full_name = lambda first, last: f"{first} {last}"
calculate_bmi = lambda weight, height: weight / (height**2)

# Usage:
# max_of_three(10, 5, 8)  # 10
# full_name("John", "Doe")  # "John Doe"
# calculate_bmi(70, 1.75)  # 22.86

# ============================================================================
# SECTION 5: HIGHER-ORDER FUNCTIONS
# ============================================================================

# Q14: What are higher-order functions? Provide examples.
"""
ANSWER:
Higher-order functions are functions that:
1. Take other functions as arguments, OR
2. Return functions as results

Common examples: map(), filter(), reduce(), sorted()
"""


def apply_operation(numbers, operation):
    """Takes a function as argument"""
    return [operation(num) for num in numbers]


def create_multiplier(factor):
    """Returns a function"""
    return lambda x: x * factor


# Usage:
numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, lambda x: x * 2)
times_three = create_multiplier(3)

# Q15: Explain map(), filter(), and reduce() with examples.
"""
ANSWER:
map(): Applies function to each element
filter(): Filters elements based on condition
reduce(): Reduces sequence to single value
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - transform each element
squares = list(map(lambda x: x**2, numbers))
# Result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter() - select elements that meet condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6, 8, 10]

# reduce() - combine all elements into single value
sum_all = reduce(lambda x, y: x + y, numbers)
# Result: 55

product_all = reduce(lambda x, y: x * y, numbers)
# Result: 3628800

# ============================================================================
# SECTION 6: DECORATORS AND CLOSURES
# ============================================================================

# Q16: What is a closure? Provide an example.
"""
ANSWER:
A closure is a nested function that captures and remembers variables
from its enclosing scope, even after the outer function returns.
"""


def create_counter(start=0):
    """Creates a closure that remembers the count"""
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


# Usage:
counter1 = create_counter(0)
counter2 = create_counter(100)

# counter1() returns 1, 2, 3, ...
# counter2() returns 101, 102, 103, ...

# Q17: What are decorators? How do they work?
"""
ANSWER:
Decorators are functions that modify or extend other functions
without changing their code. They use the @ symbol syntax.
"""


def timing_decorator(func):
    """Decorator that measures execution time"""
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def slow_function():
    """Function decorated with timing_decorator"""
    import time

    time.sleep(0.1)
    return "Done"


# Q18: Can you create a decorator with parameters?
"""
ANSWER:
Yes, you need a decorator factory - a function that returns a decorator.
"""


def repeat(times):
    """Decorator factory that repeats function execution"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


@repeat(3)
def say_hello(name):
    return f"Hello, {name}!"


# say_hello("Alice") returns ["Hello, Alice!", "Hello, Alice!", "Hello, Alice!"]

# ============================================================================
# SECTION 7: ADVANCED FUNCTION TOPICS
# ============================================================================

# Q19: What is the difference between deep copy and shallow copy in function arguments?
"""
ANSWER:
- Shallow copy: Copies references to objects (default for mutable objects)
- Deep copy: Creates completely independent copy of nested objects
"""

import copy


def modify_list_shallow(lst):
    """Modifies original list (shallow copy)"""
    lst.append(4)
    return lst


def modify_list_deep(lst):
    """Creates independent copy (deep copy)"""
    new_lst = copy.deepcopy(lst)
    new_lst.append(4)
    return new_lst


# Q20: What are generator functions? How are they different from regular functions?
"""
ANSWER:
Generator functions use 'yield' instead of 'return' and produce values lazily.
They maintain state between calls and are memory-efficient for large datasets.
"""


def number_generator(n):
    """Generator function that yields numbers"""
    for i in range(n):
        yield i**2


def fibonacci_generator():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Usage:
squares = number_generator(5)  # Returns generator object
# for square in squares: print(square)  # 0, 1, 4, 9, 16

fib = fibonacci_generator()
# next(fib)  # 0, 1, 1, 2, 3, 5, 8, ...

# Q21: What is function overloading? Does Python support it?
"""
ANSWER:
Function overloading means having multiple functions with same name
but different parameters. Python doesn't support traditional overloading,
but you can simulate it using default arguments or *args/**kwargs.
"""


def add(a, b=None, c=None):
    """Simulated function overloading"""
    if c is not None:
        return a + b + c
    elif b is not None:
        return a + b
    else:
        return a


def flexible_add(*args):
    """More flexible approach"""
    return sum(args)


# Usage:
# add(5)        # 5
# add(5, 3)     # 8
# add(5, 3, 2)  # 10

# ============================================================================
# SECTION 8: PRACTICAL CODING PROBLEMS
# ============================================================================

# Q22: Write a function to find the factorial of a number (both iterative and recursive).
"""
PROBLEM: Calculate n! = n × (n-1) × ... × 2 × 1
"""


def factorial_iterative(n):
    """Iterative approach"""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Recursive approach"""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# Q23: Write a function to check if a string is a palindrome.
"""
PROBLEM: Check if string reads same forwards and backwards
"""


def is_palindrome_simple(s):
    """Simple approach using string slicing"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def is_palindrome_recursive(s):
    """Recursive approach"""
    s = s.lower().replace(" ", "")

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome_recursive(s[1:-1])


# Q24: Write a function to find the second largest number in a list.
"""
PROBLEM: Find second highest value without sorting entire list
"""


def second_largest(numbers):
    """Find second largest number efficiently"""
    if len(numbers) < 2:
        return None

    largest = second = float("-inf")

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float("-inf") else None


# Q25: Write a function to count word frequency in a text.
"""
PROBLEM: Count how many times each word appears
"""


def word_frequency(text):
    """Count frequency of each word"""
    import re

    # Clean and split text
    words = re.findall(r"\b\w+\b", text.lower())

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def word_frequency_functional(text):
    """Functional approach using collections"""
    from collections import Counter
    import re

    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))


# Q26: Write a function to flatten a nested list.
"""
PROBLEM: Convert [1, [2, 3], [4, [5, 6]]] to [1, 2, 3, 4, 5, 6]
"""


def flatten_list(nested_list):
    """Flatten nested list recursively"""
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def flatten_list_iterative(nested_list):
    """Iterative approach using stack"""
    result = []
    stack = list(nested_list)

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            result.append(item)

    return result[::-1]  # Reverse to maintain order


# ============================================================================
# SECTION 9: TRICKY INTERVIEW SCENARIOS
# ============================================================================

# Q27: What will be the output of this code?
"""
TRICKY QUESTION: Variable binding in loops with closures
"""


def create_functions():
    """Creates list of functions - common interview trap"""
    functions = []

    for i in range(3):
        # TRAP: All functions will use the same 'i' (value 2)
        functions.append(lambda: i)

    return functions


def create_functions_correct():
    """Correct version using default arguments"""
    functions = []

    for i in range(3):
        # SOLUTION: Capture 'i' value at creation time
        functions.append(lambda x=i: x)

    return functions


# Q28: What's the output of this mutable default argument?
"""
TRICKY QUESTION: Mutable default arguments
"""


def append_item(item, target_list=[]):
    """TRAP: Default list is shared between calls"""
    target_list.append(item)
    return target_list


def append_item_correct(item, target_list=None):
    """SOLUTION: Use None and create new list inside"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list


# Usage that shows the problem:
# list1 = append_item(1)     # [1]
# list2 = append_item(2)     # [1, 2] - UNEXPECTED!
# list3 = append_item(3)     # [1, 2, 3] - UNEXPECTED!

# Q29: What happens with late binding closures?
"""
TRICKY QUESTION: Late binding in closures
"""


def create_multipliers():
    """Late binding example"""
    multipliers = []

    for i in range(4):
        # All functions will use i=3 (final value)
        multipliers.append(lambda x: x * i)

    return multipliers


def create_multipliers_fixed():
    """Fixed version"""
    multipliers = []

    for i in range(4):
        # Capture current value of i
        multipliers.append(lambda x, multiplier=i: x * multiplier)

    return multipliers


# Q30: Global vs Local variable confusion
"""
TRICKY QUESTION: Variable scope confusion
"""

x = 10


def confusing_function():
    # This will raise UnboundLocalError
    # Python sees x assignment, treats x as local throughout function
    print(x)  # ERROR: local variable referenced before assignment
    x = 20


def fixed_function():
    global x
    print(x)  # Now it works
    x = 20


# ============================================================================
# SECTION 10: PERFORMANCE AND BEST PRACTICES
# ============================================================================

# Q31: How can you optimize function performance?
"""
ANSWER:
1. Use built-in functions when possible
2. Avoid unnecessary computations
3. Use generators for large datasets
4. Cache results with memoization
5. Choose right data structures
"""


# Memoization example
def fibonacci_memo(n, memo={}):
    """Optimized Fibonacci with memoization"""
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Using functools.lru_cache
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """Fibonacci with automatic caching"""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


# Q32: What are function annotations and type hints?
"""
ANSWER:
Function annotations provide metadata about function parameters and return types.
They improve code readability and enable static type checking.
"""


def calculate_area(length: float, width: float) -> float:
    """Calculate area with type hints"""
    return length * width


def process_data(data: list[int], multiplier: int = 2) -> list[int]:
    """Process data with type annotations"""
    return [x * multiplier for x in data]


# Complex type hints
from typing import Union, Optional, Callable, Dict, List


def advanced_function(
    data: List[Union[int, float]],
    processor: Callable[[float], float],
    config: Optional[Dict[str, str]] = None,
) -> Dict[str, Union[int, float]]:
    """Advanced type hints example"""
    if config is None:
        config = {}

    processed = [processor(x) for x in data]
    return {
        "count": len(processed),
        "sum": sum(processed),
        "average": sum(processed) / len(processed),
    }


# ============================================================================
# INTERVIEW PREPARATION TIPS
# ============================================================================

"""
🎯 INTERVIEW PREPARATION CHECKLIST:

BASIC CONCEPTS (Must Know):
✅ Function definition and calling
✅ Parameters vs arguments
✅ Return statements
✅ Scope rules (LEGB)
✅ *args and **kwargs

INTERMEDIATE CONCEPTS:
✅ Lambda functions and when to use them
✅ map(), filter(), reduce()
✅ List comprehensions vs functions
✅ Generator functions
✅ Function overloading simulation

ADVANCED CONCEPTS:
✅ Decorators and decorator patterns
✅ Closures and variable capture
✅ Higher-order functions
✅ Memoization and optimization
✅ Type hints and annotations

COMMON PITFALLS:
⚠️ Mutable default arguments
⚠️ Late binding closures
⚠️ Variable scope confusion
⚠️ Global vs local variables
⚠️ Function vs method distinction

CODING PROBLEMS PRACTICE:
🔍 Factorial (recursive and iterative)
🔍 Fibonacci with optimization
🔍 Palindrome checking
🔍 List manipulation (flatten, second largest)
🔍 String processing (word frequency)
🔍 Decorator implementation
🔍 Closure-based counters

PERFORMANCE CONSIDERATIONS:
⚡ When to use generators vs lists
⚡ Memoization for expensive computations
⚡ Built-in functions vs custom implementation
⚡ Time and space complexity awareness

BEST PRACTICES:
📝 Clear function names and docstrings
📝 Single responsibility principle
📝 Proper error handling
📝 Type hints for clarity
📝 Testing and validation
"""

# ============================================================================
# SAMPLE INTERVIEW QUESTIONS TO PRACTICE
# ============================================================================

"""
EASY LEVEL:
1. Write a function to check if a number is prime
2. Create a function that returns the sum of digits in a number
3. Write a function to reverse a string without using built-in methods
4. Create a function to find the maximum element in a list
5. Write a function to count vowels in a string

MEDIUM LEVEL:
1. Implement a decorator that logs function calls
2. Create a closure-based counter with increment/decrement
3. Write a function to merge two sorted lists
4. Implement a function that finds common elements in multiple lists
5. Create a generator that produces prime numbers

HARD LEVEL:
1. Implement a memoization decorator from scratch
2. Create a function that can curry other functions
3. Write a function to solve the Tower of Hanoi problem
4. Implement a function that validates balanced parentheses
5. Create a decorator that retries function calls on failure

PRACTICAL SCENARIOS:
1. Design a caching system using functions
2. Create a validation framework using decorators
3. Implement a simple event system with callbacks
4. Build a data processing pipeline with higher-order functions
5. Design a configuration system using closures
"""

print("🎉 Function Interview Questions Guide Complete!")
print("📚 Study each section thoroughly and practice coding problems daily!")
print("💪 Remember: Understanding concepts > Memorizing answers!")
