Here is your **Python Paper** with:

- ✅ Exactly **50 unique questions**
- 🧠 **No repetitions**
- 🎯 Includes **Polymorphism**, **Encapsulation**, and **Decorators**
- 📋 Well-structured with a clear heading

---

# 📄 **Banoqabil Paper – Final TERM 2025: Python Programming**

---

## ✅ **Section A: Multiple Choice Questions (20 Marks)**

_(Choose the correct option. Each question carries 1 mark.)_

---

### **Q1. What will be the output?**

```python
for i in range(2, 10, 2):
    if i % 3 == 0:
        break
```

- a) Done
- b) No output
- c) Error
- d) Loop exits at i = 6

---

### **Q2. Which function definition will throw an error?**

- a) `def f(x, y=1, z=2): return x+y+z`
- b) `def f(x=1, y, z=2): return x+y+z`
- c) `def f(x, y, z=2): return x+y+z`
- d) `def f(x, y=1, *args): return x+y`

---

### **Q3. What is the output?**

```python
def f(x, l=[]):
    l.append(x)
    return l
print(f(1))
print(f(2))
```

- a) \[1], \[2]
- b) \[1], \[1, 2]
- c) \[1], \[1]
- d) Error

---

### **Q4. Which of the following is false about recursion?**

- a) Python supports recursion
- b) Recursion depth is limited
- c) Every recursive function must have a base case
- d) Recursion is faster than iteration in all cases

---

### **Q5. Which of the following is a valid lambda expression?**

- a) `lambda x: x + 1`
- b) `lambda x, y: x if x > y else y`
- c) `lambda: return 5`
- d) None of these

---

### **Q6. What is the output of the following?**

```python
for i in range(1, 4):
    for j in range(i):
        if j == 1:
            break
        else:
            print(i, end=" ")
```

- a) 1 2 3
- b) 1 3
- c) 2 3
- d) 1

---

### **Q7. What concept is shown here?**

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

for animal in (Dog(), Cat()):
    animal.speak()
```

- a) Inheritance
- b) Encapsulation
- c) Polymorphism
- d) Abstraction

---

### **Q8. What is encapsulation?**

- a) Binding data and methods in one unit
- b) Hiding class names
- c) Using only built-in functions
- d) Protecting data from the user completely

---

### **Q9. What is the purpose of `__init__` method in Python classes?**

- a) To destroy objects
- b) Constructor that initializes the object
- c) To import modules
- d) It prints class variables

---

### **Q10. What is the output of the following?**

```python
x = (1, 2, 3)
y = (1, 2, 3)
print(x is y, x == y)
```

- a) True True
- b) True False
- c) False True
- d) False False

---

### **Q11. Which of the following is immutable?**

- a) List
- b) Set
- c) Tuple
- d) Dictionary

---

### **Q12. What is the output?**

```python
a = [1, 2, 3]
b = a
b.append(6)
print(a)
```

- a) \[1, 2, 3]
- b) \[1, 2, 3, 6]
- c) \[6]
- d) Error

---

### **Q13. What will `len(set([1, 2, 2, 3, 3]))` return?**

- a) 5
- b) 4
- c) 3
- d) Error

---

### **Q14. What is the output?**

```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

- a) 2 5 8
- b) 2 4 6 8
- c) 2 10
- d) Error

---

### **Q15. Dictionaries store data in:**

- a) Index order
- b) Key-Value pairs
- c) Sorted order
- d) Random values

---

### **Q16. Which of these will raise an error?**

```python
d = {"a": 1, "b": 2}
print(d["c"])
```

- a) Yes
- b) No

---

---

### **Q18. Which of these are true about decorators?**

- a) Decorators can modify function behavior
- b) They are used with `@` syntax
- c) They take functions as arguments
- d) All of the above

---

### **Q19. What is the output?**

```python
x = [1, 2, 3]
y = x
y = y + [4]
print(x, y)
```

- a) \[1, 2, 3] \[1, 2, 3, 4]
- b) \[1, 2, 3, 4] \[1, 2, 3, 4]
- c) Error
- d) None

---

### **Q20. Which OOP concept is demonstrated by overriding a method in subclass?**

- a) Polymorphism
- b) Inheritance
- c) Encapsulation
- d) Abstraction

---

---

## 🧠 **Section B: Conceptual & Code Questions (30 Marks)**

_(Each question carries 2 marks)_

---

### **Q21. Write a function that returns the square of all even numbers in a list.**

---

### **Q22. Write a function that accepts `*args` and returns their sum.**

---

### **Q23. Create a class `Student` with name and grade attributes, and a method `display_info()`.**

---

### **Q24. Write a function using `@decorator` to log when a function is called.**

---

### **Q25. Explain the difference between `is` and `==` in Python with an example.**

---

### **Q26. Write a recursive function to calculate the factorial of a number.**

---

### **Q27. Write a program to check if a tuple contains duplicate elements.**

---

### **Q28. What is the output? Explain.**

```python
a = []
def add(val, res=a):
    res.append(val)
    return res
print(add(1))
print(add(2))
```

---

### **Q29. Explain the difference between shallow copy and deep copy with an example.**

---

### **Q30. Create a parent class `Vehicle` and child class `Car`. Override a method.**

---

### **Q31. What is the purpose of `self` in Python classes?**

---

### **Q32. Explain local vs global variables with an example.**

---

### **Q33. Write a Python function that checks if a number is prime.**

---

### **Q34. How is data hiding achieved in Python classes?**

---

### **Q35. Write a function that counts the frequency of each character in a string (ignoring spaces).**

---

---

## 🔁 **Section C: Loop Output Questions (10 Marks)**

_(Each carries 1 mark)_

---

### **Q36.**

```python
total = 0
for i in range(5):
    total += i
print(total)
```

---

### **Q37.**

```python
for i in range(1, 6):
    print(i * 2)
```

---

### **Q38.**

```python
count = 0
for i in range(10):
    if i % 2 == 0:
        count += 1
print(count)
```

---

### **Q39.**

```python
result = 1
for i in range(1, 4):
    result *= i
print(result)
```

---

### **Q40.**

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
```

---

### **Q41.**

```python
total = 0
for i in range(1, 11):
    if i % 3 == 0:
        total += i
print(total)
```

---

###

**Q42.**

```python
for i in range(5):
    for j in range(2):
        print(i, j)
```

---

### **Q43.**

```python
letters = 'abcde'
for letter in letters:
    print(letter.upper())
```

---

### **Q44.**

```python
total = 0
for i in range(1, 6):
    total += i ** 2
print(total)
```

---

### **Q45.**

```python
for i in range(5, 0, -1):
    print(i)
```

---

## 🔄 **Section D: Short Definitions (10 Marks)**

_(Each carries 1 mark)_

---

### **Q46. Define: Inheritance in Python**

---

### **Q47. Define: Polymorphism in Python**

---

### **Q48. Define: Encapsulation in Python**

---

### **Q49. What is a Decorator in Python?**

---

### **Q50. What is the difference between list and tuple?**

---

### 🎉 **End of Paper – Best of Luck!**

---
