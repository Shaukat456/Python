## Section A: Multiple Choice Questions (10 Marks)

(Choose the correct option. Each carries 1 mark.)

**Q1. Output?**

```python
for i in range(2, 10, 2):
    if i % 3 == 0:
        break

```

a) Done  
b) No output  
c) Error  
d) Loop exits at i=6

---

**Q2. Which of these will throw an error?**
a) `def f(x, y=1, z=2): return x+y+z`  
b) `def f(x=1, y, z=2): return x+y+z`  
c) `def f(x, y, z=2): return x+y+z`  
d) `def f(x, y=1, *args): return x+y`

---

**Q3. Output?**

```python
def f(x, l=[]):
    l.append(x)
    return l
print(f(1))
print(f(2))
```

a) [1], [2]  
b) [1], [1, 2]  
c) [1], [1]  
d) Error

---

**Q4. Which statement about recursion is false?**
a) Python supports recursion  
b) Recursion depth is limited  
c) Recursive functions must have a base case

---

**Q5. Output?**

```python
for j in range(0, 10 + 1):
    print(j - 2)
```

Make iteration column with column names: J, output

---

**Q6. Which of the following is invalid lambda?**
a) `lambda x: x + 1`  
b) `lambda x, y: x if x > y else y`  
c) none of these

---

**Q7. Output?**

```python
for i in range(1, 4):
    for j in range(i):
        if j == 1:
            break
        else:
            print(i, end=" ")
```

a) 1 2 3  
b) 1 3  
c) 2 3  
d) 1

---

**Q8. Output?**

```python
class Bike(Vehicle):
    def wheelie(self):
        print("Bike performs a wheelie!")

car = Car("Honda", 100)
bike = Bike("Yamaha", 80)
car.move()
bike.move()
```

Which concept of OOP is being applied here?

---

## Section B: Conceptual & Programming Questions (20 Marks)

**Q9. Explain the difference between shallow copy and deep copy in Python with example.**

---

**Q10. Write a program using dictionary to count character frequency in a string (ignoring spaces).**

---

**Q11. Output?**

```python
x = (1, 2, 3)
y = (1, 2, 3)
print(x is y, x == y)
```

---

**Q12. Write a function that accepts a list of integers and stores them in a list only if they are even.**

---

**Q13. Output?**

```python
a = [1, 2, 3]
b = a
b.append(6)
print(a)
```

---

**Q14. Write a recursive function to calculate factorial of a number.**

---

**Q15. Output?**

```python
d = {"a": 1, "b": 2}
print(d["c"])
```

---

**Q16. Output?**

```python
def f(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst
print(f(10))
print(f(20))
```

---

**Q17. Write a program to check whether a tuple contains duplicate elements.**

---

**Q18. Output?**

```python
x = [1, 2, 3]
y = x
y = y + [4]
print(x, y)
```

---

**Q19. Output?**

```python
s = 0
for i in range(3):
    for j in range(i):
        s += j
print(s)
```

---

**Q20. Output?**

```python
def add(val, res=[]):
    res.append(val)
    return res
print(add(5))
print(add(10, []))
print(add(15))
```

---

**Q21. Output?**

```python
for i in range(3):
    print(i)
```

---

**Q22. Write a program that computes the average of values entered by the user.**

---

**Q23. Write the output of each code and display its working also?**

```python
for i in range(1, 4):
    a = [n for n in range(10, 30) if (n % 5 == 0 or n % 7 == 0)]
    for j in range(1, 4):
        print(a)
        if i * j > 2:
            break
        print(i * j, end="")
print(i)
```

---

---

**Q25. What will be the output?**

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

---

**Q26. Which of the following is immutable?**
a) List  
b) Tuple  
c) Dictionary  
d) Set

---

**Q27. What will len(set([1, 2, 2, 3, 3])) return?**
a) 5  
b) 3  
c) 4  
d) Error

---

**Q28. Which keyword is used to define a function in Python?**
a) func  
b) define  
c) def  
d) function

---

**Q29. What will be the output?**

```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

a) 2 5 8  
b) 2 4 6 8  
c) 2 10  
d) Error

---

**Q30. Dictionaries store data in:**
a) Index order  
b) Key-Value pairs  
c) Sorted order  
d) Random values

---

## Section C: Short Questions

**Q31. Differentiate between local and global variables with example.**

---

**Q32. Explain difference between list and tuple with one example each.**

---

**Q33. Write a code using if-elif-else that checks a student’s grade:**

- A if marks ≥ 80
- B if 60–79
- C if 40–59
- Fail otherwise

---

**Q34. What is the output of the following?**

```python
x = [1, 2, 3]
y = (1, 2, 3)
print(x * 2)
print(y * 2)
```

---

**Q35. Explain dictionary methods: get(), keys(), values().**

---

---

**Q37. What will be the output?**

```python
def test(a, b=2, c=3):
    return a + b + c

print(test(1))
print(test(1, 5))
```

---

**Q38. What is a class in Python?**

---

**Q39. How do you create an object from a class in Python?**

---

**Q40. What is the purpose of the `__init__` method in a class?**

---

**Q41. How do you define a method inside a class?**

---

**Q42. What is the difference between a class variable and an instance variable?**

---

**Q43. How do you access an instance variable from a method within the same class?**

---

**Q44. What is inheritance in Python?**

---

**Q45. How do you create a subclass in Python?**

---

**Q46. What is method overriding in Python?**

---

**Q47. How do you call a method from a parent class in a subclass?**

---

**Q48. What is polymorphism in Python?**

---

**Q49. How can you implement polymorphism using method overloading in Python?**

---

**Q50. What is encapsulation in OOP?**

---

**Q51. How do you make an attribute private in a Python class?**

---

**Q52. What is the purpose of the `self` keyword in Python?**

---

## For Loop Questions

**Q53.**

```python
total = 0
for i in range(5):
    total += i
print(total)
```

**Output:** ?

---

**Q54.**

```python
for i in range(1, 6):
    print(i * 2)
```

**Output:** ?

---

**Q55.**

```python
count = 0
for i in range(10):
    if i % 2 == 0:
        count += 1
print(count)
```

**Output:** ?

---

**Q56.**

```python
result = 1
for i in range(1, 4):
    result *= i
print(result)
```

**Output:** ?

---

**Q57.**

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
```

**Output:** ?

---

**Q58.**

```python
total = 0
for i in range(1, 11):
    if i % 3 == 0:
        total += i
print(total)
```

**Output:** ?

---

**Q59.**

```python
for i in range(5):
    for j in range(2):
        print(i, j)
```

**Output:** ?

---

**Q60.**

```python
letters = 'abcde'
for letter in letters:
    print(letter.upper())
```

**Output:** ?

---

**Q61.**

```python
total = 0
for i in range(1, 6):
    total += i ** 2
print(total)
```

**Output:** ?

---

**Q62.**

```python
for i in range(5, 0, -1):
    print(i)
```

**Output:** ?

---

## While Loop Questions

**Q63.**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Output:** ?

---

**Q64.**

```python
num = 10
while num > 0:
    num -= 2
print(num)
```

**Output:** ?

---

**Q65.**

```python
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print(total)
```

**Output:** ?

---

**Q66.**

```python
n = 1
while n < 4:
    print(n)
    n += 1
print(n)
```

**Output:** ?

---

**Q67.**

```python
x = 0
while x < 3:
    x += 1
    print(x)
```

**Output:** ?

---

---

---

**Q72.**

```python
i = 0
while i < 5:
    print(i)
    i += 2
```

**Output:** ?

---

This concludes the Python paper for Final TERM 2025. Good luck!
