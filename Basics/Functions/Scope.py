# Global scope example
# Variables defined outside of any function are in the global scope.
# They can be accessed from any function within the same module.

global_var = "I am a global variable"


def global_example():
    # Accessing the global variable inside a function
    print(global_var)


global_example()  # Output: I am a global variable

# Local scope example
# Variables defined inside a function are in the local scope.
# They can only be accessed within that function.


def local_example():
    local_var = "I am a local variable"
    print(local_var)


local_example()  # Output: I am a local variable

# Trying to access the local variable outside its function will cause an error
# print(local_var)  # Uncommenting this line will raise a NameError

# Analogy:
# Think of the global scope as a city's public park. Everyone in the city can access it.
# The local scope is like a private garden in someone's backyard. Only the people in that house can access it.

# Modifying global variables inside a function
# To modify a global variable inside a function, use the 'global' keyword.


def modify_global():
    global global_var
    global_var = "I have been modified"
    print(global_var)


modify_global()  # Output: I have been modified
print(global_var)  # Output: I have been modified

# Accessibility example
# Variables defined in the global scope can be accessed from any function.
# Variables defined in the local scope can only be accessed within that function.


def access_example():
    # Accessing the global variable
    print(global_var)

    # Defining a local variable
    local_var = "I am another local variable"
    print(local_var)


access_example()  # Output: I am a global variable
# Output: I am another local variable

# Trying to access the local variable outside its function will cause an error
# print(local_var)  # Uncommenting this line will raise a NameError

# Nested function example
# A variable defined in an outer function can be accessed by an inner function.


def outer_function():
    outer_var = "I am an outer variable"

    def inner_function():
        print(outer_var)

    inner_function()


outer_function()  # Output: I am an outer variable


# However, the inner function's variables are not accessible to the outer function
def another_outer_function():
    def another_inner_function():
        inner_var = "I am an inner variable"
        print(inner_var)

    another_inner_function()
    # Trying to access the inner variable outside its function will cause an error
    # print(inner_var)  # Uncommenting this line will raise a NameError


another_outer_function()  # Output: I am an inner variable
