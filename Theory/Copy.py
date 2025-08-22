"""
Deep Copy vs Shallow Copy in Python
==================================
Copying objects is a fundamental concept in Python, especially when working with mutable data structures like lists, dictionaries, and custom objects. Understanding the difference between shallow and deep copies helps prevent bugs and unexpected behavior.
"""

import copy

# 1. Shallow Copy
# ---------------
# A shallow copy creates a new object, but does NOT recursively copy nested objects.
# Instead, it copies references to the nested objects.

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

# Modifying a nested element affects both original and shallow copy
shallow[0][0] = 99
# Both original[0][0] and shallow[0][0] are now 99

# 2. Deep Copy
# -------------
# A deep copy creates a new object AND recursively copies all nested objects.
# Changes to nested objects do NOT affect the original.

deep = copy.deepcopy(original)
deep[0][1] = 88
# Only deep[0][1] is changed; original remains unchanged

# 3. Copy by Value vs Copy by Reference
# -------------------------------------
# Copy by value: A new, independent object is created (e.g., numbers, strings)
# Copy by reference: Only the reference (address) is copied; both variables point to the same object (e.g., lists, dicts)

# Example: Copy by value
x = 5
y = x  # y is a new value, changing y does not affect x

# Example: Copy by reference
list1 = [10, 20, 30]
list2 = list1  # Both refer to the same list object
list2[0] = 99  # list1[0] is also 99

# Summary Table
# =============
# | Type           | What is copied?         | Changes affect original? |
# |----------------|------------------------|--------------------------|
# | Shallow Copy   | Top-level object only   | Yes (for nested objects) |
# | Deep Copy      | All nested objects      | No                       |
# | By Value       | New independent object  | No                       |
# | By Reference   | Reference/address only  | Yes                      |

# Real-World Example: Data Analysis
# ---------------------------------
# When working with large datasets, use deep copy to avoid accidental changes to the original data.
# Use shallow copy for performance when you know nested objects won't be modified.

# Practical Tip:
# Use copy.deepcopy() for safe duplication of complex objects.
# Use copy.copy() for simple, top-level copies.
# For immutable types (int, str, tuple), assignment always copies by value.
