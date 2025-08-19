## **Inheritance in Python (With Real-World Analogies & Use Cases)**

### **What is Inheritance?**
# Inheritance allows a class (child) to inherit properties and behaviors from another class (parent). This promotes **code reusability** and follows the **DRY (Don't Repeat Yourself)** principle.

# ---

# ## **Real-World Analogy**
# Think of **inheritance** like a **family tree**:
# - A child inherits traits (eye color, height) and behaviors (habits) from their parents.
# - The child can **use** these traits as they are or **modify them** as they grow.
# - Similarly, in Python, a child class inherits attributes and methods from a parent class but can also override them if needed.

# ### **Example: Vehicle Inheritance**
# Imagine a **"Vehicle"** is the parent class. All vehicles share common features like wheels, engines, and speed. However, different types of vehicles (cars, bikes, trucks) have specialized behaviors.


# super()# The `super()` function allows a child class to call methods from its parent class, enabling the reuse of code and properties.
# This is like a child using their parent's knowledge to build upon it.


#### **Python Code Example**
# Parent class (Base class)
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"The {self.brand} is moving at {self.speed} km/h.")


# Child class (Derived class) - inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)  # Inheriting properties from Vehicle
        self.fuel_type = fuel_type

    def honk(self):
        print("Car honks: Beep Beep!")


# Child class (Derived class) - inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, speed, helmet_required):
        super().__init__(brand, speed)
        self.helmet_required = helmet_required

    def wheelie(self):
        print("Bike performs a wheelie!")


# Creating objects
car = Car("Toyota", 120, "Petrol")
bike = Bike("Yamaha", 80, True)

car.move()  # Inherited from Vehicle
car.honk()  # Specific to Car

bike.move()  # Inherited from Vehicle
bike.wheelie()  # Specific to Bike

### **Output:**
# The Toyota is moving at 120 km/h.
# Car honks: Beep Beep!
# The Yamaha is moving at 80 km/h.
# Bike performs a wheelie!
# ```

# ---

# ## **Types of Inheritance in Python**
# ### 1️⃣ **Single Inheritance**
# One class inherits from another. *(e.g., Car inherits from Vehicle)*


# ### 2️⃣ **Multiple Inheritance**
# A class inherits from multiple parent classes. *(e.g., A FlyingCar inherits from both Car and Airplane classes)*
class Airplane:
    def fly(self):
        print("Airplane is flying!")


class FlyingCar(Car, Airplane):  # Multiple inheritance
    def transform(self):
        print("FlyingCar transforming!")


flying_car = FlyingCar("Tesla", 150, "Electric")
flying_car.move()  # Inherited from Vehicle
flying_car.fly()  # Inherited from Airplane
flying_car.transform()  # Specific to FlyingCar


### 3️⃣ **Multilevel Inheritance**
# A class inherits from another child class. *(e.g., ElectricCar → Car → Vehicle)*
class ElectricCar(Car):  # Inherits from Car, which inherits from Vehicle
    def charge(self):
        print("Electric car is charging!")


### 4️⃣ **Hierarchical Inheritance**
# Multiple child classes inherit from the same parent class. *(e.g., Car and Bike both inherit from Vehicle)*

### 5️⃣ **Hybrid Inheritance**
# A combination of multiple types of inheritance.


## **Use Cases of Inheritance in Development**


## **Conclusion**
# Inheritance helps keep your code **organized, reusable, and scalable**. Just like how humans inherit traits from parents but develop their own unique characteristics, Python classes can inherit and extend functionalities! 🚀
