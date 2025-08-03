# commonFn.py
# Common Built-in Functions in Python

"""
COMPREHENSIVE GUIDE: PYTHON BUILT-IN FUNCTIONS

This file covers essential built-in functions:
1. Type Conversion Functions: int(), float(), str(), bool(), list(), tuple(), set(), dict()
2. Mathematical Functions: abs(), max(), min(), sum(), round(), pow(), divmod()
3. Sequence Functions: len(), sorted(), reversed(), enumerate(), zip(), range()
4. Iterator Functions: iter(), next(), all(), any()
5. Higher-order Functions: map(), filter(), reduce()
6. Type Checking: type(), isinstance(), hasattr(), getattr(), setattr()
7. I/O Functions: print(), input(), open()
8. Utility Functions: id(), hash(), repr(), eval(), exec()
"""

# commonFn.py
# Common Built-in Functions in Python

"""
COMPREHENSIVE GUIDE: PYTHON BUILT-IN FUNCTIONS

This file covers essential built-in functions:
1. Type Conversion Functions: int(), float(), str(), bool(), list(), tuple(), set(), dict()
2. Mathematical Functions: abs(), max(), min(), sum(), round(), pow(), divmod()
3. Sequence Functions: len(), sorted(), reversed(), enumerate(), zip(), range()
4. Iterator Functions: iter(), next(), all(), any()
5. Higher-order Functions: map(), filter(), reduce()
6. Type Checking: type(), isinstance(), hasattr(), getattr(), setattr()
7. I/O Functions: print(), input(), open()
8. Utility Functions: id(), hash(), repr(), eval(), exec()
"""

# ============================================================================
# SECTION 1: TYPE CONVERSION FUNCTIONS
# ============================================================================

# Type conversion functions allow you to convert data from one type to another
# Essential for data processing, user input handling, and API interactions

# Example 1: int() Function - Convert to Integer
# The int() function converts various data types to integers
# Useful for processing user input, mathematical calculations, and data validation

# Convert a string to an integer
string = "123"
number = int(string)
# Result: number = 123 (type: int)

# Convert a float to an integer (truncates decimal part)
float_number = 3.14
integer_number = int(float_number)
# Result: integer_number = 3 (decimal part removed)

# Convert a boolean to an integer
boolean = True
integer_boolean = int(boolean)
# Result: integer_boolean = 1 (True=1, False=0)

# Convert binary, octal, hex strings with base parameter
binary_str = "1010"
octal_str = "12"
hex_str = "A"
binary_to_int = int(binary_str, 2)  # Result: 10
octal_to_int = int(octal_str, 8)  # Result: 10
hex_to_int = int(hex_str, 16)  # Result: 10

# Error handling for invalid conversions
try:
    invalid_int = int("hello")
except ValueError as e:
    print(f"Error converting to int: {e}")
    # This will raise ValueError: invalid literal for int()
    pass


# Example 2: float() Function - Convert to Float
# The float() function converts numbers and strings to floating-point numbers
# Essential for mathematical operations requiring decimal precision

# Convert string to float
float_str = "3.14159"
pi = float(float_str)
# Result: pi = 3.14159

# Convert integer to float
int_num = 42
float_num = float(int_num)
# Result: float_num = 42.0

# Special float values - useful for mathematical operations and comparisons
infinity = float("inf")  # Positive infinity
neg_infinity = float("-inf")  # Negative infinity
not_a_number = float("nan")  # Not a Number (NaN)

# Example 3: str() Function - Convert to String
# The str() function converts any object to its string representation
# Critical for display, logging, and text processing

# Convert numbers to strings
number = 42
pi = 3.14159
number_str = str(number)  # Result: "42"
pi_str = str(pi)  # Result: "3.14159"

# Convert list to string
my_list = [1, 2, 3, 4, 5]
list_str = str(my_list)  # Result: "[1, 2, 3, 4, 5]"

# Convert boolean to string
bool_val = True
bool_str = str(bool_val)  # Result: "True"

# Example 4: bool() Function - Convert to Boolean
# The bool() function converts values to True or False
# Essential for conditional logic and data validation

# Various values and their boolean equivalents
test_values = [0, 1, -1, "", "hello", [], [1, 2, 3], {}, {"key": "value"}, None]

# Value → Boolean conversion results:
# 0 → False (zero integer)
# 1 → True (non-zero integer)
# -1 → True (negative integer)
# "" → False (empty string)
# "hello" → True (non-empty string)
# [] → False (empty list)
# [1, 2, 3] → True (non-empty list)
# {} → False (empty dictionary)
# {"key": "value"} → True (non-empty dictionary)
# None → False (None value)

for value in test_values:
    bool_result = bool(value)
    # Each value shows its boolean conversion pattern

# Example 5: tuple() Function - Convert to Tuple
# The tuple() function creates immutable sequences from other iterables
# Useful for creating read-only data structures and function returns

# Convert a list to a tuple
numbers = [1, 2, 3]
number_tuple = tuple(numbers)  # Result: (1, 2, 3) - immutable version

# Convert a string to a tuple
myname = "John"
name_tuple = tuple(myname)  # Result: ('J', 'o', 'h', 'n')

# Convert range to tuple
range_tuple = tuple(range(5))  # Result: (0, 1, 2, 3, 4)

# Convert dictionary keys to tuple
my_dict = {"a": 1, "b": 2, "c": 3}
keys_tuple = tuple(my_dict.keys())  # Result: ('a', 'b', 'c')

# Example 6: list() Function - Convert to List
# The list() function creates mutable sequences from other iterables
# Essential for creating modifiable collections from immutable data

# Convert a tuple to a list
numbers = (1, 2, 3)
number_list = list(numbers)  # Result: [1, 2, 3] - mutable version

# Convert a string to a list
word = "Python"
char_list = list(word)  # Result: ['P', 'y', 't', 'h', 'o', 'n']

# Convert range to list
range_list = list(range(1, 6))  # Result: [1, 2, 3, 4, 5]

# Convert set to list
my_set = {3, 1, 4, 1, 5}
set_list = list(my_set)  # Result: [1, 3, 4, 5] (order may vary)

# Example 7: set() Function - Convert to Set
# The set() function creates collections of unique elements
# Crucial for removing duplicates and set operations

# Convert list to set (removes duplicates)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_with_duplicates)
# Original: [1, 2, 2, 3, 3, 3, 4, 5]
# Result: {1, 2, 3, 4, 5} - duplicates removed

# Convert string to set
word = "programming"
char_set = set(word)  # Result: {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}

# Example 8: dict() Function - Create Dictionary
# The dict() function creates key-value mappings from various sources
# Fundamental for data organization and lookup operations

# Create dictionary from key-value pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)  # Result: {'a': 1, 'b': 2, 'c': 3}

# Create dictionary using keyword arguments
dict_from_kwargs = dict(name="Alice", age=30, city="New York")
# Result: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Create dictionary from two lists using zip
keys = ["name", "age", "city"]
values = ["Bob", 25, "Chicago"]
dict_from_zip = dict(zip(keys, values))
# zip combines keys and values into a dictionary
# Result: {'name': 'Bob', 'age': 25, 'city': 'Chicago'}

# ============================================================================
# SECTION 2: MATHEMATICAL FUNCTIONS
# ============================================================================

# 🧮 MATHEMATICAL FUNCTIONS
# These functions perform mathematical operations and calculations

# Example 9: abs() Function - Absolute Value
# Returns the absolute (positive) value of a number
# Essential for distance calculations and magnitude operations

numbers = [-5, -3.14, 0, 7, 10.5]
# Number → Absolute Value results:
# -5 → 5
# -3.14 → 3.14
# 0 → 0
# 7 → 7
# 10.5 → 10.5

for num in numbers:
    abs_val = abs(num)
    # Process each number's absolute value

# Example 10: max() and min() Functions
# Find the largest and smallest values in sequences
# Critical for data analysis and boundary detection

# With numbers
numbers = [3, 7, 2, 9, 1, 8, 5]
maximum = max(numbers)  # Result: 9
minimum = min(numbers)  # Result: 1

# With strings (lexicographic order)
words = ["apple", "banana", "cherry", "date"]
max_word = max(words)  # Result: "date" (alphabetically last)
min_word = min(words)  # Result: "apple" (alphabetically first)

# With key function for complex data
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]
best_student = max(students, key=lambda student: student[1])  # ("Diana", 95)
worst_student = min(students, key=lambda student: student[1])  # ("Charlie", 78)

# Example 11: sum() Function
# Calculates the total of all numeric elements in an iterable
# Essential for statistical calculations and data aggregation

# Sum numbers
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # Result: 15

# Sum with start value
total_with_start = sum(numbers, 10)  # Result: 25 (15 + 10)

# Sum of squares using generator expression
squares_sum = sum(x**2 for x in range(1, 6))  # Result: 55 (1+4+9+16+25)

# Example 12: round() Function
# Rounds numbers to specified decimal places
# Critical for formatting financial data and measurements

# Round to nearest integer
pi = 3.14159
rounded_int = round(pi)  # Result: 3
rounded_2dp = round(pi, 2)  # Result: 3.14
rounded_4dp = round(pi, 4)  # Result: 3.1416

# Round negative numbers
negative = -2.675
neg_rounded_int = round(negative)  # Result: -3
neg_rounded_2dp = round(negative, 2)  # Result: -2.67 (banker's rounding)

# Example 13: pow() Function - Power Operation
# Calculates base raised to the power of exponent
# Optimized for large numbers and modular arithmetic

# Basic power
base, exponent = 2, 3
result = pow(base, exponent)  # Result: 8 (2³)

# Power with modulo (useful in cryptography)
base, exponent, modulo = 2, 10, 3
result_mod = pow(base, exponent, modulo)  # Result: 1 (2¹⁰ mod 3)

# Comparison with ** operator
pow_result = pow(2, 3)  # Result: 8
operator_result = 2**3  # Result: 8 (same but less efficient for large numbers)

# Example 14: divmod() Function
# Returns quotient and remainder of division in a single operation
# Efficient for mathematical calculations requiring both values

# Divmod returns (quotient, remainder)
dividend, divisor = 17, 5
quotient, remainder = divmod(dividend, divisor)  # Result: (3, 2)
# Verification: 3 × 5 + 2 = 17 ✓

# Practical example: Convert minutes to hours and minutes
total_minutes = 125
hours, minutes = divmod(total_minutes, 60)  # Result: (2, 5)
# 125 minutes = 2 hours and 5 minutes

# ============================================================================
# SECTION 3: SEQUENCE FUNCTIONS
# ============================================================================

# 📝 SEQUENCE FUNCTIONS
# These functions work with sequences like lists, tuples, strings

# Example 15: len() Function - Length of Sequences
# Returns the number of items in a sequence or collection
# Fundamental for iteration bounds and data validation

# Different types of sequences
sequences = [
    [1, 2, 3, 4, 5],  # list → length: 5
    (1, 2, 3),  # tuple → length: 3
    "Hello, World!",  # string → length: 13
    {1, 2, 3, 4},  # set → length: 4
    {"a": 1, "b": 2, "c": 3},  # dictionary → length: 3
]

for seq in sequences:
    length = len(seq)
    # __name__ is the type of the sequence
    # what is type(seq).__name__
    seq_type = type(seq).__name__
    # Each sequence type shows its item count: list: 5, tuple: 3, etc.

# Example 16: sorted() Function - Sort Sequences
# Returns a new sorted list from any iterable
# Essential for data organization and searching algorithms

# Sort numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)  # Result: [1, 1, 2, 3, 4, 5, 6, 9]

# Sort in reverse
sorted_reverse = sorted(numbers, reverse=True)  # Result: [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)  # Result: ['apple', 'banana', 'cherry', 'date']

# Sort by length
sorted_by_length = sorted(
    words, key=len
)  # Result: ['date', 'apple', 'banana', 'cherry']

# Sort complex data
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
# Result: [("Bob", 92), ("Alice", 85), ("Charlie", 78)]

# Example 17: reversed() Function
print("↩️ reversed() Function - Reverse Sequences:")

# Reverse list
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(f"Original: {numbers}")
print(f"Reversed: {reversed_numbers}")

# Reverse string
word = "Python"
reversed_word = "".join(reversed(word))
print(f"Original: '{word}'")
print(f"Reversed: '{reversed_word}'")

# Note: reversed() returns an iterator, so we convert to list/string
print(f"reversed() object: {reversed(numbers)}")

print()

# Example 18: enumerate() Function
print("🔢 enumerate() Function - Index and Value:")

# Enumerate list
fruits = ["apple", "banana", "cherry", "date"]
print("Index: Value")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Enumerate with custom start
print("\nWith start=1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")

# Practical example: Menu display
menu_items = ["New File", "Open File", "Save File", "Exit"]
print("\nMenu:")
for i, item in enumerate(menu_items, 1):
    print(f"  {i}. {item}")

print()

# Example 19: zip() Function
print("🔗 zip() Function - Combine Sequences:")

# Zip two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Chicago", "Los Angeles"]

print("Combining lists:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# Zip three lists
print("\nCombining three lists:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} ({age}) lives in {city}")

# Create dictionary from zip
person_dict = dict(zip(names, ages))
print(f"\nDictionary from zip: {person_dict}")

# Unzip using zip with unpacking
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(f"Unzipping: {pairs}")
print(f"Letters: {letters}")
print(f"Numbers: {numbers}")

print()

# Example 20: range() Function
print("🎯 range() Function - Generate Number Sequences:")

# Basic range
print("range(5):", list(range(5)))
print("range(1, 6):", list(range(1, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

# Practical examples
print("\nPractical examples:")
print("Even numbers 0-10:", [x for x in range(0, 11) if x % 2 == 0])
print("Odd numbers 1-10:", [x for x in range(1, 11, 2)])

print()

# ============================================================================
# SECTION 4: ITERATOR FUNCTIONS
# ============================================================================

print("\n🔄 SECTION 4: ITERATOR FUNCTIONS")
print("-" * 35)

# Example 21: iter() Function
print("🔁 iter() Function - Create Iterators:")

# Create iterator from list
numbers = [1, 2, 3, 4, 5]
number_iterator = iter(numbers)
print(f"List: {numbers}")
print(f"Iterator object: {number_iterator}")

# Create iterator from string
word = "Hello"
char_iterator = iter(word)
print(f"String: '{word}'")
print(f"Character iterator: {char_iterator}")

# Create iterator with callable and sentinel
import random

random.seed(42)  # For reproducible results


def random_number():
    return random.randint(1, 6)


# This creates an iterator that calls random_number() until it returns 6
dice_iterator = iter(random_number, 6)
print("Rolling dice until we get 6:")
dice_rolls = []
for roll in dice_iterator:
    dice_rolls.append(roll)
    if len(dice_rolls) > 10:  # Safety limit for demo
        break
print(f"Dice rolls: {dice_rolls}")

print()

# Example 22: next() Function
print("➡️ next() Function - Get Next Item from Iterator:")

# Using next() with iterator
fruits = ["apple", "banana", "cherry"]
fruit_iterator = iter(fruits)

print("Getting items one by one:")
print(f"First: {next(fruit_iterator)}")
print(f"Second: {next(fruit_iterator)}")
print(f"Third: {next(fruit_iterator)}")

# Handle StopIteration with default value
print(f"Fourth (with default): {next(fruit_iterator, 'No more fruits')}")


# Create infinite iterator and use next()
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_iterator = fibonacci()
print("\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {next(fib_iterator)}")

print()

# Example 23: all() Function
print("✅ all() Function - Check if All Elements are True:")

# Test different cases
test_cases = [
    [True, True, True],
    [True, False, True],
    [1, 2, 3, 4],
    [1, 0, 3, 4],
    [],
    ["hello", "world"],
    ["hello", "", "world"],
]

print("Sequence → all() result:")
for case in test_cases:
    result = all(case)
    print(f"  {str(case):25} → {result}")

# Practical example: Validate form data
form_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": "25",
    "terms_accepted": True,
}

# Check if all required fields are filled
required_fields = ["name", "email", "age"]
all_filled = all(form_data.get(field, "") for field in required_fields)
print(f"\nForm validation - all required fields filled: {all_filled}")

# Check if all numbers are positive
numbers = [1, 5, 3, 8, 2]
all_positive = all(x > 0 for x in numbers)
print(f"All numbers {numbers} are positive: {all_positive}")

print()

# Example 24: any() Function
print("🔍 any() Function - Check if Any Element is True:")

# Test different cases
test_cases = [
    [False, False, False],
    [False, True, False],
    [0, 0, 0],
    [0, 1, 0],
    [],
    ["", "", ""],
    ["", "hello", ""],
]

print("Sequence → any() result:")
for case in test_cases:
    result = any(case)
    print(f"  {str(case):25} → {result}")

# Practical examples
grades = [45, 52, 38, 67, 43]
has_passing_grade = any(grade >= 60 for grade in grades)
print(f"\nGrades {grades} - any passing (≥60): {has_passing_grade}")

permissions = ["read", "write", "execute"]
user_permissions = ["read", "write"]
has_admin_access = any(
    perm in user_permissions for perm in ["admin", "root", "execute"]
)
print(f"User has admin access: {has_admin_access}")

print()

# ============================================================================
# SECTION 5: TYPE CHECKING AND INTROSPECTION
# ============================================================================

print("\n🔍 SECTION 5: TYPE CHECKING AND INTROSPECTION")
print("-" * 50)

# Example 25: type() Function
print("🏷️ type() Function - Get Object Type:")

# Different types of objects
objects = [
    42,
    3.14,
    "hello",
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    {"key": "value"},
    lambda x: x * 2,
    print,
]

print("Object → Type:")
for obj in objects:
    obj_type = type(obj)
    print(f"  {str(obj):20} → {obj_type}")

print()

# Example 26: isinstance() Function
print("✅ isinstance() Function - Check if Object is Instance of Type:")

# Single type checking
test_value = 42
print(f"Value: {test_value}")
print(f"isinstance({test_value}, int): {isinstance(test_value, int)}")
print(f"isinstance({test_value}, float): {isinstance(test_value, float)}")
print(f"isinstance({test_value}, str): {isinstance(test_value, str)}")

# Multiple type checking (more Pythonic than type())
print(f"isinstance({test_value}, (int, float)): {isinstance(test_value, (int, float))}")


# Practical example: Input validation
def process_number(value):
    """Process a number, accepting both int and float"""
    if isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, str):
        try:
            return float(value) * 2
        except ValueError:
            return f"Cannot convert '{value}' to number"
    else:
        return f"Unsupported type: {type(value)}"


test_inputs = [42, 3.14, "25", "hello", [1, 2, 3]]
print("\nInput validation example:")
for input_val in test_inputs:
    result = process_number(input_val)
    print(f"  {str(input_val):10} → {result}")

print()

# Example 27: hasattr() Function
print("🔍 hasattr() Function - Check if Object has Attribute:")


# Test with different objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}"


person = Person("Alice", 30)
test_string = "hello"
test_list = [1, 2, 3]

objects_and_attrs = [
    (person, "name"),
    (person, "age"),
    (person, "greet"),
    (person, "height"),
    (test_string, "upper"),
    (test_string, "length"),
    (test_list, "append"),
    (test_list, "sort"),
]

print("Object, Attribute → hasattr() result:")
for obj, attr in objects_and_attrs:
    has_attr = hasattr(obj, attr)
    obj_desc = f"{type(obj).__name__} object"
    print(f"  {obj_desc:15}, '{attr}':10 → {has_attr}")

print()

# Example 28: getattr() and setattr() Functions
print("🔧 getattr() and setattr() Functions - Get/Set Attributes:")


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x):
        self.result += x
        return self.result

    def multiply(self, x):
        self.result *= x
        return self.result


calc = Calculator()

# getattr() with default value
print("Using getattr():")
result_attr = getattr(calc, "result", "Not found")
print(f"getattr(calc, 'result'): {result_attr}")

nonexistent = getattr(calc, "nonexistent", "Default value")
print(f"getattr(calc, 'nonexistent', 'Default'): {nonexistent}")

# Dynamic method calling
method_name = "add"
if hasattr(calc, method_name):
    method = getattr(calc, method_name)
    result = method(5)
    print(f"Dynamic method call calc.{method_name}(5): {result}")

# setattr() to add new attributes
print("\nUsing setattr():")
setattr(calc, "history", [])
setattr(calc, "precision", 2)

print(f"Added 'history' attribute: {calc.history}")
print(f"Added 'precision' attribute: {calc.precision}")

# Verify new attributes exist
print(f"hasattr(calc, 'history'): {hasattr(calc, 'history')}")

print()

# ============================================================================
# SECTION 6: HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n🎛️ SECTION 6: HIGHER-ORDER FUNCTIONS")
print("-" * 40)

# Example 29: map() Function
print("🗺️ map() Function - Apply Function to All Items:")

# Basic map usage
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

# Map with built-in function
strings = ["1", "2", "3", "4", "5"]
integers = list(map(int, strings))
print(f"Strings: {strings}")
print(f"Integers: {integers}")

# Map with multiple iterables
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"List 1: {numbers1}")
print(f"List 2: {numbers2}")
print(f"Sums: {sums}")

# Practical example: Process user data
users = [
    {"name": "alice", "age": 25},
    {"name": "bob", "age": 30},
    {"name": "charlie", "age": 35},
]

# Capitalize names
capitalized_users = list(
    map(lambda user: {**user, "name": user["name"].title()}, users)
)
print(f"\nOriginal users: {users}")
print(f"Capitalized names: {capitalized_users}")

print()

# Example 30: filter() Function
print("🔍 filter() Function - Filter Items Based on Condition:")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers: {evens}")

# Filter strings by length
words = ["cat", "elephant", "dog", "hippopotamus", "ant"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"\nWords: {words}")
print(f"Words longer than 5 chars: {long_words}")

# Filter with None (removes falsy values)
mixed_values = [1, 0, "hello", "", True, False, None, [1, 2], []]
truthy_values = list(filter(None, mixed_values))
print(f"\nMixed values: {mixed_values}")
print(f"Truthy values: {truthy_values}")

# Practical example: Filter valid emails
emails = [
    "alice@example.com",
    "invalid-email",
    "bob@test.org",
    "",
    "charlie@company.co.uk",
]
valid_emails = list(filter(lambda email: "@" in email and "." in email, emails))
print(f"\nAll emails: {emails}")
print(f"Valid emails: {valid_emails}")

print()

# Example 31: reduce() Function (from functools)
print("🔄 reduce() Function - Reduce Sequence to Single Value:")

from functools import reduce

# Reduce to find product of all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product: {product}")

# Reduce to find maximum
numbers = [3, 7, 2, 9, 1, 8, 5]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"\nNumbers: {numbers}")
print(f"Maximum: {maximum}")

# Reduce with initial value
numbers = [1, 2, 3, 4, 5]
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(f"\nSum with initial value 10: {sum_with_initial}")

# Practical example: Flatten nested lists
nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
flattened = reduce(lambda acc, lst: acc + lst, nested_lists, [])
print(f"\nNested lists: {nested_lists}")
print(f"Flattened: {flattened}")

print()

# ============================================================================
# SECTION 7: I/O AND UTILITY FUNCTIONS
# ============================================================================

print("\n💻 SECTION 7: I/O AND UTILITY FUNCTIONS")
print("-" * 40)

# Example 32: id() Function
print("🆔 id() Function - Get Object Identity:")

# Different objects and their IDs
a = [1, 2, 3]
b = [1, 2, 3]  # Same content, different object
c = a  # Same object reference

print(f"a = {a}, id: {id(a)}")
print(f"b = {b}, id: {id(b)}")
print(f"c = {c}, id: {id(c)}")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")

# Immutable objects (small integers are cached)
x = 5
y = 5
print(f"\nx = {x}, id: {id(x)}")
print(f"y = {y}, id: {id(y)}")
print(f"x is y: {x is y}")

print()

# Example 33: hash() Function
print("🔐 hash() Function - Get Hash Value:")

# Hashable objects
hashable_objects = [42, 3.14, "hello", (1, 2, 3), frozenset([1, 2, 3])]

print("Hashable objects and their hashes:")
for obj in hashable_objects:
    hash_value = hash(obj)
    print(f"  {str(obj):20} → {hash_value}")

# Unhashable objects (will raise TypeError)
unhashable_objects = [[1, 2, 3], {1, 2, 3}, {"key": "value"}]

print("\nUnhashable objects:")
for obj in unhashable_objects:
    try:
        hash_value = hash(obj)
        print(f"  {str(obj):20} → {hash_value}")
    except TypeError as e:
        print(f"  {str(obj):20} → TypeError: {e}")

print()

# Example 34: repr() Function
print("📝 repr() Function - String Representation for Developers:")

# Different objects and their repr
objects = [42, 3.14, "hello\nworld", [1, 2, 3], {"key": "value"}, None, True]

print("Object → repr():")
for obj in objects:
    repr_str = repr(obj)
    print(f"  {str(obj):15} → {repr_str}")

# Difference between str() and repr()
text_with_newline = "Hello\nWorld"
print(f"\nString with newline:")
print(f"str():  '{str(text_with_newline)}'")
print(f"repr(): {repr(text_with_newline)}")

print()

# Example 35: eval() Function (Use with Caution!)
print("⚠️ eval() Function - Evaluate String as Python Expression:")

# Safe examples
safe_expressions = ["2 + 3", "10 ** 2", "len('hello')", "max([1, 2, 3, 4, 5])"]

print("Safe eval() examples:")
for expr in safe_expressions:
    try:
        result = eval(expr)
        print(f"  eval('{expr}') = {result}")
    except Exception as e:
        print(f"  eval('{expr}') → Error: {e}")

# WARNING: eval() can be dangerous with untrusted input!
print("\n⚠️ WARNING: Never use eval() with untrusted input!")
print("   eval() can execute arbitrary code and is a security risk.")

print()

# ============================================================================
# SECTION 8: PRACTICAL EXAMPLES AND USE CASES
# ============================================================================

print("\n🎯 SECTION 8: PRACTICAL EXAMPLES")
print("-" * 35)

print("🏪 REAL-WORLD EXAMPLE: Online Store Order Processing")
print("-" * 55)

# Sample order data
orders = [
    {
        "id": 1001,
        "items": ["laptop", "mouse"],
        "amounts": [999.99, 25.99],
        "customer": "alice",
    },
    {
        "id": 1002,
        "items": ["keyboard", "monitor"],
        "amounts": [79.99, 349.99],
        "customer": "bob",
    },
    {"id": 1003, "items": ["tablet"], "amounts": [299.99], "customer": "charlie"},
]


def process_orders(orders):
    """Process orders using various built-in functions"""

    # Calculate totals using sum() and zip()
    print("📊 Order Processing:")
    processed_orders = []

    for order in orders:
        order_id = str(order["id"])
        customer = order["customer"].title()  # str() method
        items = order["items"]
        amounts = order["amounts"]

        # Calculate total using sum()
        total = sum(amounts)

        # Create item-price pairs using zip()
        item_details = list(zip(items, amounts))

        # Format currency using round()
        formatted_total = round(total, 2)

        processed_order = {
            "id": order_id,
            "customer": customer,
            "items": len(items),  # len()
            "total": formatted_total,
            "details": item_details,
        }

        processed_orders.append(processed_order)

        print(f"  Order {order_id}: {customer}")
        print(f"    Items: {', '.join(items)}")
        print(f"    Total: ${formatted_total}")

    # Find highest order using max()
    highest_order = max(processed_orders, key=lambda x: x["total"])
    print(f"\n🏆 Highest order: #{highest_order['id']} - ${highest_order['total']}")

    # Calculate overall statistics
    all_totals = [order["total"] for order in processed_orders]
    print(f"\n📈 Statistics:")
    print(f"    Total orders: {len(processed_orders)}")
    print(f"    Total revenue: ${sum(all_totals)}")
    print(f"    Average order: ${round(sum(all_totals) / len(all_totals), 2)}")
    print(f"    Min order: ${min(all_totals)}")
    print(f"    Max order: ${max(all_totals)}")

    return processed_orders


# Process the orders
processed = process_orders(orders)

print()

# ============================================================================
# SUMMARY AND BEST PRACTICES
# ============================================================================

print("\n💡 SUMMARY AND BEST PRACTICES")
print("=" * 40)

summary_tips = """
🔧 TYPE CONVERSION:
   • Use int(), float(), str() for basic conversions
   • Handle ValueError exceptions for invalid conversions
   • Remember bool() treats empty containers as False

🧮 MATHEMATICAL:
   • abs() for absolute values, round() for precision
   • max()/min() with key parameter for custom comparisons
   • sum() with generator expressions for efficiency

📝 SEQUENCES:
   • len() works on all sequences and collections
   • sorted() returns new list, doesn't modify original
   • enumerate() when you need both index and value
   • zip() for parallel iteration

🔄 ITERATORS:
   • iter() to create iterators, next() to get values
   • all() returns True if ALL elements are truthy
   • any() returns True if ANY element is truthy

🔍 TYPE CHECKING:
   • isinstance() preferred over type() for type checking
   • hasattr() to safely check for attributes
   • getattr() with default values for safe attribute access

🎛️ HIGHER-ORDER:
   • map() for transformations, filter() for selections
   • List comprehensions often more readable than map/filter
   • reduce() for cumulative operations

⚠️ SAFETY TIPS:
   • Never use eval() with untrusted input
   • Handle exceptions when converting types
   • Use isinstance() for robust type checking
   • Remember that empty containers are falsy
"""

print(summary_tips)

print("\n🎉 BUILT-IN FUNCTIONS MASTERY COMPLETE!")
print("💪 These functions are the building blocks of Python programming!")
