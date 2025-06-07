# Data Types in Python

# 1. Integer
# Integers are whole numbers, positive or negative, without decimals.
# Example:
age = 25
print(f"Age: {age}")

# Real-world usage: Counting items, age calculation, etc.

# 2. Float
# Floats are numbers with a decimal point.
# Example:
price = 19.99
print(f"Price: {price}")

# Real-world usage: Financial calculations, measurements, etc.

# 3. String
# Strings are sequences of characters, used to store text.
# Example:
name = "John Doe"
print(f"Name: {name}")


name = "Alice"
greeting = "Hello, world!"

# * Strings can contain letters, numbers, spaces, symbols — anything you can type!


# * Example: `"Python123"`, `'Hi!'`, `"It's a nice day."`


## Creating Strings

str1 = "Hello"
str2 = "World"
print(str1)
print(str2)

## Common String Operations

### 1. Concatenation (Joining strings)

full_greeting = str1 + " " + str2  # Adds a space between
print(full_greeting)  # Output: Hello World

### 2. Repetition

echo = "ha" * 3
print(echo)  # Output: hahaha

### 3. Accessing Characters (Indexing)

# * Strings are indexed starting from 0.
# * You can get a single character using square brackets `[]`.

word = "Python"
print(word[0])  # Output: P (first letter)
print(word[3])  # Output: h (4th letter)

### 4. Slicing (Getting a part of string)

print(word[0:3])  # Output: Pyt (characters from index 0 to 2)
print(word[2:])  # Output: thon (from 3rd character till end)
print(word[:4])  # Output: Pyth (first 4 characters)

## Useful String Methods

### - `len()`: Length of a string

print(len(word))  # Output: 6

### - `.lower()` and `.upper()`: Change case

print(word.lower())  # Output: python
print(word.upper())  # Output: PYTHON

### - `.strip()`: Remove whitespace from start and end

s = "  hello  "
print(s.strip())  # Output: "hello"

### - `.replace(old, new)`: Replace part of string

text = "I like apples"
print(text.replace("apples", "oranges"))  # Output: I like oranges

### - `.split(separator)`: Split string into list by separator

sentence = "Python is fun"
words = sentence.split()  # By default splits at spaces
print(words)  # Output: ['Python', 'is', 'fun']


## String Formatting (Insert variables in strings)

# name = "Alice"
# age = 25
# message = f"My name is {name} and I am {age} years old."
# print(message)
# # Output: My name is Alice and I am 25 years old.
# ```

# ---

# ## Summary

# | Operation     | Example                                        | Result                    |
# | ------------- | ---------------------------------------------- | ------------------------- |
# | Create string | `name = "Alice"`                               | `Alice`                   |
# | Concatenate   | `"Hi " + "there"`                              | `Hi there`                |
# | Repeat        | `"ha" * 3`                                     | `hahaha`                  |
# | Index         | `"Python"[0]`                                  | `P`                       |
# | Slice         | `"Python"[1:4]`                                | `yth`                     |
# | Length        | `len("Python")`                                | `6`                       |
# | Lowercase     | `"Python".lower()`                             | `python`                  |
# | Uppercase     | `"Python".upper()`                             | `PYTHON`                  |
# | Replace       | `"I like apples".replace("apples", "oranges")` | `I like oranges`          |
# | Split         | `"Python is fun".split()`                      | `['Python', 'is', 'fun']` |

# ---


# Real-world usage: Storing names, addresses, any textual information.

# 4. Boolean
# Booleans represent one of two values: True or False.
# Example:
is_student = True
print(f"Is student: {is_student}")

# Real-world usage: Conditional statements, flags, etc.
