# nestedLoop.py
# Real-World Nested Loop Examples and Use Cases

"""
COMPREHENSIVE GUIDE: NESTED LOOPS IN PYTHON

This file covers:
1. Understanding Nested Loop Concept
2. Real-World Use Cases and Examples
3. Working with Lists (2D arrays, matrices)
4. Dictionary Iterations and Processing
5. Tuple Operations and Combinations
6. Performance Considerations
7. Best Practices and Optimization
8. Common Patterns and Applications
"""

# ============================================================================
# UNDERSTANDING NESTED LOOPS
# ============================================================================

# What are nested loops?
# Nested loops are loops inside other loops - like Russian nesting dolls!
# The inner loop completes ALL its iterations for EACH iteration of the outer loop

# Basic structure:
# for outer_item in outer_collection:
#     for inner_item in inner_collection:
#         # Process combination of outer_item and inner_item

print("🔄 NESTED LOOPS: REAL-WORLD EXAMPLES AND USE CASES")
print("=" * 60)

# ============================================================================
# SECTION 1: BASIC NESTED LOOP CONCEPTS WITH SIMPLE EXAMPLES
# ============================================================================

print("\n📚 SECTION 1: BASIC CONCEPTS")
print("-" * 40)

# Example 1: Multiplication Table (Classic Example)
print("🧮 MULTIPLICATION TABLE:")
print("Like learning times tables in school!")


def create_multiplication_table(size=5):
    """Create multiplication table - classic nested loop example"""
    print(f"\nMultiplication Table ({size}x{size}):")
    print("   ", end="")

    # Header row
    for j in range(1, size + 1):
        print(f"{j:4}", end="")
    print()

    # Table rows
    for i in range(1, size + 1):
        print(f"{i:2} ", end="")
        for j in range(1, size + 1):
            print(f"{i*j:4}", end="")
        print()


create_multiplication_table(5)

# Example 2: Pattern Printing
print("\n⭐ STAR PATTERNS:")
print("Like drawing patterns on paper!")


def print_triangle_pattern(height=5):
    """Print triangle pattern using nested loops"""
    print(f"\nTriangle Pattern (height={height}):")
    for row in range(1, height + 1):
        # Print spaces for alignment
        for space in range(height - row):
            print(" ", end="")
        # Print stars
        for star in range(2 * row - 1):
            print("*", end="")
        print()


print_triangle_pattern(5)


def print_rectangle_pattern(width=6, height=4):
    """Print rectangle pattern"""
    print(f"\nRectangle Pattern ({width}x{height}):")
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


print_rectangle_pattern(8, 5)

# ============================================================================
# SECTION 2: REAL-WORLD USE CASES WITH LISTS
# ============================================================================

print("\n📊 SECTION 2: REAL-WORLD EXAMPLES WITH LISTS")
print("-" * 50)

# Example 1: Student Grade Management System
print("🎓 STUDENT GRADE MANAGEMENT:")
print("Like a teacher's gradebook!")

# 2D list representing students and their grades
students_grades = [
    ["Alice", 85, 92, 78, 88],  # Student name + 4 test scores
    ["Bob", 79, 85, 91, 87],
    ["Charlie", 92, 88, 85, 90],
    ["Diana", 88, 94, 87, 92],
    ["Eve", 76, 82, 89, 85],
]


def analyze_student_grades(grades_data):
    """Analyze student performance using nested loops"""
    print("\n📈 Grade Analysis Report:")
    print("Student      Test1  Test2  Test3  Test4  Average  Grade")
    print("-" * 60)

    class_totals = [0, 0, 0, 0]  # Track totals for each test

    for student_data in grades_data:
        name = student_data[0]
        scores = student_data[1:]

        # Calculate student average
        student_avg = sum(scores) / len(scores)

        # Add to class totals
        for i, score in enumerate(scores):
            class_totals[i] += score

        # Determine letter grade
        if student_avg >= 90:
            letter_grade = "A"
        elif student_avg >= 80:
            letter_grade = "B"
        elif student_avg >= 70:
            letter_grade = "C"
        else:
            letter_grade = "D"

        # Print student report
        print(f"{name:<12}", end="")
        for score in scores:
            print(f"{score:6}", end="")
        print(f" {student_avg:7.1f}    {letter_grade}")

    print("-" * 60)
    print("Class Avg   ", end="")
    for total in class_totals:
        avg = total / len(grades_data)
        print(f"{avg:6.1f}", end="")
    print()


analyze_student_grades(students_grades)

# Example 2: Shopping Cart System
print("\n🛒 SHOPPING CART SYSTEM:")
print("Like organizing items in different categories!")

shopping_cart = [
    ["Electronics", [("Laptop", 999.99), ("Mouse", 25.99), ("Keyboard", 79.99)]],
    ["Books", [("Python Guide", 39.99), ("Data Science", 59.99), ("AI Basics", 44.99)]],
    ["Clothing", [("T-Shirt", 19.99), ("Jeans", 69.99), ("Sneakers", 89.99)]],
]


def process_shopping_cart(cart):
    """Process shopping cart with nested categories"""
    print("\n🧾 Shopping Cart Summary:")
    print("=" * 50)

    grand_total = 0

    for category_data in cart:
        category_name = category_data[0]
        items = category_data[1]

        print(f"\n📦 {category_name}:")
        print("-" * 30)
        category_total = 0

        for item_name, price in items:
            print(f"  {item_name:<20} ${price:7.2f}")
            category_total += price

        print(f"  {'Category Total:':<20} ${category_total:7.2f}")
        grand_total += category_total

    print("=" * 50)
    print(f"🏆 Grand Total: ${grand_total:.2f}")

    # Calculate tax (8.5%)
    tax = grand_total * 0.085
    final_total = grand_total + tax
    print(f"💰 Tax (8.5%): ${tax:.2f}")
    print(f"🎯 Final Total: ${final_total:.2f}")


process_shopping_cart(shopping_cart)

# Example 3: Matrix Operations
print("\n🔢 MATRIX OPERATIONS:")
print("Like working with spreadsheet data!")

# Matrix represented as list of lists
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


def add_matrices(matrix1, matrix2):
    """Add two matrices using nested loops"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have same dimensions"

    result = []
    rows = len(matrix1)
    cols = len(matrix1[0])

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def print_matrix(matrix, title="Matrix"):
    """Print matrix in formatted way"""
    print(f"\n{title}:")
    for row in matrix:
        print("  ", end="")
        for element in row:
            print(f"{element:4}", end="")
        print()


print_matrix(matrix_a, "Matrix A")
print_matrix(matrix_b, "Matrix B")

result_matrix = add_matrices(matrix_a, matrix_b)
print_matrix(result_matrix, "A + B")

# Example 4: Seating Arrangement System
print("\n🎭 THEATER SEATING SYSTEM:")
print("Like booking seats in a movie theater!")

# Theater seating: 0 = available, 1 = booked
theater_seats = [
    [0, 1, 1, 0, 0, 1, 0, 0],  # Row A
    [1, 1, 0, 0, 1, 1, 1, 0],  # Row B
    [0, 0, 0, 1, 1, 0, 0, 0],  # Row C
    [1, 0, 1, 0, 0, 0, 1, 1],  # Row D
    [0, 0, 0, 0, 0, 0, 0, 0],  # Row E
]


def display_theater_seating(seats):
    """Display theater seating chart"""
    print("\n🎪 Theater Seating Chart:")
    print("   1 2 3 4 5 6 7 8")
    print("  ┌─────────────────┐")

    row_letters = ["A", "B", "C", "D", "E"]

    for i, row in enumerate(seats):
        print(f"{row_letters[i]} │", end="")
        for seat in row:
            if seat == 0:
                print(" ○", end="")  # Available
            else:
                print(" ●", end="")  # Booked
        print(" │")

    print("  └─────────────────┘")
    print("  ○ = Available  ● = Booked")


def find_available_seats(seats, group_size=2):
    """Find available seats for a group"""
    print(f"\n🔍 Finding {group_size} consecutive seats:")

    row_letters = ["A", "B", "C", "D", "E"]
    found_seats = []

    for row_idx, row in enumerate(seats):
        consecutive_count = 0
        start_seat = 0

        for seat_idx, seat in enumerate(row):
            if seat == 0:  # Available
                if consecutive_count == 0:
                    start_seat = seat_idx
                consecutive_count += 1

                if consecutive_count >= group_size:
                    seat_range = f"{row_letters[row_idx]}{start_seat+1}-{row_letters[row_idx]}{start_seat+group_size}"
                    found_seats.append(seat_range)
                    break
            else:
                consecutive_count = 0

    if found_seats:
        print("✅ Available seat groups:")
        for seats_group in found_seats:
            print(f"   {seats_group}")
    else:
        print("❌ No consecutive seats available for group size")


display_theater_seating(theater_seats)
find_available_seats(theater_seats, 3)

# ============================================================================
# SECTION 3: DICTIONARY ITERATIONS AND PROCESSING
# ============================================================================

print("\n📖 SECTION 3: NESTED LOOPS WITH DICTIONARIES")
print("-" * 50)

# Example 1: Employee Management System
print("👥 EMPLOYEE MANAGEMENT SYSTEM:")
print("Like HR department managing employee data!")

company_data = {
    "Engineering": {
        "employees": [
            {
                "name": "Alice",
                "salary": 85000,
                "experience": 3,
                "skills": ["Python", "Java", "SQL"],
            },
            {
                "name": "Bob",
                "salary": 95000,
                "experience": 5,
                "skills": ["JavaScript", "React", "Node.js"],
            },
            {
                "name": "Charlie",
                "salary": 75000,
                "experience": 2,
                "skills": ["Python", "Django", "PostgreSQL"],
            },
        ],
        "budget": 300000,
    },
    "Marketing": {
        "employees": [
            {
                "name": "Diana",
                "salary": 65000,
                "experience": 4,
                "skills": ["SEO", "Content", "Analytics"],
            },
            {
                "name": "Eve",
                "salary": 70000,
                "experience": 6,
                "skills": ["PPC", "Social Media", "Design"],
            },
        ],
        "budget": 150000,
    },
    "Sales": {
        "employees": [
            {
                "name": "Frank",
                "salary": 60000,
                "experience": 3,
                "skills": ["CRM", "Negotiation", "B2B"],
            },
            {
                "name": "Grace",
                "salary": 68000,
                "experience": 4,
                "skills": ["Lead Gen", "Closing", "Customer Relations"],
            },
        ],
        "budget": 140000,
    },
}


def analyze_company_data(data):
    """Analyze company data using nested dictionary iteration"""
    print("\n📊 Company Analysis Report:")
    print("=" * 60)

    total_employees = 0
    total_salary_cost = 0
    skill_count = {}

    for department, dept_data in data.items():
        print(f"\n🏢 {department} Department:")
        print("-" * 40)

        employees = dept_data["employees"]
        budget = dept_data["budget"]
        dept_salary_cost = 0

        print(f"Budget: ${budget:,}")
        print("Employees:")

        for employee in employees:
            name = employee["name"]
            salary = employee["salary"]
            experience = employee["experience"]
            skills = employee["skills"]

            print(
                f"  👤 {name:<10} | Salary: ${salary:,} | Exp: {experience}y | Skills: {', '.join(skills)}"
            )

            dept_salary_cost += salary
            total_salary_cost += salary
            total_employees += 1

            # Count skills across company
            for skill in skills:
                skill_count[skill] = skill_count.get(skill, 0) + 1

        remaining_budget = budget - dept_salary_cost
        print(f"Salary Cost: ${dept_salary_cost:,}")
        print(f"Remaining Budget: ${remaining_budget:,}")

        if remaining_budget < 0:
            print("⚠️  OVER BUDGET!")

    print("\n🎯 Company Summary:")
    print("=" * 40)
    print(f"Total Employees: {total_employees}")
    print(f"Total Salary Cost: ${total_salary_cost:,}")

    print("\n🛠️ Skills Distribution:")
    for skill, count in sorted(skill_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  {skill}: {count} employees")


analyze_company_data(company_data)

# Example 2: Restaurant Menu and Orders
print("\n🍽️ RESTAURANT ORDER SYSTEM:")
print("Like managing orders in a restaurant!")

restaurant_menu = {
    "Appetizers": {
        "Spring Rolls": {
            "price": 8.99,
            "ingredients": ["vegetables", "wrapper", "oil"],
            "vegetarian": True,
        },
        "Chicken Wings": {
            "price": 12.99,
            "ingredients": ["chicken", "sauce", "celery"],
            "vegetarian": False,
        },
        "Garlic Bread": {
            "price": 6.99,
            "ingredients": ["bread", "garlic", "butter"],
            "vegetarian": True,
        },
    },
    "Main Courses": {
        "Grilled Salmon": {
            "price": 24.99,
            "ingredients": ["salmon", "lemon", "herbs"],
            "vegetarian": False,
        },
        "Vegetable Curry": {
            "price": 16.99,
            "ingredients": ["vegetables", "coconut milk", "spices"],
            "vegetarian": True,
        },
        "Beef Steak": {
            "price": 28.99,
            "ingredients": ["beef", "pepper", "garlic"],
            "vegetarian": False,
        },
    },
    "Desserts": {
        "Chocolate Cake": {
            "price": 7.99,
            "ingredients": ["chocolate", "flour", "eggs"],
            "vegetarian": True,
        },
        "Ice Cream": {
            "price": 4.99,
            "ingredients": ["milk", "sugar", "vanilla"],
            "vegetarian": True,
        },
    },
}

# Customer orders
customer_orders = [
    {"customer": "Table 1", "items": ["Spring Rolls", "Grilled Salmon", "Ice Cream"]},
    {"customer": "Table 2", "items": ["Chicken Wings", "Beef Steak", "Chocolate Cake"]},
    {"customer": "Table 3", "items": ["Garlic Bread", "Vegetable Curry"]},
]


def process_restaurant_orders(menu, orders):
    """Process restaurant orders using nested dictionary loops"""
    print("\n🧾 Restaurant Order Processing:")
    print("=" * 50)

    total_revenue = 0
    ingredient_usage = {}

    for order in orders:
        customer = order["customer"]
        items = order["items"]

        print(f"\n👥 {customer}:")
        print("-" * 25)
        order_total = 0
        order_vegetarian = True

        for item_name in items:
            # Find item in menu
            found = False
            for category, category_items in menu.items():
                if item_name in category_items:
                    item_info = category_items[item_name]
                    price = item_info["price"]
                    ingredients = item_info["ingredients"]
                    is_veg = item_info["vegetarian"]

                    print(f"  🍽️ {item_name:<20} ${price:6.2f}")
                    order_total += price

                    if not is_veg:
                        order_vegetarian = False

                    # Track ingredient usage
                    for ingredient in ingredients:
                        ingredient_usage[ingredient] = (
                            ingredient_usage.get(ingredient, 0) + 1
                        )

                    found = True
                    break

            if not found:
                print(f"  ❌ {item_name} - Item not found!")

        print(f"  {'Order Total:':<20} ${order_total:6.2f}")
        if order_vegetarian:
            print("  🌱 Vegetarian Order")
        total_revenue += order_total

    print(f"\n💰 Total Restaurant Revenue: ${total_revenue:.2f}")

    print("\n📦 Ingredient Usage Report:")
    for ingredient, usage in sorted(
        ingredient_usage.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"  {ingredient}: {usage} times")


process_restaurant_orders(restaurant_menu, customer_orders)

# Example 3: Social Media Analytics
print("\n📱 SOCIAL MEDIA ANALYTICS:")
print("Like analyzing social media engagement!")

social_media_data = {
    "platforms": {
        "Instagram": {
            "posts": [
                {
                    "date": "2024-01-01",
                    "likes": 150,
                    "comments": 23,
                    "shares": 12,
                    "hashtags": ["#food", "#yummy"],
                },
                {
                    "date": "2024-01-02",
                    "likes": 200,
                    "comments": 35,
                    "shares": 18,
                    "hashtags": ["#travel", "#adventure"],
                },
                {
                    "date": "2024-01-03",
                    "likes": 180,
                    "comments": 28,
                    "shares": 15,
                    "hashtags": ["#food", "#recipe"],
                },
            ]
        },
        "Twitter": {
            "posts": [
                {
                    "date": "2024-01-01",
                    "likes": 85,
                    "comments": 12,
                    "shares": 25,
                    "hashtags": ["#tech", "#AI"],
                },
                {
                    "date": "2024-01-02",
                    "likes": 120,
                    "comments": 18,
                    "shares": 32,
                    "hashtags": ["#programming", "#python"],
                },
                {
                    "date": "2024-01-03",
                    "likes": 95,
                    "comments": 15,
                    "shares": 22,
                    "hashtags": ["#tech", "#innovation"],
                },
            ]
        },
        "Facebook": {
            "posts": [
                {
                    "date": "2024-01-01",
                    "likes": 75,
                    "comments": 8,
                    "shares": 5,
                    "hashtags": ["#family", "#memories"],
                },
                {
                    "date": "2024-01-02",
                    "likes": 110,
                    "comments": 14,
                    "shares": 9,
                    "hashtags": ["#business", "#success"],
                },
                {
                    "date": "2024-01-03",
                    "likes": 90,
                    "comments": 11,
                    "shares": 7,
                    "hashtags": ["#motivation", "#goals"],
                },
            ]
        },
    }
}


def analyze_social_media(data):
    """Analyze social media performance across platforms"""
    print("\n📈 Social Media Analytics Dashboard:")
    print("=" * 55)

    platform_stats = {}
    all_hashtags = {}
    total_engagement = 0

    for platform_name, platform_data in data["platforms"].items():
        print(f"\n📱 {platform_name}:")
        print("-" * 30)

        posts = platform_data["posts"]
        platform_likes = 0
        platform_comments = 0
        platform_shares = 0

        for post in posts:
            date = post["date"]
            likes = post["likes"]
            comments = post["comments"]
            shares = post["shares"]
            hashtags = post["hashtags"]

            engagement = likes + comments + shares

            print(
                f"  📅 {date}: Likes: {likes:3d} | Comments: {comments:2d} | Shares: {shares:2d} | Engagement: {engagement:3d}"
            )

            platform_likes += likes
            platform_comments += comments
            platform_shares += shares
            total_engagement += engagement

            # Count hashtags
            for hashtag in hashtags:
                all_hashtags[hashtag] = all_hashtags.get(hashtag, 0) + 1

        platform_total = platform_likes + platform_comments + platform_shares
        avg_engagement = platform_total / len(posts) if posts else 0

        platform_stats[platform_name] = {
            "total_engagement": platform_total,
            "avg_engagement": avg_engagement,
            "posts_count": len(posts),
        }

        print(f"  Total Engagement: {platform_total}")
        print(f"  Average per Post: {avg_engagement:.1f}")

    print("\n🏆 Platform Comparison:")
    print("-" * 40)
    for platform, stats in sorted(
        platform_stats.items(), key=lambda x: x[1]["total_engagement"], reverse=True
    ):
        print(
            f"  {platform:<10}: {stats['total_engagement']:3d} total | {stats['avg_engagement']:5.1f} avg | {stats['posts_count']} posts"
        )

    print("\n🏷️ Top Hashtags:")
    print("-" * 20)
    top_hashtags = sorted(all_hashtags.items(), key=lambda x: x[1], reverse=True)[:5]
    for hashtag, count in top_hashtags:
        print(f"  {hashtag:<15}: {count} uses")

    print(f"\n🎯 Total Platform Engagement: {total_engagement}")


analyze_social_media(social_media_data)

# ============================================================================
# SECTION 4: TUPLE OPERATIONS AND COMBINATIONS
# ============================================================================

print("\n📦 SECTION 4: NESTED LOOPS WITH TUPLES")
print("-" * 45)

# Example 1: Coordinate System and Distance Calculations
print("📍 COORDINATE SYSTEM:")
print("Like GPS coordinates and finding distances!")

# Cities with their coordinates (latitude, longitude)
cities = [
    ("New York", 40.7128, -74.0060),
    ("Los Angeles", 34.0522, -118.2437),
    ("Chicago", 41.8781, -87.6298),
    ("Houston", 29.7604, -95.3698),
    ("Phoenix", 33.4484, -112.0740),
]


def calculate_distance(coord1, coord2):
    """Calculate distance between two coordinates (simplified)"""
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Simplified distance calculation (not actual geographic distance)
    distance = ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5
    return distance * 69  # Rough conversion to miles


def find_city_distances(cities_list):
    """Find distances between all city pairs"""
    print("\n🗺️ City Distance Matrix:")
    print("=" * 50)

    # Print header
    print("From/To".ljust(12), end="")
    for city_name, _, _ in cities_list:
        print(f"{city_name[:8]:>10}", end="")
    print()

    for i, (city1, lat1, lon1) in enumerate(cities_list):
        print(f"{city1[:10]:10}  ", end="")

        for j, (city2, lat2, lon2) in enumerate(cities_list):
            if i == j:
                print("     -    ", end="")
            else:
                distance = calculate_distance((lat1, lon1), (lat2, lon2))
                print(f"{distance:8.0f}  ", end="")
        print()


find_city_distances(cities)

# Example 2: Product Combinations and Pricing
print("\n🛍️ PRODUCT COMBINATIONS:")
print("Like creating product bundles and pricing!")

# Product catalog with categories
product_catalog = [
    ("Laptop", "Electronics", 999.99),
    ("Mouse", "Electronics", 25.99),
    ("Keyboard", "Electronics", 79.99),
    ("Desk", "Furniture", 299.99),
    ("Chair", "Furniture", 199.99),
    ("Monitor", "Electronics", 349.99),
]


def create_product_bundles(products, max_bundle_size=3):
    """Create product bundles and calculate pricing"""
    print("\n🎁 Product Bundle Generator:")
    print("=" * 40)

    electronics = []
    furniture = []

    # Separate products by category
    for name, category, price in products:
        if category == "Electronics":
            electronics.append((name, price))
        elif category == "Furniture":
            furniture.append((name, price))

    print("📱 Electronics Bundles:")
    bundle_count = 0

    # Create electronics bundles
    for i in range(len(electronics)):
        for j in range(i + 1, len(electronics)):
            if bundle_count < 5:  # Limit output
                item1_name, item1_price = electronics[i]
                item2_name, item2_price = electronics[j]
                bundle_price = item1_price + item2_price
                discount = bundle_price * 0.1  # 10% bundle discount
                final_price = bundle_price - discount

                print(f"  Bundle {bundle_count + 1}: {item1_name} + {item2_name}")
                print(f"    Regular Price: ${bundle_price:.2f}")
                print(f"    Bundle Price:  ${final_price:.2f} (Save ${discount:.2f})")
                print()
                bundle_count += 1

    print("🪑 Cross-Category Bundles:")
    cross_bundle_count = 0

    # Create cross-category bundles
    for elec_name, elec_price in electronics:
        for furn_name, furn_price in furniture:
            if cross_bundle_count < 3:  # Limit output
                bundle_price = elec_price + furn_price
                discount = bundle_price * 0.15  # 15% cross-category discount
                final_price = bundle_price - discount

                print(
                    f"  Workspace Bundle {cross_bundle_count + 1}: {elec_name} + {furn_name}"
                )
                print(f"    Regular Price: ${bundle_price:.2f}")
                print(f"    Bundle Price:  ${final_price:.2f} (Save ${discount:.2f})")
                print()
                cross_bundle_count += 1


create_product_bundles(product_catalog)

# Example 3: Tournament Scheduling
print("\n🏆 TOURNAMENT SCHEDULING:")
print("Like organizing sports tournaments!")

# Teams participating in tournament
teams = [
    ("Warriors", "Basketball", 85),  # (name, sport, skill_level)
    ("Lakers", "Basketball", 88),
    ("Celtics", "Basketball", 82),
    ("Bulls", "Basketball", 79),
    ("Eagles", "Football", 90),
    ("Cowboys", "Football", 87),
    ("Patriots", "Football", 85),
    ("Steelers", "Football", 83),
]


def create_tournament_schedule(teams_list):
    """Create tournament matchups"""
    print("\n📅 Tournament Schedule Generator:")
    print("=" * 45)

    # Group teams by sport
    sports_teams = {}
    for team_name, sport, skill in teams_list:
        if sport not in sports_teams:
            sports_teams[sport] = []
        sports_teams[sport].append((team_name, skill))

    # Create matchups for each sport
    for sport, sport_teams in sports_teams.items():
        print(f"\n🏀 {sport} Tournament:")
        print("-" * 25)

        match_number = 1
        used_teams = set()

        # Create round-robin style matchups
        for i in range(len(sport_teams)):
            for j in range(i + 1, len(sport_teams)):
                team1_name, team1_skill = sport_teams[i]
                team2_name, team2_skill = sport_teams[j]

                # Predict match outcome based on skill levels
                if team1_skill > team2_skill:
                    favorite = team1_name
                    underdog = team2_name
                    skill_diff = team1_skill - team2_skill
                else:
                    favorite = team2_name
                    underdog = team1_name
                    skill_diff = team2_skill - team1_skill

                print(f"  Match {match_number}: {team1_name} vs {team2_name}")
                print(f"    Skills: {team1_skill} vs {team2_skill}")
                print(f"    Favorite: {favorite} (by {skill_diff} points)")
                print()
                match_number += 1

                if match_number > 6:  # Limit output
                    break
            if match_number > 6:
                break


create_tournament_schedule(teams)

# ============================================================================
# SECTION 5: PERFORMANCE CONSIDERATIONS AND OPTIMIZATION
# ============================================================================

print("\n⚡ SECTION 5: PERFORMANCE OPTIMIZATION")
print("-" * 45)

import time

# Example: Efficient vs Inefficient Nested Loop Patterns
print("🚀 PERFORMANCE COMPARISON:")


def inefficient_search(data, target):
    """Inefficient nested loop search"""
    start_time = time.time()

    found_items = []
    for outer_list in data:
        for item in outer_list:
            for char in str(item):
                if str(target) in str(item):
                    found_items.append(item)
                    break

    end_time = time.time()
    return found_items, end_time - start_time


def efficient_search(data, target):
    """More efficient search with early termination"""
    start_time = time.time()

    found_items = []
    target_str = str(target)

    for outer_list in data:
        for item in outer_list:
            if target_str in str(item):
                found_items.append(item)
                # Early termination - no need to check further

    end_time = time.time()
    return found_items, end_time - start_time


# Test data
test_data = [
    [100, 200, 300, 150, 250],
    [400, 500, 600, 450, 550],
    [700, 800, 900, 750, 850],
    [1000, 1100, 1200, 1050, 1150],
]

print("\n⏱️ Performance Test Results:")
print("Searching for numbers containing '5':")

# Test both approaches
result1, time1 = inefficient_search(test_data, "5")
result2, time2 = efficient_search(test_data, "5")

print(f"  Inefficient method: {time1:.6f} seconds")
print(f"  Efficient method:   {time2:.6f} seconds")
print(f"  Speedup: {time1/time2:.2f}x faster" if time2 > 0 else "  Results instant")

# ============================================================================
# SECTION 6: COMMON PATTERNS AND BEST PRACTICES
# ============================================================================

print("\n💡 SECTION 6: BEST PRACTICES AND PATTERNS")
print("-" * 50)

# Pattern 1: Break and Continue in Nested Loops
print("🔄 LOOP CONTROL PATTERNS:")


def find_target_in_matrix(matrix, target):
    """Demonstrate break and continue in nested loops"""
    print(f"\n🎯 Searching for {target} in matrix:")

    for row_idx, row in enumerate(matrix):
        print(f"  Checking row {row_idx}: {row}")

        for col_idx, value in enumerate(row):
            if value == target:
                print(f"  ✅ Found {target} at position ({row_idx}, {col_idx})")
                return (row_idx, col_idx)  # Early return when found
            elif value < 0:
                print(f"  ⏭️ Skipping negative value {value}")
                continue  # Skip negative values

        # Could add break condition for entire row if needed
        if all(val > target * 2 for val in row):
            print(f"  🚫 Row {row_idx} values too large, stopping search")
            break

    print(f"  ❌ {target} not found in matrix")
    return None


test_matrix = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 11, 13, 15], [10, 12, 14, 16]]

find_target_in_matrix(test_matrix, 6)

# Pattern 2: List Comprehensions vs Nested Loops
print("\n📝 LIST COMPREHENSIONS VS NESTED LOOPS:")


# Traditional nested loops
def create_multiplication_table_loops(size):
    """Create multiplication table using traditional loops"""
    result = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        result.append(row)
    return result


# List comprehension equivalent
def create_multiplication_table_comprehension(size):
    """Create multiplication table using list comprehension"""
    return [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]


print("Traditional loops result:")
traditional_result = create_multiplication_table_loops(3)
for row in traditional_result:
    print(f"  {row}")

print("\nList comprehension result:")
comprehension_result = create_multiplication_table_comprehension(3)
for row in comprehension_result:
    print(f"  {row}")

# Pattern 3: Generator Expressions for Memory Efficiency
print("\n🧠 MEMORY-EFFICIENT PATTERNS:")


def process_large_dataset_generator(rows, cols):
    """Generator for memory-efficient processing of large datasets"""
    print("Using generator - processes one item at a time:")

    # Generator expression instead of creating entire list
    data_generator = ((i, j, i * j) for i in range(rows) for j in range(cols))

    count = 0
    for row, col, product in data_generator:
        if product % 2 == 0:  # Process only even products
            print(f"  Position ({row}, {col}): {product}")
            count += 1
        if count >= 5:  # Limit output
            print("  ... (processing continues)")
            break


process_large_dataset_generator(10, 10)

# ============================================================================
# SUMMARY AND KEY TAKEAWAYS
# ============================================================================

print("\n🎓 KEY TAKEAWAYS AND BEST PRACTICES")
print("=" * 50)

print(
    """
🔑 WHEN TO USE NESTED LOOPS:
   ✅ Processing 2D data (matrices, tables, grids)
   ✅ Comparing all pairs of items
   ✅ Creating combinations or permutations
   ✅ Multi-dimensional data analysis
   ✅ Pattern generation and printing

⚡ PERFORMANCE TIPS:
   • Use early termination (break/return) when possible
   • Consider list comprehensions for simple cases
   • Use generators for large datasets
   • Avoid unnecessary nested iterations
   • Cache repeated calculations

🐍 PYTHONIC PATTERNS:
   • Prefer list comprehensions for simple transformations
   • Use enumerate() when you need indices
   • Consider itertools for complex combinations
   • Use zip() for parallel iteration
   • Break complex loops into functions

🚫 COMMON PITFALLS:
   • Modifying lists while iterating
   • Unnecessary deep nesting (>3 levels)
   • Not handling empty collections
   • Forgetting to break when target found
   • Creating unnecessary temporary lists

💡 ALTERNATIVES TO CONSIDER:
   • NumPy for numerical operations
   • Pandas for data analysis
   • itertools for combinations/permutations
   • map()/filter() for functional approach
   • Database queries for large datasets
"""
)

print("\n🎉 NESTED LOOPS MASTERY COMPLETE!")
print("Practice with real-world data to build intuition! 🚀")
