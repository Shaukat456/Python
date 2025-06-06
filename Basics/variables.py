# Variables in python

# Variables are used to store data values in Python. A variable is created by assigning a value to it using the assignment operator (=). The value of a variable can be changed or updated throughout the program.

# Variables can store different types of data, such as numbers, strings, lists, tuples, dictionaries, etc.


#  Python is a dynamically typed language, so you don't need to specify the data type of a variable when you create it.

# Variable Naming Rules

# Variable names can contain letters, numbers, and underscores.

# Variable names must start with a letter or an underscore (_).

# Variable names are case-sensitive (name, Name, and NAME are different variables).

# Variable names cannot contain spaces or special characters, except for underscores (_).

# Variable names should be descriptive and meaningful (e.g., name, age, total_marks).

# Variable names should not be the same as Python keywords (e.g., if, else, for, while, etc.).

# Assigning Values to Variables

# You can assign a value to a variable using the assignment operator (=). The value on the right side of the assignment operator is assigned to the variable on the left side.

# Example:

name = "Alice"
age = 25
total_marks = 95.5
print(name, age, total_marks)

# In this example, we assigned the values "Alice" to the variable name, 25 to the variable age, and 95.5 to the variable total_marks. We then printed the values of these variables using the print() function.

# Multiple Assignments

# You can assign multiple values to multiple variables in a single line using multiple assignment.

# Example:

name, age, total_marks = "Alice", 25, 95.5
print(name, age, total_marks)

# In this example, we assigned the values "Alice" to the variable name, 25 to the variable age, and 95.5 to the variable total_marks in a single line. We then printed the values of these variables using the print() function.


# Constants in Python

# Constants are similar to variables, but their values remain constant throughout the program. In Python, you can create constants by using uppercase letters and underscores to separate words in the variable name.

# Example:

PI = 3.14159
GRAVITY = 9.81
MAX_SPEED = 300
# Constants are used to represent fixed values that should not be changed during the execution of the program. By convention, constant names are written in uppercase to distinguish them from variables.

# Constants are not enforced by the Python interpreter, so you can still change the value of a constant. However, it is a good practice to treat them as read-only variables and avoid changing their values.

# Example:

PI = 3.14159
PI = 3.14  # This is allowed, but not recommended


# In this example, we defined a constant PI with the value 3.14159. Although we can change the value of PI later in the program, it is not recommended to do so. Constants should be treated as read-only variables to maintain code clarity and prevent accidental changes.
