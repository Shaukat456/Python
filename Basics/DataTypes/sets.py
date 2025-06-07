# sets.py
# Introduction to Sets in Python

# What is a set?
# A set is an unordered collection of unique elements.

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# Adding elements
fruits.add("orange")
print("After adding orange:", fruits)

# Removing elements
fruits.remove("banana")  # Raises KeyError if not present
print("After removing banana:", fruits)

# Discarding elements (no error if not present)
fruits.discard("banana")
print("After discarding banana again:", fruits)

# Checking membership
print("Is apple in fruits?", "apple" in fruits)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print("Union:", set_a | set_b)  # {1, 2, 3, 4, 5, 6}

# Intersection
print("Intersection:", set_a & set_b)  # {3, 4}

# Difference
print("Difference (A - B):", set_a - set_b)  # {1, 2}

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)  # {1, 2, 5, 6}

# Real-world use case 1: Removing duplicates from a list
emails = ["a@example.com", "b@example.com", "a@example.com"]
unique_emails = set(emails)
print("Unique emails:", unique_emails)

# Real-world use case 2: Finding common skills between two candidates
alice_skills = {"python", "sql", "excel"}
bob_skills = {"java", "python", "excel"}
common_skills = alice_skills & bob_skills
print("Common skills:", common_skills)

# Real-world use case 3: Checking if two groups have no members in common
group1 = {"alice", "bob"}
group2 = {"carol", "dave"}
print("Groups disjoint?", group1.isdisjoint(group2))  # True

# Sets are mutable, but their elements must be immutable (hashable).
# You cannot have a set of sets, but you can have a set of tuples.
set_of_tuples = {(1, 2), (3, 4)}
print("Set of tuples:", set_of_tuples)
