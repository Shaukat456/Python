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

# Set operations with detailed explanations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set A:", set_a)
print("Set B:", set_b)
print()

# UNION (|) - Combines all unique elements from both sets
# Alternative: set_a.union(set_b)
print("1. UNION (|): All elements from both sets")
print("Union (A | B):", set_a | set_b)  # {1, 2, 3, 4, 5, 6}
print("Method form:", set_a.union(set_b))
print()

# INTERSECTION (&) - Elements common to both sets
# Alternative: set_a.intersection(set_b)
print("2. INTERSECTION (&): Elements common to both sets")
print("Intersection (A & B):", set_a & set_b)  # {3, 4}
print("Method form:", set_a.intersection(set_b))
print()

# DIFFERENCE (-) - Elements in first set but not in second
# Alternative: set_a.difference(set_b)
print("3. DIFFERENCE (-): Elements in A but not in B")
print("Difference (A - B):", set_a - set_b)  # {1, 2}
print("Difference (B - A):", set_b - set_a)  # {5, 6}
print("Method form:", set_a.difference(set_b))
print()

# SYMMETRIC DIFFERENCE (^) - Elements in either set but not in both
# Alternative: set_a.symmetric_difference(set_b)
print("4. SYMMETRIC DIFFERENCE (^): Elements in either set but not both")
print("Symmetric Difference (A ^ B):", set_a ^ set_b)  # {1, 2, 5, 6}
print("Method form:", set_a.symmetric_difference(set_b))
print()

# Additional set methods and comparisons
print("5. SET COMPARISON METHODS:")
print("A is subset of {1,2,3,4,5,6}:", set_a.issubset({1, 2, 3, 4, 5, 6}))
print("A is superset of {1,2}:", set_a.issuperset({1, 2}))
print("A and B are disjoint:", set_a.isdisjoint(set_b))
print()

# ===== COMPREHENSIVE REAL-WORLD USE CASES =====

# Real-world use case 1: Removing duplicates from a list
print("=== USE CASE 1: REMOVING DUPLICATES ===")
emails = [
    "a@example.com",
    "b@example.com",
    "a@example.com",
    "c@example.com",
    "b@example.com",
]
print("Original emails:", emails)
unique_emails = set(emails)
print("Unique emails:", unique_emails)
print("Count: Original =", len(emails), "| Unique =", len(unique_emails))
print()

# Real-world use case 2: Finding common skills between candidates
print("=== USE CASE 2: SKILL MATCHING FOR HIRING ===")
alice_skills = {"python", "sql", "excel", "machine_learning", "statistics"}
bob_skills = {"java", "python", "excel", "spring_boot", "docker"}
charlie_skills = {"python", "javascript", "react", "node.js", "mongodb"}

common_skills_alice_bob = alice_skills & bob_skills
print("Alice skills:", alice_skills)
print("Bob skills:", bob_skills)
print("Common skills (Alice & Bob):", common_skills_alice_bob)
print("Skills only Alice has:", alice_skills - bob_skills)
print("Skills only Bob has:", bob_skills - alice_skills)
print()

# Real-world use case 3: User permissions and access control
print("=== USE CASE 3: ACCESS CONTROL SYSTEM ===")
admin_permissions = {"read", "write", "delete", "execute", "manage_users"}
editor_permissions = {"read", "write", "execute"}
viewer_permissions = {"read"}

print("Admin permissions:", admin_permissions)
print("Editor permissions:", editor_permissions)
print("Can editor delete?", "delete" in editor_permissions)
print("Additional admin privileges:", admin_permissions - editor_permissions)
print()

# Real-world use case 4: E-commerce - Product categories and filtering
print("=== USE CASE 4: E-COMMERCE PRODUCT FILTERING ===")
electronics = {"laptop", "phone", "tablet", "headphones", "camera"}
discounted_items = {"laptop", "shoes", "book", "headphones", "jacket"}
in_stock = {"phone", "tablet", "shoes", "book", "camera", "laptop"}

print("Electronics:", electronics)
print("Discounted items:", discounted_items)
print("In stock:", in_stock)
print("Discounted electronics:", electronics & discounted_items)
print("Available discounted electronics:", electronics & discounted_items & in_stock)
print()

# Real-world use case 5: Social media - Friend recommendations
print("=== USE CASE 5: SOCIAL MEDIA FRIEND RECOMMENDATIONS ===")
alice_friends = {"bob", "charlie", "diana", "eve"}
bob_friends = {"alice", "charlie", "frank", "grace"}
charlie_friends = {"alice", "bob", "diana", "henry"}

# Find mutual friends between Alice and Bob
mutual_friends = alice_friends & bob_friends
print("Alice's friends:", alice_friends)
print("Bob's friends:", bob_friends)
print("Mutual friends:", mutual_friends)

# Recommend friends to Alice (Bob's friends who aren't Alice's friends, excluding Alice herself)
recommendations_for_alice = (bob_friends - alice_friends) - {"alice"}
print("Friend recommendations for Alice:", recommendations_for_alice)
print()

# Real-world use case 6: Data validation and quality control
print("=== USE CASE 6: DATA VALIDATION ===")
required_fields = {"name", "email", "phone", "address"}
received_data_1 = {"name", "email", "phone", "address", "age"}
received_data_2 = {"name", "email", "age"}

print("Required fields:", required_fields)
print("Data 1 fields:", received_data_1)
print("Data 2 fields:", received_data_2)
print("Data 1 has all required?", required_fields.issubset(received_data_1))
print("Data 2 has all required?", required_fields.issubset(received_data_2))
print("Data 2 missing fields:", required_fields - received_data_2)
print()

# Real-world use case 7: Network security - IP address filtering
print("=== USE CASE 7: NETWORK SECURITY ===")
allowed_ips = {"192.168.1.1", "192.168.1.10", "10.0.0.1", "172.16.0.1"}
blocked_ips = {"192.168.1.10", "203.0.113.1", "198.51.100.1"}
incoming_requests = {"192.168.1.1", "192.168.1.10", "203.0.113.1", "10.0.0.5"}

print("Allowed IPs:", allowed_ips)
print("Blocked IPs:", blocked_ips)
print("Incoming requests:", incoming_requests)
print("Requests to allow:", (incoming_requests & allowed_ips) - blocked_ips)
print("Requests to block:", incoming_requests & blocked_ips)
print("Unknown IPs:", incoming_requests - allowed_ips - blocked_ips)
print()

# Real-world use case 8: Inventory management
print("=== USE CASE 8: INVENTORY MANAGEMENT ===")
warehouse_a = {"widget_1", "widget_2", "widget_3", "gadget_1"}
warehouse_b = {"widget_2", "widget_4", "gadget_1", "gadget_2"}
needed_items = {"widget_1", "widget_2", "widget_4", "gadget_2"}

print("Warehouse A inventory:", warehouse_a)
print("Warehouse B inventory:", warehouse_b)
print("Needed items:", needed_items)
print("Available in A:", needed_items & warehouse_a)
print("Available in B:", needed_items & warehouse_b)
print("Available in either warehouse:", needed_items & (warehouse_a | warehouse_b))
print("Items not available anywhere:", needed_items - (warehouse_a | warehouse_b))
print()

# Real-world use case 9: Event planning - Guest management
print("=== USE CASE 9: EVENT PLANNING ===")
invited_guests = {"alice", "bob", "charlie", "diana", "eve", "frank"}
confirmed_guests = {"alice", "charlie", "eve", "frank"}
vip_guests = {"alice", "diana"}
dietary_restrictions = {"bob", "eve"}

print("Invited guests:", invited_guests)
print("Confirmed guests:", confirmed_guests)
print("VIP guests:", vip_guests)
print("Confirmed VIPs:", confirmed_guests & vip_guests)
print("Pending responses:", invited_guests - confirmed_guests)
print(
    "Confirmed guests with dietary restrictions:",
    confirmed_guests & dietary_restrictions,
)
print()

# Real-world use case 10: Software testing - Test coverage
print("=== USE CASE 10: SOFTWARE TESTING ===")
all_functions = {
    "login",
    "logout",
    "create_user",
    "delete_user",
    "update_profile",
    "send_email",
}
unit_tested = {"login", "logout", "create_user", "update_profile"}
integration_tested = {"login", "create_user", "send_email"}
manually_tested = {"delete_user", "update_profile", "send_email"}

print("All functions:", all_functions)
print("Unit tested:", unit_tested)
print("Integration tested:", integration_tested)
print("Manually tested:", manually_tested)

tested_functions = unit_tested | integration_tested | manually_tested
untested_functions = all_functions - tested_functions
fully_tested = unit_tested & integration_tested & manually_tested

print("All tested functions:", tested_functions)
print("Untested functions:", untested_functions)
print("Fully tested (all 3 types):", fully_tested)
print("Coverage percentage:", f"{len(tested_functions)/len(all_functions)*100:.1f}%")
print()

# ===== ADVANCED SET OPERATIONS AND METHODS =====

print("=== ADVANCED SET METHODS ===")
# Creating sets in different ways
set1 = set()  # Empty set
set2 = set([1, 2, 3, 3, 4])  # From list (duplicates removed)
set3 = set("hello")  # From string (unique characters)
set4 = {i for i in range(5) if i % 2 == 0}  # Set comprehension

print("Empty set:", set1)
print("From list [1,2,3,3,4]:", set2)
print("From string 'hello':", set3)
print("Set comprehension (even numbers 0-4):", set4)
print()

# Modifying sets
numbers = {1, 2, 3}
print("Original set:", numbers)

# Adding multiple elements
numbers.update([4, 5, 6])
print("After update([4,5,6]):", numbers)

# Adding elements from another set
numbers.update({7, 8})
print("After update({7,8}):", numbers)

# Removing elements safely
numbers.discard(10)  # No error if element doesn't exist
print("After discard(10) - no error:", numbers)

# Pop random element
popped = numbers.pop()
print("Popped element:", popped)
print("Set after pop:", numbers)

# Clear all elements
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear():", temp_set)
print()

# ===== PERFORMANCE CHARACTERISTICS =====
print("=== PERFORMANCE CHARACTERISTICS ===")
print("Set operations are generally O(1) for:")
print("- Membership testing (in operator)")
print("- Adding elements (add method)")
print("- Removing elements (remove/discard methods)")
print()

# Demonstrating fast membership testing
import time

large_list = list(range(100000))
large_set = set(large_list)

# Testing membership in list vs set
start_time = time.time()
result1 = 99999 in large_list
list_time = time.time() - start_time

start_time = time.time()
result2 = 99999 in large_set
set_time = time.time() - start_time

print(f"Membership test in list of 100,000 items: {list_time:.6f} seconds")
print(f"Membership test in set of 100,000 items: {set_time:.6f} seconds")
print(f"Set is {list_time/set_time:.0f}x faster for membership testing")
print()

# ===== SET VS OTHER DATA STRUCTURES =====
print("=== WHEN TO USE SETS ===")
print("Use sets when you need:")
print("1. Unique elements only")
print("2. Fast membership testing")
print("3. Mathematical set operations (union, intersection, etc.)")
print("4. Removing duplicates from data")
print("5. Finding relationships between datasets")
print()
print("Don't use sets when you need:")
print("1. Ordered data (use list or tuple)")
print("2. Indexed access (use list)")
print("3. Mutable elements (sets require hashable/immutable elements)")
print("4. Duplicate values (use list)")
print()

# Sets are mutable, but their elements must be immutable (hashable).
# You cannot have a set of sets, but you can have a set of tuples.
set_of_tuples = {(1, 2), (3, 4), (1, 2)}  # Duplicate tuple removed
print("Set of tuples:", set_of_tuples)

# Frozen sets - immutable version of sets
frozen_set1 = frozenset([1, 2, 3])
frozen_set2 = frozenset([3, 4, 5])
print("Frozen set 1:", frozen_set1)
print("Frozen set union:", frozen_set1 | frozen_set2)

# You can have a set of frozen sets
set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print("Set of frozen sets:", set_of_frozensets)
print()

# ===== COMMON PITFALLS AND TIPS =====
print("=== COMMON PITFALLS ===")
print("1. Empty set must be created with set(), not {}")
empty_dict = {}  # This is a dictionary!
empty_set = set()  # This is a set!
print("Type of {}:", type(empty_dict))
print("Type of set():", type(empty_set))
print()

print("2. Sets cannot contain mutable elements:")
# This would cause an error:
# bad_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
good_set = {(1, 2), (3, 4)}  # Tuples are hashable
print("Set with tuples works:", good_set)
print()

print("3. Set order is not guaranteed (though stable in Python 3.7+)")
sample_set = {"c", "a", "b"}
print("Set order:", sample_set)
print("Note: Order preservation is implementation detail, don't rely on it!")
print()

# ===== SUMMARY OF SET OPERATORS ===
print("=== SUMMARY OF SET OPERATORS ===")
print("| - Union (combine all unique elements)")
print("& - Intersection (common elements only)")
print("- - Difference (elements in first set but not second)")
print("^ - Symmetric Difference (elements in either set but not both)")
print()
print("Comparison operators:")
print("<= - Subset (all elements of left set are in right set)")
print(">= - Superset (left set contains all elements of right set)")
print("< - Proper subset (subset but not equal)")
print("> - Proper superset (superset but not equal)")
print("== - Equal sets")
print("!= - Not equal sets")
