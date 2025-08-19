# ---

# ## **🧠 Abstraction in Python (with Real-World Analogies & Use Cases)**

# ---

# ### **🔍 What is Abstraction?**

# **Abstraction** means **hiding complex implementation details** and **showing only the necessary features** to the user.

# It focuses on **what** an object does instead of **how** it does it.

# > ✅ **Goal**: Simplify the interface, reduce complexity, and isolate the impact of changes.

# ---

# ### **🧬 Real-World Analogy: Driving a Car**

# * When you drive a car, you **press the accelerator**, **brake**, or **steering wheel**.
# * You don’t need to know **how the engine ignites fuel**, or **how brakes generate friction**—that’s **hidden**.
# * You only use a **simple interface**.

# 🧠 That’s abstraction: exposing only *what's important* and hiding *internal mechanics*.

# ---

# ### **🛠️ Abstraction in Python**

# Python supports abstraction mainly through:

# * **Abstract Classes**
# * **Abstract Methods**

# We use the `abc` (**A**bstract **B**ase **C**lasses) module for this.

# ---

# ### **📦 Code Example (With Real-World Analogy)**

# Let’s say we’re building a **Payment System**.

# ```python
# from abc import ABC, abstractmethod


# # Abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete class
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


# # Driver code
payment1 = CreditCardPayment()
payment1.pay(100)

payment2 = PayPalPayment()
payment2.pay(250)
# ```

# ### 🧾 **Output:**

# ```
# Paid 100 using Credit Card.
# Paid 250 using PayPal.
# ```

# #### ✅ You only care about `.pay(amount)` – not how PayPal or CreditCard processes the payment behind the scenes!

# ---

# ## **🔗 Abstract Class vs Concrete Class**

# | Concept           | Description                                                                       |
# | ----------------- | --------------------------------------------------------------------------------- |
# | `Abstract Class`  | A class that cannot be instantiated. It may contain abstract methods.             |
# | `Abstract Method` | A method declared but not implemented in the base class.                          |
# | `Concrete Class`  | A class that inherits from an abstract class and implements all abstract methods. |

# ---

# ## **🧬 Real Use Cases of Abstraction**

# | Use Case                   | Description                                                                                                       |
# | -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
# | 🚗 **Vehicle API**         | Different vehicle types (Car, Bike, Truck) can have `.start()`, `.stop()` methods, but their inner workings vary. |
# | 💰 **Payment Systems**     | Abstract "Payment" interface while hiding third-party details (Stripe, Razorpay, PayPal).                         |
# | 🎮 **Game Design**         | Abstract class "Character" with move(), attack(), defend()—different for each subclass.                           |
# | 🏢 **Enterprise Software** | Abstracting database layers, APIs, services to improve maintainability.                                           |

# ---

# ### **Types of Abstraction in Python**

# | Type                        | Description                                                                 |
# | --------------------------- | --------------------------------------------------------------------------- |
# | **Data Abstraction**        | Hiding internal object details. Eg: Class/Encapsulation.                    |
# | **Functional Abstraction**  | Hiding function logic. Eg: Using built-in methods like `len()` or `sort()`. |
# | **Class-level Abstraction** | Done using Abstract Base Classes.                                           |

# ---

# ## **✅ Benefits of Abstraction**

# * Reduces complexity
# * Promotes cleaner code
# * Enhances security (prevents misuse of internal logic)
# * Improves scalability (easy to change internals)

# ---

# ## **🚀 Conclusion**

# > **Abstraction** is about designing with simplicity in mind—letting users interact with your code **without worrying about how things work under the hood**.

# It’s like using a TV remote—you just press buttons; you don’t open the remote to figure out how it sends signals. Python helps you build such smart, clean interfaces using **abstract classes and methods**.


## 🧾 **Example 1: Animal Sounds (Abstract Class)**

# Let’s model different animals making sounds, but we don't care *how* each animal makes the sound — only *that* they do.

# ```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")


# Client code
animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
# ```

# ### 🧠 Analogy:

# You ask any animal to make a sound. You don’t need to know its vocal mechanism. That’s **abstraction**.

# ---

# ## 🔧 **Example 2: File Reader System**

# Different file types can be opened, but how they are opened internally differs.

# ```python
from abc import ABC, abstractmethod


class FileReader(ABC):
    @abstractmethod
    def read(self):
        pass


class PDFReader(FileReader):
    def read(self):
        print("Reading a PDF file.")


class WordReader(FileReader):
    def read(self):
        print("Reading a Word document.")


def display_content(reader: FileReader):
    reader.read()


# Using the abstraction
display_content(PDFReader())
display_content(WordReader())
# ```

# 💡 `display_content()` doesn't care about the file type. It only calls `.read()`.

# ---

# ## 🎮 **Example 3: Game Controller Interface**

# Let’s abstract the concept of a game controller, where different platforms (PC, Console) implement differently.

# ```python
from abc import ABC, abstractmethod


class GameController(ABC):
    @abstractmethod
    def press_button(self):
        print("Button is pressed")


class PCController(GameController):
    def press_button(self):
        print("PC: WASD keys pressed")


class ConsoleController(GameController):
    def press_button(self):
        print("Console: Gamepad button pressed")


# Player interacts
def play_game(controller: GameController):
    controller.press_button()


play_game(PCController())
play_game(ConsoleController())
# ```

# ---

# ## 🏦 **Example 4: Bank Transactions**

# You want to perform a transaction, but the internal processing of banks may differ.

# ```python
# from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def transfer(self, amount):
        pass


class HBL(Bank):
    def transfer(self, amount):
        print(f"HBL transferred Rs. {amount}")


class Meezan(Bank):
    def transfer(self, amount):
        print(f"Meezan transferred Rs. {amount} ")


bank1 = HBL()
bank2 = Meezan()

# bank1.transfer(5000)
# bank2.transfer(3000)
# ```

# ---

# ## 🛍️ **Example 5: E-commerce Checkout System**

# ```python
from abc import ABC, abstractmethod


class CheckoutMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(CheckoutMethod):
    def process_payment(self, amount):
        print(f"Processing card payment of Rs. {amount}")


class CashOnDelivery(CheckoutMethod):
    def process_payment(self, amount):
        print(f"Will collect Rs. {amount} on delivery")


def complete_checkout(method: CheckoutMethod, amount):
    method.process_payment(amount)


complete_checkout(CardPayment(), 1500)
complete_checkout(CashOnDelivery(), 2200)
# ```

# ---

# ## ✅ **Summary of What These Examples Teach You**

# | Example         | Teaches You                             |
# | --------------- | --------------------------------------- |
# | Animal          | Abstract class with method override     |
# | File Reader     | Flexible reading logic per file type    |
# | Game Controller | Same interface, different platforms     |
# | Bank            | Same action, different processing rules |
# | E-commerce      | Checkout interface abstracted           |
