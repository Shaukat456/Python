# explain why we need to use the function in programming


# Functions are a way to organize code into reusable blocks. They allow you to define a set of instructions that can be called multiple times with different inputs. This helps to reduce code duplication, improve readability, and make the code easier to maintain.


# Functions also help in modularizing code, making it easier to understand and debug. They allow you to break down complex problems into smaller, more manageable parts, which can be tested and debugged independently.


# syntax of a function in python

# def function_name(parameters):

#     # block of code

#     return value


# what is the meaning of return in a function

# The return statement is used to exit a function and return a value to the caller. It can be used to pass data back from the function to the calling code. The return statement can also be used to terminate the execution of a function prematurely.


# example of a function in python

# def add(a, b):
#     return a + b


# result = add(10, 20)

# print(result)


# what is the meaning of parameters in a function

# Parameters are variables that are used to pass values to a function. They are defined in the function definition and are used to specify the inputs that the function expects. Parameters allow you to pass data to a function and customize its behavior based on the inputs provided.


# what is the meaning of arguments in a function


# Arguments are the actual values that are passed to a function when it is called. They are the values that are assigned to the parameters defined in the function definition. Arguments are used to provide input data to the function and determine its behavior based on the specific values passed.


# example of a function with multiple parameters


def multiply(a, b):
    return a * b


result = multiply(5, 10)


print(result)


# example of a function with default parameters


def greet(name="World"):
    return f"Hello, {name}!"


message = greet("Alice")
print(message)

# example of a function with keyword arguments


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


message = greet("Alice", greeting="Hi")
print(message)


message = greet("Bob")
print(message)


# example of a function with variable number of arguments


def add(*args):
    total = 0
    for num in args:
        total += num
    return total


result = add(1, 2, 3, 4, 5)


print(result)


# example of a function with variable number of keyword arguments


def greet(**kwargs):
    if "name" in kwargs and "greeting" in kwargs:
        return f"{kwargs['greeting']}, {kwargs['name']}!"
    else:
        return "Hello, World!"


message = greet(name="Alice", greeting="Hi")
print(message)


# example of a function with a docstring


def greet(name):
    """
    This function greets the user by name.
    """
    return f"Hello, {name}!"


message = greet("Alice")


print(message)


# give an example of a function that takes a list as an argument and returns the sum of all the elements in the list


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


result = sum_list([1, 2, 3, 4, 5])


print(result)


# give an example of a function that takes a string as an argument and returns the number of vowels in the string


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


result = count_vowels("Hello, World!")


print(result)


# give an example of a function that takes a list of numbers as an argument and returns the average of the numbers


def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


result = average([1, 2, 3, 4, 5])


print(result)


# give an example of a function that takes a list of strings as an argument and returns the longest string in the list


def longest_string(strings):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest


result = longest_string(["apple", "banana", "cherry", "date"])


print(result)


# Exercise 2: Concatenate Strings
# Task:
# Write a function called concatenate_strings that takes two strings as arguments and returns them concatenated together with a space in between.


def concatenate_strings(str1, str2):
    return str1 + " " + str2


result = concatenate_strings("Hello", "World")
print(result)


# Task:
# Write a function called list_length that takes a list as an argument and returns the length of the list.
[2, 6, 3, 1, 9]


def list_length(anyList):
    return len(anyList)


result = list_length([1, 2, 3, 4, 5])
anotherList = list_length([54, 345, 3, 345])
print(result)


#  Check Substring
# Write a function called contains_substring that takes two strings as arguments and returns True if the second string is found within the first string, otherwise returns False.


def contains_substring(main_str, sub_str):
    return sub_str in main_str


# Test the function
result = contains_substring("Hello, world!", "somethinglikethis")
print(result)  # Output: True


# Reverse String
# Write a function called reverse_string that takes a string as an argument and returns the string reversed.

# sequence[start:stop:step]


def is_palindrome(s):
    # Reverse the string using slicing
    reversed_s = s[::-1]

    # Check if the original string is equal to the reversed string
    return s == reversed_s


# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


def reverse_string(s):

    return s[::-1]


# Test the function
reversed_str = reverse_string("Python")
print(reversed_str)


#  Find Key in Dictionary

# Write a function called find_key that takes a dictionary and a key as arguments and returns True if the key is found in the dictionary, otherwise returns False.


def find_key(d, key):
    return key in d


# Test the function
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}
result = find_key(sample_dict, "age")
print(result)


# Count words in a string
string1 = "shaukat"


def count_words(s):
    words = s.split()

    length = len(words)
    return length


# Test the function
word_count = count_words("The quick brown fox jumps over the lazy dog")
print(word_count)


#  Join List into String

# Write a function called join_list that takes a list of strings as an argument and returns a single string with all the list elements joined by a comma and a space.


def join_list(lst):
    return ", ".join(lst)


# Test the function
joined_str = join_list(["apple", "banana", "cherry"])
print(joined_str)


# Assignment start


# extract the unique words from a string
def unique_words(s):
    words = s.lower().split()
    uniqueWords = set(words)
    return list(uniqueWords)


# Test the function
unique = unique_words("This is a test. This test is only a test.")
print(unique)  # Output: ['this', 'is', 'a', 'test.', 'only']


# count Characters
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Test the function
char_freq = count_characters("hello world")
print(char_freq)


# Remove duplicates from a list


def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Test the function
unique_list = remove_duplicates(["apple", "banana", "apple", "cherry", "banana"])
print(unique_list)


# resubale sum function WE can use this function to add any number of numbers


def add(*args):
    total = 0
    for num in args:
        total += num
    return total


# Test the function
result = add(1, 2, 3, 4, 5)
print(result)


# Function real life analogy
# Functions are like recipes in a cookbook. Just as a recipe provides step-by-step instructions to create a dish, a function provides a set of instructions to perform a specific task in programming.

#  You can use the same recipe (function) multiple times with different ingredients (arguments) to create different dishes (outputs). Functions help organize code, making it easier to read and maintain, just like recipes help organize cooking steps.

# In both cases, you can follow the same process to achieve different results based on the inputs you provide.

# Functions allow you to break down complex tasks into smaller, manageable parts, just as recipes break down cooking into individual steps. This modular approach makes it easier to understand and debug both in programming and cooking.

# Use Case 1: Mathematical Operations
# Functions can be used to perform mathematical operations, such as addition, subtraction, multiplication, and division.


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


result = divide(10, 2)
print(result)  # Output: 5.0

# Use Case 2: String Manipulation
# Functions can process and manipulate strings, such as reversing, formatting, or finding substrings.


def capitalize_words(sentence):
    return " ".join(word.capitalize() for word in sentence.split())


result = capitalize_words("hello world")
print(result)  # Output: "Hello World"

# Use Case 3: Data Processing
# Functions can process data structures like lists, dictionaries, or sets to extract or transform information.


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


result = filter_even_numbers([1, 2, 3, 4, 5, 6])
print(result)  # Output: [2, 4, 6]

# Use Case 4: Real-World Analogy
# Functions can simulate real-world processes, such as calculating discounts or processing orders.


def calculate_discount(price, discount_rate):
    return price - (price * discount_rate / 100)


result = calculate_discount(100, 10)
print(result)  # Output: 90.0

# Use Case 5: Recursive Functions
# Functions can call themselves to solve problems like factorials or Fibonacci sequences.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


result = factorial(5)
print(result)  # Output: 120

# Use Case 6: Higher-Order Functions
# Functions can accept other functions as arguments or return them as results.


def apply_function(func, value):
    return func(value)


result = apply_function(lambda x: x**2, 5)
print(result)  # Output: 25

# Use Case 7: File Operations
# Functions can handle file operations, such as reading or writing data to files.


def read_file(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


# Uncomment the following line to test with an actual file path:
# print(read_file("example.txt"))
