# perform arithmetic operations in python

# 1. Addition
a = 10
b = 20
c = a + b

print(c)


# 2. Subtraction
a = 20
b = 10
c = a - b


print(c)


# 3. Multiplication
a = 10
b = 20
c = a * b


print(c)


# 4. Division
a = 20
b = 10
c = a / b


print(c)


# 5. Modulus
a = 20
b = 10
c = a % b


print(c)


# 6. Exponentiation
a = 2
b = 3

c = a**b


print(c)


# 7. Floor Division meaning the result is the integer value "discarding any fractional part"
a = 20
b = 3
c = a // b
print(c)  # Output: 6 - This performs floor division of a by b.

# Ceil division is not directly available in Python, but you can achieve it using the `math.ceil()` function.

import math

# Example of Ceil Division
a = 20
b = 3
ceil_division = math.ceil(a / b)
print(ceil_division)  # Output: 7 - This performs ceil division of a by b.

# 8. Augmented Assignment
a = 10
b = 20
print(a)

a = a + b
a += b

print(a)


# Adds b to a and updates a or a = a + b
print(a)  # Output: 30 - a is updated to 30 after addition.

# 9. Augmented Assignment
a = 20
b = 10

a = a - b

a -= b  # Subtracts b from a and updates a.
print(a)  # Output: 10 - a is updated to 10 after subtraction.

# 10. Augmented Assignment
a = 10
b = 20
a *= b  # Multiplies a by b and updates a.
print(a)  # Output: 200 - a is updated to 200 after multiplication.

# 11. Augmented Assignment
a = 20
b = 10

a = a / b
a /= b  # Divides a by b and updates a.
print(a)  # Output: 2.0 - a is updated to 2.0 after division.

# 12. Augmented Assignment
a = 20
b = 10
a %= b  # Calculates the remainder of a divided by b and updates a.
print(a)  # Output: 0 - a is updated to 0 as 20 is divisible by 10.

# 13. Augmented Assignment
a = 2
b = 3
a **= b  # Raises a to the power of b and updates a.
print(a)  # Output: 8 - a is updated to 8 as 2 raised to the power of 3 is 8.

# 14. Augmented Assignment
a = 20
b = 3
a //= b  # Performs floor division of a by b and updates a.
# Output: 6 - a is updated to 6 after floor division.


# 15. Comparison Operators

# 1. Equal to
a = 10

b = 20
c = a == b
print(c)


# Output: False - as 10 is not equal to 20.


# 2. Not equal to
a = 10

b = 20

print(a != b)  # Output: True - as 10 is not equal to 20.


# 3. Greater than
a = 10

b = 2 / 2

print(a < b)


# Output: False - as 10 is not greater than 20.


# 4. Less than
a = 10
b = 20
print(a < b)  # Output: True - as 10 is less than 20.


# 5. Greater than or equal to
a = 10
b = 20
print(a >= b)  # Output: False - as 10 is not greater than or equal to 20.


# 6. Less than or equal to
a = 10
b = 20

print(a <= b)  # Output: True - as 10 is less than or equal to 20.


# 16. Logical Operators

# 1. and
a = 10
b = 20

print(a > 5 and b < 30)  # Output: True - as both conditions are True.


# 2. or
a = 10
b = 20

print(a > 5 or b > 30)  # Output: True - as one of the conditions is True.


# 3. not
a = 10
print(not a > 5)  # Output: False - as the condition is True.


# 17. Identity Operators

# 1. is
a = 10
b = 10

print(a is b)  # Output: True - as both a and b are equal.


# 2. is not
a = 10
b = 20

print(a is not b)  # Output: True - as a is not equal to b.


# Topic after covering list

# 18. Membership Operators

# 1. in
list = [10, 20, 30, 40, 50]

print(10 in list)  # Output: True - as 10 is present in the list.


# 2. not in
list = [10, 20, 30, 40, 50]

print(60 not in list)  # Output: True - as 60 is not present in the list.
