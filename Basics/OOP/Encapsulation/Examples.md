Got it 👍 let’s dive into **more real-world examples of Encapsulation** before moving to Abstraction.

---

# 🌍 **Real-World Encapsulation Examples**

### 1️⃣ **ATM Machine**

- You **insert card, enter PIN, withdraw money**.
- You don’t see the **internal banking system** (how it validates balance, connects to bank server).
- That logic is **encapsulated** inside.

```python
class ATM:
    def __init__(self, balance):
        self.__balance = balance   # private

    def withdraw(self, pin, amount):
        if pin == 1234 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn {amount}, remaining: {self.__balance}"
        else:
            return "Transaction failed!"

atm = ATM(5000)
print(atm.withdraw(1234, 1000))   # ✅ allowed
print(atm.withdraw(1111, 1000))   # ❌ wrong PIN
```

---

### 2️⃣ **Car (Speed Control)**

- When you drive, you press the **accelerator**.
- You don’t directly control the **fuel injection or engine** — that’s encapsulated.

```python
class Car:
    def __init__(self):
        self.__speed = 0   # private

    def accelerate(self, amount):
        self.__speed += amount
        print(f"Car speed: {self.__speed} km/h")

    def brake(self, amount):
        self.__speed = max(0, self.__speed - amount)
        print(f"Car speed: {self.__speed} km/h")

car = Car()
car.accelerate(50)  # Car speed: 50 km/h
car.brake(20)       # Car speed: 30 km/h
```

---

### 3️⃣ **Hospital Patient Records**

- Patient’s medical history must be **private**.
- Doctors can view it, but random people cannot.

```python
class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.__disease = disease  # private

    def get_disease(self, doctor):
        if doctor == "authorized":
            return self.__disease
        else:
            return "Access denied!"

p = Patient("Ali", "Diabetes")
print(p.get_disease("guest"))       # ❌ Access denied
print(p.get_disease("authorized"))  # ✅ Diabetes
```

---

### 4️⃣ **Mobile Phone**

- You **use apps, make calls**.
- You don’t see the **operating system’s inner code** (hidden/encapsulated).

---

### 5️⃣ **University System**

- Students can **view their grades**, but cannot **directly edit them**.
- Grades are encapsulated and only teachers/admins can modify.

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = None  # private

    def set_grade(self, teacher, grade):
        if teacher == "professor":
            self.__grade = grade
        else:
            print("Not authorized!")

    def get_grade(self):
        return self.__grade

s = Student("Sara")
s.set_grade("student", "A")     # ❌ Not authorized
s.set_grade("professor", "A")   # ✅ Allowed
print(s.get_grade())            # A
```

---

✅ These examples show that Encapsulation is everywhere:

- **Banking (balance protection)**
- **Cars (speed control)**
- **Hospitals (privacy of records)**
- **Phones (hiding OS internals)**
- **Universities (grades security)**

---
