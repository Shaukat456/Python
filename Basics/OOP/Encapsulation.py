# **Encapsulation in Python (With Real-World Examples & Analogies)**

# ## **What is Encapsulation?**
# **Encapsulation** is the concept of **restricting direct access** to an object's data and only allowing controlled interaction through **methods**.
# It helps in **data protection** and **hiding implementation details** while exposing only what is necessary.

# ✅ **Key Features:**
# - **Hides the internal details** of an object (data hiding).
# - **Protects data** from accidental modification.
# - **Allows controlled access** using **getter and setter methods**.
# - **Improves code maintainability** and security.

# ---

# ## **Real-World Analogy: ATM Machine 🏦**
# Imagine an **ATM machine**:
# 1. You insert a card and enter your PIN.
# 2. You can withdraw money, check your balance, or deposit cash.
# 3. But you **can't directly access** the bank's database to change your balance.

# ✅ **Encapsulation in Action:**
# - The **bank’s internal system** is **hidden** from you (**data hiding**).
# - You can only **interact through buttons on the screen** (**controlled access**).
# - The ATM ensures that **only authorized users** access their accounts (**security**).

# Similarly, in Python, **encapsulation** ensures that data is **hidden and protected**, and access is **controlled using methods**.

# ---

# ## **Encapsulation in Python**
# Encapsulation is implemented using **private (`__`) and protected (`_`) attributes**.

# ### **1️⃣ Public, Private, and Protected Attributes**
# | **Access Modifier** | **Syntax** | **Access Level** |
# |--------------------|-----------|----------------|
# | **Public**   | `self.name`  | Can be accessed from anywhere |
# | **Protected** | `self._name` | Can be accessed, but considered for internal use |
# | **Private**   | `self.__name` | Cannot be accessed directly outside the class |

# ---


# ### **2️⃣ Public Attributes (Accessible from Anywhere)**
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute


car = Car("Toyota", "Corolla")
print(car.brand)  # ✅ Allowed
print(car.model)  # ✅ Allowed

# **🔹 Problem:** Public attributes **can be modified directly**, which is **not safe** in some cases.

# ---


# ### **3️⃣ Private Attributes (`__`) (Encapsulation in Action)**
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (Encapsulation)

    def get_balance(self):  # Getter method
        return self.__balance

    def deposit(self, amount):  # Setter method
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount!")


account = BankAccount(5000)
print(account.get_balance())  # ✅ Allowed via method
account.deposit(1000)  # ✅ Allowed via method
print(account.__balance)  # ❌ AttributeError: Cannot access private attribute

# ### **🔹 Key Takeaways**
# - `self.__balance` **cannot be accessed directly** from outside the class.
# - It can only be accessed **via methods like `get_balance()` and `deposit()`**.
# - This **prevents accidental modification** of critical data.

# ---


# ### **4️⃣ Protected Attributes (`_`)**
# Protected attributes **are not strictly private** but should be **treated as private** by convention.
class Laptop:
    def __init__(self, brand, price):
        self._brand = brand  # Protected attribute
        self._price = price  # Protected attribute


laptop = Laptop("Dell", 1000)
print(laptop._price)  # ⚠️ Technically accessible, but should be avoided

# 🔹 **By convention**, attributes with `_` should be **treated as private** but are still accessible.

# ---

# ## **5️⃣ Using Getters and Setters for Controlled Access**
# Encapsulation **prevents direct modification** of sensitive data.
# We use **getter and setter methods** to access or modify private attributes safely.


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # Getter method
    def get_salary(self):
        return self.__salary

    # Setter method
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")


employee = Employee("Alice", 50000)
print(employee.get_salary())  # ✅ Allowed via getter
employee.set_salary(60000)  # ✅ Allowed via setter
print(employee.get_salary())  # ✅ Updated salary

# ### **🔹 Why Use Getters and Setters?**
# - Prevents **unauthorized access** to sensitive data.
# - Ensures **data validation** before modification.
# - Improves **code maintainability** and security.

# ---

# ## **6️⃣ Encapsulation in Inheritance**
# Even in **child classes**, private attributes (`__`) **are not accessible** directly.


class Parent:
    def __init__(self):
        self.__secret = "Hidden data"


class Child(Parent):
    def show_secret(self):
        return self.__secret  # ❌ AttributeError


# child = Child()
# print(child.show_secret())  # ❌ Will raise an error

# 🔹 **Solution:** Use **getter methods** to access private attributes.

# ---

# ## **7️⃣ Encapsulation in Real-World Use Cases**
# ✅ **1. Data Protection in Banking Apps**
# Encapsulation **hides sensitive user data** and **prevents unauthorized access**.


class Bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private data
        self.__balance = balance  # Private data

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount!")


# Creating a bank account
account = Bank("12345", 10000)
print(account.get_balance())  # ✅ Allowed via method
# print(account.__balance)      # ❌ Cannot access private data directly

# ✅ **2. Preventing Direct Modification of Data**
# Encapsulation ensures that important attributes **cannot be changed accidentally**.


class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade


student = Student("John", "A")
print(student.get_grade())  # ✅ Allowed via method
# student.__grade = "F"       # ❌ This will NOT modify the real grade
print(student.get_grade())  # ✅ Still "A"

# 🔹 **Even if we try to modify `__grade`, encapsulation prevents it!**

# ---

# ## **Encapsulation vs Abstraction**
# | Feature | Encapsulation | Abstraction |
# |---------|--------------|-------------|
# | **Definition** | Hiding data and restricting direct access | Hiding implementation details and showing only essential features |
# | **Focus** | **Protecting data** | **Hiding complexity** |
# | **Implementation** | **Private (`__`) and protected (`_`) attributes, getters, and setters** | **Abstract classes and methods (`ABC` module)** |
# | **Example** | ATM hides **bank database details** but allows balance check | Car **hides internal engine mechanism** but provides a **steering wheel** |

# ---

# ## **Summary**
# ✅ **Encapsulation is a fundamental OOP concept that protects data and provides controlled access.**
# ✅ It is implemented using **private (`__`) and protected (`_`) attributes**.
# ✅ Getters and setters **help manage access to private data safely**.
# ✅ Encapsulation is **useful in banking apps, security systems, and sensitive data handling**.
