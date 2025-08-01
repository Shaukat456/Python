# usecases.py
# When to Use Different Data Structures in Python
# Lists vs Tuples vs Dictionaries vs Sets

"""
COMPREHENSIVE GUIDE: CHOOSING THE RIGHT DATA STRUCTURE

This file covers:
1. When to use each data structure
2. Real-world examples
3. Performance considerations
4. Common interview questions
5. Decision flowchart
"""

print("=" * 60)
print("PYTHON DATA STRUCTURES: WHEN TO USE WHAT")
print("=" * 60)
print()

# ===== LISTS: WHEN TO USE =====
print("🔸 LISTS - Ordered, Mutable Collections")
print("-" * 40)
print("Use Lists When:")
print("✓ You need ordered data")
print("✓ You need to modify elements (add, remove, change)")
print("✓ You need indexed access (list[0], list[1])")
print("✓ You allow duplicate values")
print("✓ You need to append/prepend frequently")
print()

print("Real-World Examples:")
print("1. Shopping Cart Items")
shopping_cart = ["laptop", "mouse", "keyboard", "laptop"]  # Duplicates allowed
print("Shopping cart:", shopping_cart)
shopping_cart.append("monitor")  # Easy to add
shopping_cart.remove("laptop")  # Remove one instance
print("Updated cart:", shopping_cart)
print()

print("2. User Activity Log")
activity_log = []
activity_log.append("User logged in at 09:00")
activity_log.append("User viewed profile at 09:05")
activity_log.append("User updated settings at 09:10")
print("Activity log:", activity_log)
print("Latest activity:", activity_log[-1])
print()

print("3. Task Queue (Processing Order Matters)")
task_queue = ["send_email", "backup_database", "generate_report"]
while task_queue:
    current_task = task_queue.pop(0)  # FIFO - First In, First Out
    print(f"Processing: {current_task}")
print()

print("4. Student Grades (Sequential Data)")
grades = [85, 92, 78, 96, 88]
print("Grades:", grades)
print("Average:", sum(grades) / len(grades))
print("Highest grade:", max(grades))
print("Grade improvement:", [grades[i] - grades[i - 1] for i in range(1, len(grades))])
print()

print("5. Game High Scores (Ordered List)")
high_scores = [1500, 1200, 1100, 950, 800]
new_score = 1300
# Insert new score in correct position
for i, score in enumerate(high_scores):
    if new_score > score:
        high_scores.insert(i, new_score)
        break
print("Updated high scores:", high_scores[:5])  # Keep top 5
print()

# ===== TUPLES: WHEN TO USE =====
print("🔸 TUPLES - Ordered, Immutable Collections")
print("-" * 40)
print("Use Tuples When:")
print("✓ Data should not change (immutable)")
print("✓ You need ordered data")
print("✓ You want to use as dictionary keys (hashable)")
print("✓ You're returning multiple values from functions")
print("✓ You need structured data (like records)")
print()

print("Real-World Examples:")
print("1. Geographic Coordinates")
location_paris = (48.8566, 2.3522)  # (latitude, longitude)
location_london = (51.5074, -0.1278)
print("Paris coordinates:", location_paris)
print("Cannot modify:", "location_paris[0] = 50  # Would raise TypeError")
print()

print("2. RGB Color Values")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = {"primary_red": red, "primary_green": green, "primary_blue": blue}
print("Colors dictionary:", colors)
print()

print("3. Database Records (Structured Data)")
employee_1 = ("John Doe", 30, "Engineer", 75000)
employee_2 = ("Jane Smith", 28, "Designer", 70000)
employees = [employee_1, employee_2]
print("Employee records:", employees)
# Accessing structured data
name, age, position, salary = employee_1  # Tuple unpacking
print(f"Employee: {name}, Age: {age}, Position: {position}, Salary: ${salary}")
print()

print("4. Function Return Multiple Values")


def get_user_stats(user_id):
    # Simulate database query
    return (
        "alice123",
        150,
        "Premium",
        "2023-01-15",
    )  # username, points, status, join_date


username, points, status, join_date = get_user_stats(123)
print(f"User: {username}, Points: {points}, Status: {status}, Joined: {join_date}")
print()

print("5. Date and Time")
today = (2025, 8, 1)  # (year, month, day)
meeting_time = (14, 30, 0)  # (hour, minute, second)
print("Date:", today)
print("Time:", meeting_time)
print()

print("6. Mathematical Points and Vectors")
point_a = (3, 4)
point_b = (6, 8)
vector = (point_b[0] - point_a[0], point_b[1] - point_a[1])
print(f"Vector from {point_a} to {point_b}: {vector}")
print()

# ===== DICTIONARIES: WHEN TO USE =====
print("🔸 DICTIONARIES - Key-Value Pairs")
print("-" * 40)
print("Use Dictionaries When:")
print("✓ You need key-value relationships")
print("✓ You need fast lookups by key")
print("✓ You need to map one thing to another")
print("✓ Order doesn't matter (or insertion order is fine)")
print("✓ You need to group related data")
print()

print("Real-World Examples:")
print("1. User Profile Data")
user_profile = {
    "username": "alice123",
    "email": "alice@example.com",
    "age": 28,
    "premium": True,
    "last_login": "2025-08-01",
    "preferences": {"theme": "dark", "notifications": True},
}
print("User profile:", user_profile)
print("Quick access to email:", user_profile["email"])
print("Is premium user?", user_profile["premium"])
print()

print("2. Inventory Management")
inventory = {
    "laptop": {"quantity": 50, "price": 999.99, "supplier": "TechCorp"},
    "mouse": {"quantity": 200, "price": 25.99, "supplier": "AccessoryCo"},
    "keyboard": {"quantity": 100, "price": 79.99, "supplier": "KeyMaster"},
}
print("Laptop inventory:", inventory["laptop"])
print(
    "Total laptop value:",
    inventory["laptop"]["quantity"] * inventory["laptop"]["price"],
)
print()

print("3. Configuration Settings")
app_config = {
    "database": {"host": "localhost", "port": 5432, "name": "myapp_db"},
    "cache": {"enabled": True, "ttl": 3600},
    "features": {"user_registration": True, "email_notifications": False},
}
print("Database config:", app_config["database"])
print("Cache enabled?", app_config["cache"]["enabled"])
print()

print("4. Word Frequency Counter")
text = "python is great python is powerful python is fun"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequencies:", word_count)
print("Most common word:", max(word_count, key=word_count.get))
print()

print("5. API Response Mapping")
api_response = {
    "status": "success",
    "data": {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]},
    "metadata": {"total": 2, "page": 1, "per_page": 10},
}
print("API status:", api_response["status"])
print("Total users:", api_response["metadata"]["total"])
print()

print("6. Caching System")
cache = {}


def expensive_calculation(n):
    if n in cache:
        print(f"Cache hit for {n}")
        return cache[n]

    # Simulate expensive calculation
    result = n**2 + n * 10
    cache[n] = result
    print(f"Calculated and cached result for {n}")
    return result


print("First call:", expensive_calculation(5))
print("Second call:", expensive_calculation(5))  # Will use cache
print("Cache contents:", cache)
print()

# ===== SETS: WHEN TO USE =====
print("🔸 SETS - Unique Elements Collection")
print("-" * 40)
print("Use Sets When:")
print("✓ You need unique elements only")
print("✓ You need fast membership testing")
print("✓ You need mathematical set operations")
print("✓ Order doesn't matter")
print("✓ You need to remove duplicates")
print()

print("Real-World Examples:")
print("1. Unique Website Visitors")
daily_visitors = {"user123", "user456", "user789", "user123"}  # Duplicate removed
print("Unique visitors today:", daily_visitors)
print("Visitor count:", len(daily_visitors))
print()

print("2. Required vs Available Skills")
required_skills = {"python", "sql", "git", "docker"}
candidate_skills = {"python", "javascript", "sql", "react"}
print("Required skills:", required_skills)
print("Candidate skills:", candidate_skills)
print("Missing skills:", required_skills - candidate_skills)
print("Extra skills:", candidate_skills - required_skills)
print("Matching skills:", required_skills & candidate_skills)
print()

print("3. Access Control")
admin_users = {"admin1", "admin2", "superuser"}
current_user = "admin1"
if current_user in admin_users:
    print(f"{current_user} has admin access")
else:
    print(f"{current_user} does not have admin access")
print()

# ===== PERFORMANCE COMPARISON =====
print("🔸 PERFORMANCE COMPARISON")
print("-" * 40)
import time

# Create test data
test_data = list(range(10000))
test_list = test_data.copy()
test_tuple = tuple(test_data)
test_dict = {i: f"value_{i}" for i in test_data}
test_set = set(test_data)

print("Performance for 10,000 items:")
print()

# Membership testing
target = 9999

start = time.time()
result = target in test_list
list_time = time.time() - start

start = time.time()
result = target in test_tuple
tuple_time = time.time() - start

start = time.time()
result = target in test_dict
dict_time = time.time() - start

start = time.time()
result = target in test_set
set_time = time.time() - start

print("Membership Testing (finding element 9999):")
print(f"List:       {list_time:.6f} seconds")
print(f"Tuple:      {tuple_time:.6f} seconds")
print(f"Dictionary: {dict_time:.6f} seconds")
print(f"Set:        {set_time:.6f} seconds")
print()

# Access by index/key
start = time.time()
result = test_list[5000]
list_access_time = time.time() - start

start = time.time()
result = test_tuple[5000]
tuple_access_time = time.time() - start

start = time.time()
result = test_dict[5000]
dict_access_time = time.time() - start

print("Access by Index/Key:")
print(f"List[5000]:       {list_access_time:.6f} seconds")
print(f"Tuple[5000]:      {tuple_access_time:.6f} seconds")
print(f"Dict[5000]:       {dict_access_time:.6f} seconds")
print("Set: No index access available")
print()

# ===== INTERVIEW QUESTIONS AND ANSWERS =====
print("🔸 COMMON INTERVIEW QUESTIONS")
print("-" * 40)
print()

print("Q1: When would you use a tuple instead of a list?")
print("A1: Use tuples when:")
print("   - Data should not change (coordinates, RGB values)")
print("   - You need to use it as a dictionary key")
print("   - You're returning multiple values from a function")
print("   - You want to ensure data integrity")
print("   Example: coordinates = (40.7128, -74.0060)  # NYC lat/lng")
print()

print("Q2: Why use a dictionary instead of a list for user data?")
print("A2: Dictionaries provide:")
print("   - O(1) lookup time vs O(n) for lists")
print("   - Meaningful keys instead of numeric indices")
print("   - Self-documenting code")
print("   - Easy to add/remove fields")
print("   Example: user = {'name': 'John', 'age': 30} vs user = ['John', 30]")
print()

print("Q3: When should you use a set?")
print("A3: Use sets when you need:")
print("   - Unique elements only")
print("   - Fast membership testing O(1)")
print("   - Mathematical operations (union, intersection)")
print("   - To remove duplicates from data")
print("   Example: unique_emails = set(email_list)")
print()

print("Q4: What's the difference between list and tuple performance?")
print("A4:")
print("   - Tuples: Faster creation, less memory, immutable")
print("   - Lists: Slower creation, more memory, but mutable")
print("   - Both have O(1) index access")
print("   - Tuples can be used as dict keys, lists cannot")
print()

print("Q5: How do you choose between dict and set?")
print("A5:")
print("   - Use dict when you need key-value pairs")
print("   - Use set when you only need to track existence")
print("   - Dict: user_roles = {'alice': 'admin', 'bob': 'user'}")
print("   - Set: admin_users = {'alice', 'charlie'}")
print()

print("Q6: Can you store mutable objects in sets?")
print("A6: No, sets can only contain hashable (immutable) objects:")
print("   - ✓ Valid: {1, 'hello', (1,2), frozenset([1,2])}")
print("   - ✗ Invalid: {[1,2], {1:2}, set([1,2])}  # Lists, dicts, sets")
print()

# ===== DECISION FLOWCHART =====
print("🔸 DECISION FLOWCHART")
print("-" * 40)
print(
    """
CHOOSING THE RIGHT DATA STRUCTURE:

Start Here
    ↓
Do you need key-value pairs?
    ├─ YES → Use DICTIONARY
    └─ NO → Continue
        ↓
Do you need only unique elements?
    ├─ YES → Use SET
    └─ NO → Continue
        ↓
Will the data change after creation?
    ├─ NO → Use TUPLE
    └─ YES → Use LIST

Additional Considerations:
- Need fast lookup? → Dictionary or Set
- Need ordered data? → List or Tuple
- Need to use as dict key? → Tuple only
- Need mathematical operations? → Set
- Need indexed access? → List or Tuple
"""
)
print()

# ===== SUMMARY TABLE =====
print("🔸 SUMMARY TABLE")
print("-" * 40)
print(
    """
| Feature          | List | Tuple | Dict | Set |
|------------------|------|-------|------|-----|
| Ordered          |  ✓   |   ✓   |  ✓*  |  ✗  |
| Mutable          |  ✓   |   ✗   |  ✓   |  ✓  |
| Indexed Access   |  ✓   |   ✓   |  ✗   |  ✗  |
| Key-Value Pairs  |  ✗   |   ✗   |  ✓   |  ✗  |
| Unique Elements  |  ✗   |   ✗   |  ✗** |  ✓  |
| Hashable         |  ✗   |   ✓   |  ✗   |  ✗  |
| Fast Lookup      |  ✗   |   ✗   |  ✓   |  ✓  |
| Duplicates       |  ✓   |   ✓   |  ✗** |  ✗  |

* Insertion order preserved (Python 3.7+)
** Keys are unique, values can be duplicated
"""
)
print()

# ===== PRACTICAL EXERCISE =====
print("🔸 PRACTICAL EXERCISE")
print("-" * 40)
print("Given the following scenarios, choose the best data structure:")
print()

scenarios = [
    ("Storing a person's name, age, and email", "Dictionary (key-value pairs)"),
    ("Storing GPS coordinates that won't change", "Tuple (immutable, ordered)"),
    ("Storing items in a shopping cart", "List (ordered, allows duplicates)"),
    ("Tracking unique website visitors", "Set (unique elements only)"),
    ("Storing configuration settings", "Dictionary (nested key-value pairs)"),
    ("Storing the top 10 high scores", "List (ordered, indexed access)"),
    ("Storing allowed file extensions", "Set (unique, fast membership testing)"),
    ("Storing RGB color values", "Tuple (immutable, structured data)"),
]

for i, (scenario, answer) in enumerate(scenarios, 1):
    print(f"{i}. {scenario}")
    print(f"   Answer: {answer}")
    print()

print("=" * 60)
print("CONCLUSION")
print("=" * 60)
print("The key to choosing the right data structure is understanding:")
print("1. What operations you need to perform")
print("2. Whether data will change")
print("3. Performance requirements")
print("4. Whether you need unique elements")
print("5. Whether you need key-value relationships")
print()
print("Remember: The right data structure can make your code more")
print("efficient, readable, and maintainable!")
