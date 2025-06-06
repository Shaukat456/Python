# Explain Classes in python with examples

# Classes are the blueprint for creating objects. They can contain methods and attributes that are associated with the object created from it.


# Example 1
class Cat:
    def __init__(self, providedname, providedage):
        self.name = providedname
        self.age = providedage
        self.height = "5'5"

    # def bark(self):
    #     print(f"{self.name} is barking")


cat1 = Cat("Tom", 5)

# Example 2
class Car:
    year = 2020

    def __init__(self, providedModel, providedAge):
        self.model = providedModel
        self.age = providedAge
        self.year = 2021

    def drive(self):
        print(f"{self.model} is driving")


car1 = Car("Toyota", 5)
cat1.year


# Example 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")


p1 = Person("John", 25)
p1.walk()
# Explain constructor in python with examples

# A constructor is a special method in a class that is automatically called when an object is created. It is used to initialize the object's attributes.


# Example 1 with explanation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")


# In this example, the __init__ method is the constructor of the Dog class. It takes two parameters, name and age, and initializes the object's attributes self.name and self.age with the values passed to the constructor.


# Example 2 with explanation
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")


# In this example, the __init__ method is the constructor of the Car class. It takes two parameters, model and year, and initializes the object's attributes self.model and self.year with the values passed to the constructor.


# now we can create objects from these classes

dog1 = Dog("Buddy", 5)
dog1.bark()


car1 = Car("Toyota", 2020)
car1.drive()


person1 = Person("John", 25)
person1.walk()

# Object contains state, identity and behavior

# Explain state ,identity and behavior of an object in python with examples


# State: The state of an object is the value of its attributes at a given time. For example, the state of a car object can be its model and year.

# Identity: The identity of an object is a unique identifier that distinguishes it from other objects. For example, two car objects with the same model and year are still different objects with different identities.

# Behavior: The behavior of an object is defined by its methods, which are functions that can be called on the object to perform certain actions. For example, a car object can have a drive method that allows it to drive.


# Example 1 explaining state, identity and behavior of an object
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")


car1 = Car("Toyota", 2020)
car1.drive()

# State: The state of car1 object is model = "Toyota" and year = 2020
# Identity: The identity of car1 object is unique and different from other objects
# Behavior: The behavior of car1 object is to drive, which is defined by the drive method


# Class Attributes and Instance Attributes

# Explain class attributes and instance attributes in python with examples

# Class attributes are attributes that are shared by all instances of a class. They are defined outside the constructor and are accessed using the class name.

# Instance attributes are attributes that are specific to each instance of a class. They are defined inside the constructor and are accessed using the self keyword.


# Example 1 with explanation
class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute


dog1 = Dog("Buddy", 5)


# In this example, species is a class attribute that is shared by all instances of the Dog class. name and age are instance attributes that are specific to each instance of the Dog class.


# Example 2 with explanation
class Car:
    wheels = 4  # class attribute

    def __init__(self, model, year):
        self.model = model  # instance attribute
        self.year = year  # instance attribute


# In this example, wheels is a class attribute that is shared by all instances of the Car class. model and year are instance attributes that are specific to each instance of the Car class.


# Method in python

# Explain method in python with examples

# A method is a function that is associated with a class and can be called on an object of that class. It can perform actions on the object or return values.


# Example 1 with explanation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")


dog1 = Dog("Buddy", 5)

dog1.bark()
# In this example, bark is a method of the Dog class. It takes no parameters (other than self, which is a reference to the object itself) and prints a message indicating that the dog is barking.


# Example 2 with explanation
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")


# In this example, drive is a method of the Car class. It takes no parameters (other than self) and prints a message indicating that the car is driving.


# Inheritance in python

# Explain inheritance in python with examples


# Inheritance is a mechanism in which a new class inherits attributes and methods from an existing class. The existing class is called the base class or parent class, and the new class is called the derived class or child class.


# Example 1 with explanation
class Animal:
    def __init__(self, providedspecies):
        self.species = providedspecies

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog("Canis familiaris")

animal1 = Animal("something")
animal1.eat()

# In this example, Animal is the base class and Dog is the derived class. Dog inherits the attributes and methods of Animal, such as the species attribute and the eat method. It also defines its own method, bark.


# Example 2 with explanation
class Vehicle:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("Vehicle is driving")


class Car(Vehicle):
    def honk(self):
        print("Car is honking")


car1 = Car("Toyota")

# In this example, Vehicle is the base class and Car is the derived class. Car inherits the attributes and methods of Vehicle, such as the model attribute and the drive method. It also defines its own method, honk.


# Polymorphism in python

# Explain polymorphism in python with examples

# Polymorphism is the ability of an object to take on different forms or behaviors depending on the context in which it is used. It allows objects of different classes to be treated as objects of a common superclass.


# Example 1 with explanation


class Animal:

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Dog is barking")


class Cat(Animal):
    def speak(self):
        print("Cat is meowing")


dog1 = Dog()
cat1.speak()

# In this example, Animal is the base class with a speak method that does nothing. Dog and Cat are derived classes that override the speak method with their own implementations. This allows objects of type Dog and Cat to be treated as objects of type Animal.


# Example 2 with explanation
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# explain encapsulation in python with examples

# Encapsulation is the bundling of data and methods that operate on that data into a single unit, called a class. It allows the data to be hidden from the outside world and accessed only through the methods of the class.


# Example 1 with explanation


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


p1 = Person("John", 25)
print(p1.get_name())

# In this example, the name and age attributes of the Person class are encapsulated by making them private (using double underscores). The get_name and get_age methods provide controlled access to these attributes, allowing them to be accessed only through these methods.


# Example 2 with explanation


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")


# In this example, the account_number and balance attributes of the BankAccount class are encapsulated by making them private. The deposit and withdraw methods provide controlled access to these attributes, allowing deposits and withdrawals to be made only through these methods.


# Abstraction in python

# Explain abstraction in python with examples

# Abstraction is the process of hiding the implementation details of a class and exposing only the essential features to the outside world. It allows the user to interact with the class without needing to know how it is implemented.


# Example 1 with explanation
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# In this example, Shape is an abstract base class with an abstract method area. Circle is a concrete class that inherits from Shape and provides an implementation of the area method. The user can interact with the Circle class without needing to know the details of how the area is calculated.


# Example 2 with explanation
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Dog is barking")


class Cat(Animal):
    def speak(self):
        print("Cat is meowing")


# In this example, Animal is an abstract base class with an abstract method speak. Dog and Cat are concrete classes that inherit from Animal and provide implementations of the speak method. The user can interact with objects of type Dog and Cat without needing to know the details of how they speak.


# Composition in python

# Explain composition in python with examples

# Composition is a design technique in which a class contains objects of other classes as attributes. It allows for code reuse and flexibility in defining relationships between classes.


# Example 1 with explanation
class Engine:
    def start(self):
        print("Engine is starting")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")


# In this example, Engine is a class that represents an engine. Car is a class that contains an Engine object as an attribute. When a Car object is created, it contains an Engine object, which can be used to start the engine and drive the car.


# Example 2 with explanation
class Wheel:
    def rotate(self):
        print("Wheel is rotating")


class Bicycle:
    def __init__(self):
        self.front_wheel = Wheel()
        self.rear_wheel = Wheel()

    def ride(self):
        self.front_wheel.rotate()
        self.rear_wheel.rotate()
        print("Bicycle is riding")


# In this example, Wheel is a class that represents a wheel. Bicycle is a class that contains two Wheel objects as attributes (front_wheel and rear_wheel). When a Bicycle object is created, it contains two Wheel objects, which can be used to rotate the wheels and ride the bicycle.


# static method in python

# Explain static method in python with examples

# A static method is a method that is associated with a class rather than an instance of the class. It does not have access to the instance attributes or methods and does not require an instance of the class to be called.


# Example 1 with explanation
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


result = MathUtils.add(5, 10)
print(result)


# In this example, add is a static method of the MathUtils class. It takes two parameters, x and y, and returns their sum. The static method can be called using the class name without needing an instance of the class.


# Example 2 with explanation
class StringUtils:

    @staticmethod
    def reverse(string):
        return string[::-1]


result = StringUtils.reverse("hello")

print(result)


# In this example, reverse is a static method of the StringUtils class. It takes a string as a parameter and returns the reversed string. The static method can be called using the class name without needing an instance of the class.


# super() in python


# Explain super() in python with examples

# super() is a built-in function that allows a derived class to call the constructor or methods of its base class. It is commonly used in inheritance to access the base class's attributes and methods.


# Example 1 with explanation
class Animal:
    def __init__(self, species):
        self.species = species

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def bark(self):
        print("Dog is barking")


dog1 = Dog("Canis familiaris", "Labrador")

# In this example, Animal is the base class with an __init__ method that initializes the species attribute. Dog is the derived class that calls the base class's __init__ method using super() to initialize the species attribute. The breed attribute is specific to the Dog class.


# Example 2 with explanation


class Vehicle:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("Vehicle is driving")


class Car(Vehicle):
    def __init__(self, model, year):
        super().__init__(model)
        self.year = year

    def honk(self):
        print("Car is honking")


car1 = Car("Toyota", 2020)

# In this example, Vehicle is the base class with an __init__ method that initializes the model attribute. Car is the derived class that calls the base class's __init__ method using super() to initialize the model attribute. The year attribute is specific to the Car class.


# Decorators in python

# Explain decorators in python with examples

# Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods. They are used to add functionality to existing functions without modifying their code.


# Example 1 with explanation
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@uppercase_decorator
def greet():
    return "hello"


result = greet()
print(result)


# In this example, uppercase_decorator is a decorator function that takes a function as a parameter and returns a new function that modifies the result of the original function by converting it to uppercase. The @uppercase_decorator syntax is used to apply the decorator to the greet function.


# class method in python


# Explain class method in python with examples

# A class method is a method that is associated with a class rather than an instance of the class. It takes the class itself as the first parameter (usually named cls) and can be called using the class name.


# Example 1 with explanation
class MathUtils:
    @classmethod
    def add(cls, x, y):
        return x + y


result = MathUtils.add(5, 10)
print(result)


# In this example, add is a class method of the MathUtils class. It takes two parameters, x and y, and returns their sum. The class method can be called using the class name.


# Example 2 with explanation
class StringUtils:
    @classmethod
    def reverse(cls, string):
        return string[::-1]


result = StringUtils.reverse("hello")

print(result)


# In this example, reverse is a class method of the StringUtils class. It takes a string as a parameter and returns the reversed string. The class method can be called using the class name.


# Conclusion

# we have covered the key concepts of object-oriented programming in Python, including classes, constructors, methods, inheritance, polymorphism, encapsulation, abstraction, composition, static methods, super(), decorators, and class methods. Understanding these concepts is essential for writing clean, modular, and maintainable code in Python. I hope this article has helped you gain a better understanding of object-oriented programming in Python and how to apply these concepts in your own projects. Thank you for reading!


# Class method vs Static method in python

# Explain class method vs static method in python with examples

# A class method is a method that is associated with a class rather than an instance of the class. It takes the class itself as the first parameter (usually named cls) and can be called using the class name.

# A static method is a method that is associated with a class rather than an instance of the class. It does not have access to the instance attributes or methods and does not require an instance of the class to be called.


# Example 1 with explanation
class MathUtils:
    @classmethod
    def add(cls, x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y


result1 = MathUtils.add(5, 10)
result2 = MathUtils.subtract(10, 5)

print(result1)
