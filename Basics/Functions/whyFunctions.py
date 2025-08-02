# whyFunctions.py
# Why Functions Are Important and Needed in Programming

"""
WHY FUNCTIONS MATTER: A COMPREHENSIVE GUIDE

This file demonstrates:
1. Why functions are essential in programming
2. Real-world analogies to understand functions
3. Problems that functions solve
4. Benefits of using functions
5. Examples showing before/after function implementation
"""

# ===== REAL-WORLD ANALOGY: FUNCTIONS ARE LIKE RECIPES =====

# Think of functions like cooking recipes:
# - A recipe has a name (like "Chocolate Cake")
# - It takes ingredients (inputs/parameters)
# - It has step-by-step instructions (function body)
# - It produces a final dish (output/return value)
# - You can use the same recipe multiple times
# - You can share the recipe with others

# Example: Without functions (like cooking without recipes)
# Imagine you want to make chocolate cake 3 times but don't have a recipe
# You'd have to remember and repeat all steps each time:

# First cake - writing all steps from scratch
flour_1 = 2  # cups
sugar_1 = 1.5  # cups
cocoa_1 = 0.5  # cups
# ... mix ingredients
# ... bake at 350°F for 30 minutes
# ... let cool
cake_1 = "First chocolate cake ready"

# Second cake - repeating all steps again
flour_2 = 2  # cups
sugar_2 = 1.5  # cups
cocoa_2 = 0.5  # cups
# ... same mixing process
# ... same baking process
# ... same cooling process
cake_2 = "Second chocolate cake ready"

# Third cake - repeating again (getting tedious!)
flour_3 = 2  # cups
sugar_3 = 1.5  # cups
cocoa_3 = 0.5  # cups
# ... repeat everything once more
cake_3 = "Third chocolate cake ready"


# With functions (like having a recipe)
def make_chocolate_cake(servings=8):
    """
    A reusable 'recipe' for making chocolate cake
    Input: number of servings (ingredients scale automatically)
    Output: completed cake
    """
    # Calculate ingredients based on servings
    flour = (2 * servings) / 8  # scale recipe
    sugar = (1.5 * servings) / 8
    cocoa = (0.5 * servings) / 8

    # Follow the recipe steps (function body)
    # Step 1: Mix dry ingredients
    # Step 2: Add wet ingredients
    # Step 3: Bake at 350°F for 30 minutes
    # Step 4: Let cool

    return f"Chocolate cake for {servings} people ready!"


# Now making multiple cakes is easy - just call the function
cake_1 = make_chocolate_cake(8)  # Standard size
cake_2 = make_chocolate_cake(12)  # Larger for party
cake_3 = make_chocolate_cake(4)  # Small for family

# ===== PROBLEM 1: CODE DUPLICATION (DRY PRINCIPLE) =====

# DRY = Don't Repeat Yourself
# Imagine you're building a calculator and need to add numbers frequently

# Without functions - repetitive code
# Calculating total price for customer 1
item1_price = 25.99
item2_price = 15.50
item3_price = 8.75
tax_rate = 0.08
customer1_subtotal = item1_price + item2_price + item3_price
customer1_tax = customer1_subtotal * tax_rate
customer1_total = customer1_subtotal + customer1_tax

# Calculating total price for customer 2 - repeating same logic
item1_price_c2 = 45.00
item2_price_c2 = 12.99
tax_rate_c2 = 0.08
customer2_subtotal = item1_price_c2 + item2_price_c2
customer2_tax = customer2_subtotal * tax_rate_c2
customer2_total = customer2_subtotal + customer2_tax

# Calculating total price for customer 3 - repeating again
item1_price_c3 = 33.25
item2_price_c3 = 7.50
item3_price_c3 = 22.00
item4_price_c3 = 5.99
tax_rate_c3 = 0.08
customer3_subtotal = item1_price_c3 + item2_price_c3 + item3_price_c3 + item4_price_c3
customer3_tax = customer3_subtotal * tax_rate_c3
customer3_total = customer3_subtotal + customer3_tax


# With functions - reusable solution
def calculate_total_with_tax(prices, tax_rate=0.08):
    """
    Calculate total price including tax for a list of item prices

    Real-world analogy: Like a cashier's standard procedure
    - Take all item prices
    - Add them up (subtotal)
    - Calculate tax
    - Give final total

    Input: list of prices, tax rate (default 8%)
    Output: final total including tax
    """
    subtotal = sum(prices)  # Add all prices
    tax = subtotal * tax_rate  # Calculate tax
    total = subtotal + tax  # Final total
    return total


# Now calculating totals is simple and consistent
customer1_total = calculate_total_with_tax([25.99, 15.50, 8.75])
customer2_total = calculate_total_with_tax([45.00, 12.99])
customer3_total = calculate_total_with_tax([33.25, 7.50, 22.00, 5.99])

# ===== PROBLEM 2: COMPLEX OPERATIONS BECOME MANAGEABLE =====

# Real-world analogy: Functions are like specialized workers in a factory
# Instead of one person doing everything, you have specialists

# Without functions - one massive, confusing process
# Imagine processing a customer order without breaking it down
customer_name = "Alice Johnson"
customer_email = "alice@email.com"
items_ordered = ["laptop", "mouse", "keyboard"]
item_prices = [999.99, 25.99, 79.99]

# Everything mixed together in one place - hard to follow
# Validate email
if "@" in customer_email and "." in customer_email:
    email_valid = True
else:
    email_valid = False

# Calculate total
order_subtotal = 0
for price in item_prices:
    order_subtotal += price
order_tax = order_subtotal * 0.08
order_total = order_subtotal + order_tax

# Check inventory
laptop_stock = 5
mouse_stock = 20
keyboard_stock = 15
all_in_stock = laptop_stock > 0 and mouse_stock > 0 and keyboard_stock > 0

# Generate confirmation
if email_valid and all_in_stock:
    order_status = f"Order confirmed for {customer_name}. Total: ${order_total:.2f}"
else:
    order_status = "Order failed - check email or inventory"


# With functions - each specialist does their job
def validate_email(email):
    """
    Email validation specialist
    Like having a receptionist who checks if contact info is correct
    """
    return "@" in email and "." in email


def calculate_order_total(prices, tax_rate=0.08):
    """
    Accounting specialist
    Like having an accountant who handles all money calculations
    """
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    return subtotal + tax


def check_inventory(items, stock_levels):
    """
    Inventory specialist
    Like having a warehouse manager who knows what's available
    """
    item_stock_map = {
        "laptop": stock_levels.get("laptop", 0),
        "mouse": stock_levels.get("mouse", 0),
        "keyboard": stock_levels.get("keyboard", 0),
    }

    for item in items:
        if item_stock_map.get(item, 0) <= 0:
            return False
    return True


def process_order(customer_name, customer_email, items, prices):
    """
    Order processing manager
    Like a supervisor who coordinates all specialists
    """
    # Use specialists for their expertise
    if not validate_email(customer_email):
        return f"Invalid email for {customer_name}"

    total = calculate_order_total(prices)

    stock_levels = {"laptop": 5, "mouse": 20, "keyboard": 15}
    if not check_inventory(items, stock_levels):
        return f"Items out of stock for {customer_name}"

    return f"Order confirmed for {customer_name}. Total: ${total:.2f}"


# Now processing orders is clear and organized
order_result = process_order(
    "Alice Johnson",
    "alice@email.com",
    ["laptop", "mouse", "keyboard"],
    [999.99, 25.99, 79.99],
)

# ===== PROBLEM 3: DEBUGGING AND MAINTENANCE =====

# Real-world analogy: Functions are like car parts
# When your car breaks, you don't replace the whole car
# You identify the broken part and fix just that part


# Without functions - when something breaks, hard to find and fix
# Imagine a bug in this massive code block
def process_everything():
    # Validation mixed with calculation mixed with formatting
    user_input = "25.5, 30.2, invalid, 15.7"
    numbers = []
    for item in user_input.split(", "):
        try:
            num = float(item)
            if num > 0:
                numbers.append(num)
        except:
            pass  # Skip invalid numbers

    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1

    if count > 0:
        average = total / count
        result = f"Total: {total}, Average: {average:.2f}, Count: {count}"
    else:
        result = "No valid numbers found"

    # If there's a bug anywhere in here, it's hard to isolate
    return result


# With functions - each part can be tested and fixed independently
def clean_and_validate_numbers(input_string):
    """
    Input cleaning specialist
    Like a quality control inspector who removes defective items
    """
    numbers = []
    for item in input_string.split(", "):
        try:
            num = float(item)
            if num > 0:  # Only positive numbers
                numbers.append(num)
        except ValueError:
            continue  # Skip invalid entries
    return numbers


def calculate_statistics(numbers):
    """
    Statistics calculator specialist
    Like a data analyst who processes clean numbers
    """
    if not numbers:  # Handle empty list
        return {"total": 0, "average": 0, "count": 0}

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return {"total": total, "average": average, "count": count}


def format_results(stats):
    """
    Report formatting specialist
    Like a secretary who presents information clearly
    """
    if stats["count"] == 0:
        return "No valid numbers found"

    return f"Total: {stats['total']}, Average: {stats['average']:.2f}, Count: {stats['count']}"


def process_number_data(input_string):
    """
    Project manager who coordinates all specialists
    """
    # Step 1: Clean the data
    clean_numbers = clean_and_validate_numbers(input_string)

    # Step 2: Calculate statistics
    stats = calculate_statistics(clean_numbers)

    # Step 3: Format results
    result = format_results(stats)

    return result


# Now if there's a bug, you know exactly where to look:
# - Validation issues? Check clean_and_validate_numbers()
# - Math problems? Check calculate_statistics()
# - Display issues? Check format_results()

test_data = "25.5, 30.2, invalid, 15.7"
result = process_number_data(test_data)

# ===== PROBLEM 4: TESTING AND RELIABILITY =====

# Real-world analogy: Functions are like appliance testing
# You can test each appliance (function) individually before using them together


# Without functions - testing is difficult
# How do you test just the email validation part of this complex code?
def complex_user_registration(name, email, age, password):
    # Email validation mixed with other logic
    if len(name) < 2 or not name.replace(" ", "").isalpha():
        return "Invalid name"
    if "@" not in email or "." not in email or len(email) < 5:
        return "Invalid email"
    if age < 18 or age > 120:
        return "Invalid age"
    if len(password) < 8 or not any(c.isdigit() for c in password):
        return "Weak password"
    return "Registration successful"


# With functions - each function can be tested independently
def validate_name(name):
    """
    Name validator - like a bouncer checking IDs
    Can be tested with various inputs to ensure it works correctly
    """
    if len(name) < 2:
        return False, "Name too short"
    if not name.replace(" ", "").isalpha():
        return False, "Name contains invalid characters"
    return True, "Valid name"


def validate_email(email):
    """
    Email validator - like a postal worker checking addresses
    Easy to test with good and bad email examples
    """
    if "@" not in email:
        return False, "Missing @ symbol"
    if "." not in email:
        return False, "Missing domain extension"
    if len(email) < 5:
        return False, "Email too short"
    return True, "Valid email"


def validate_age(age):
    """
    Age validator - like an age verification system
    Can be tested with edge cases easily
    """
    if age < 18:
        return False, "Must be 18 or older"
    if age > 120:
        return False, "Age seems unrealistic"
    return True, "Valid age"


def validate_password(password):
    """
    Password validator - like a security guard checking credentials
    Easy to test password strength rules individually
    """
    if len(password) < 8:
        return False, "Password too short"
    if not any(c.isdigit() for c in password):
        return False, "Password needs at least one number"
    return True, "Strong password"


def register_user(name, email, age, password):
    """
    Registration coordinator - uses all validators
    """
    # Test each validation independently
    name_valid, name_msg = validate_name(name)
    if not name_valid:
        return name_msg

    email_valid, email_msg = validate_email(email)
    if not email_valid:
        return email_msg

    age_valid, age_msg = validate_age(age)
    if not age_valid:
        return age_msg

    password_valid, password_msg = validate_password(password)
    if not password_valid:
        return password_msg

    return "Registration successful"


# Now you can test each part individually
# Test name validation
test_names = ["John", "A", "John123", "Mary Jane"]
for name in test_names:
    valid, message = validate_name(name)
    # Each test is focused and clear

# ===== PROBLEM 5: REUSABILITY ACROSS PROJECTS =====

# Real-world analogy: Functions are like tools in a toolbox
# A hammer is useful in many different projects
# You don't need to reinvent the hammer each time


# Utility functions that can be used in multiple projects
def format_currency(amount, currency_symbol="$"):
    """
    Currency formatter - like a standardized price tag maker
    Useful in e-commerce, accounting, invoicing, etc.
    """
    return f"{currency_symbol}{amount:.2f}"


def calculate_percentage(part, whole):
    """
    Percentage calculator - like a universal ratio finder
    Useful in statistics, grades, discounts, progress bars, etc.
    """
    if whole == 0:
        return 0
    return (part / whole) * 100


def is_business_day(day_of_week):
    """
    Business day checker - like a calendar consultant
    Useful in scheduling, payroll, delivery systems, etc.
    """
    # Monday = 0, Sunday = 6
    return 0 <= day_of_week <= 4


def generate_confirmation_code(length=6):
    """
    Confirmation code generator - like a ticket number maker
    Useful in orders, bookings, transactions, etc.
    """
    import random
    import string

    characters = string.ascii_uppercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))


# These functions can be used in different contexts:

# E-commerce application
product_price = 29.99
formatted_price = format_currency(product_price)
discount_percent = calculate_percentage(5, product_price)

# Educational application
correct_answers = 18
total_questions = 20
grade_percentage = calculate_percentage(correct_answers, total_questions)

# Scheduling application
import datetime

today = datetime.datetime.now().weekday()
can_schedule_meeting = is_business_day(today)

# Booking system
booking_code = generate_confirmation_code(8)

# ===== REAL-WORLD ANALOGIES SUMMARY =====

# Functions are like:

# 1. RECIPES IN COOKING
#    - Reusable instructions
#    - Consistent results
#    - Easy to share and modify

# 2. TOOLS IN A TOOLBOX
#    - Each tool has a specific purpose
#    - Tools can be used in many projects
#    - Quality tools last a long time

# 3. SPECIALISTS IN A COMPANY
#    - Each person has expertise in one area
#    - Teams work together efficiently
#    - Easy to replace or train one specialist

# 4. ASSEMBLY LINE IN MANUFACTURING
#    - Each station does one specific task
#    - Products move smoothly through the process
#    - Easy to optimize individual stations

# 5. APPLIANCES IN A KITCHEN
#    - Each appliance has a specific function
#    - Can be tested individually
#    - When one breaks, you fix just that one

# ===== THE MAIN BENEFITS OF FUNCTIONS =====

"""
WHY FUNCTIONS ARE ESSENTIAL:

1. REUSABILITY
   - Write once, use many times
   - Like having a Swiss Army knife instead of buying separate tools

2. ORGANIZATION
   - Break complex problems into simple parts
   - Like organizing a messy room into labeled containers

3. DEBUGGING
   - Isolate problems to specific functions
   - Like having separate fuses for different parts of your house

4. TESTING
   - Test each function independently
   - Like quality-checking each ingredient before cooking

5. COLLABORATION
   - Multiple people can work on different functions
   - Like different specialists working on the same project

6. MAINTENANCE
   - Update one function to fix issues everywhere it's used
   - Like updating a recipe that everyone follows

7. READABILITY
   - Code becomes self-documenting with good function names
   - Like having clear labels on everything in your workshop

8. SCALABILITY
   - Easy to add new features by combining existing functions
   - Like building with LEGO blocks - endless possibilities
"""

# ===== CONCLUSION =====

# Functions are not just a programming concept - they're a way of thinking
# about breaking down complex problems into manageable, reusable parts.

# Just like in real life:
# - We don't reinvent the wheel every time we need transportation
# - We don't write out the alphabet every time we want to write a word
# - We don't explain how to make bread every time we make a sandwich

# Functions let us build on previous work and create more sophisticated
# programs without getting overwhelmed by complexity.

# The key is to think of functions as building blocks that can be
# combined in different ways to solve different problems.


# Example of building blocks in action:
def main_program():
    """
    Main program that coordinates everything
    Like a conductor leading an orchestra
    """
    # Get user data
    user_name = "Alice"
    user_email = "alice@example.com"
    user_age = 25
    user_password = "mypassword123"

    # Process registration using our building blocks
    registration_result = register_user(user_name, user_email, user_age, user_password)

    # Calculate some prices using our building blocks
    item_prices = [25.99, 15.50, 8.75]
    total_cost = calculate_total_with_tax(item_prices)
    formatted_cost = format_currency(total_cost)

    # Generate confirmation using our building blocks
    confirmation = generate_confirmation_code()

    # Each function is a reliable building block that we can trust
    return {
        "registration": registration_result,
        "total_cost": formatted_cost,
        "confirmation": confirmation,
    }


# Run the program
if __name__ == "__main__":
    result = main_program()
    # This main program is clean and easy to understand because
    # all the complex logic is organized into well-named functions
