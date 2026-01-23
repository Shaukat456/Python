## ===

# 🟨 JavaScript Quiz (20 Questions)

### **Topics Covered**

✅ Variables
✅ Operators
✅ Functions
✅ Callback Functions
✅ for / while loops on arrays

---

## 🧠 PART 1: Variables (Q1–Q4)

### **Q1.** What will be the output?

```js
let x = 10;
x = 20;
console.log(x);
```

A) 10
B) 20
C) Error
D) undefined

---

### **Q2.** Which variable can be **reassigned**?

A) `const a = 5`
B) `let a = 5`
C) `const a = []`
D) Both B and C

---

### **Q3.** What is the output?

```js
var a = 5;
var a = 10;
console.log(a);
```

A) Error
B) 5
C) 10
D) undefined

---

### **Q4.** Which is **block scoped**?

A) var
B) let
C) const
D) Both B and C

---

## ⚙️ PART 2: Operators (Q5–Q8)

### **Q5.** What is the output?

```js
console.log(5 == "5");
```

A) true
B) false
C) Error
D) undefined

---

### **Q6.** What is the output?

```js
console.log(5 === "5");
```

A) true
B) false
C) Error
D) undefined

---

### **Q7.** What will this print?

```js
let x = 10;
console.log(x++ + ++x);
```

A) 21
B) 22
C) 23
D) 24

---

### **Q8.** Which operator checks **both value and type**?

A) ==
B) =
C) ===
D) !==

---

## 🔧 PART 3: Functions (Q9–Q12)

### **Q9.** What is the output?

```js
function add(a, b) {
  return a + b;
}
console.log(add(2, 3));
```

A) 23
B) 5
C) undefined
D) Error

---

### **Q10.** What happens here?

```js
console.log(square(4));

function square(n) {
  return n * n;
}
```

A) Error
B) undefined
C) 16
D) NaN

---

### **Q11.** What is a function that does **not return anything** called?

A) Pure function
B) Callback function
C) Void function
D) Anonymous function

---

### **Q12.** What will be logged?

```js
function test() {
  console.log("Hello");
}
let result = test();
console.log(result);
```

A) Hello Hello
B) Hello undefined
C) undefined Hello
D) Error

---

## 🔁 PART 4: Callback Functions (Q13–Q15)

### **Q13.** What is a callback function?

A) Function that calls itself
B) Function passed as argument to another function
C) Function inside loop
D) Function that returns another function

---

### **Q14.** What is the output?

```js
function greet(name, callback) {
  callback(name);
}

greet("Ali", function (n) {
  console.log("Hello " + n);
});
```

A) Hello Ali
B) Hello
C) Ali
D) Error

---

### **Q15.** Which built-in JS function uses callbacks?

A) map()
B) filter()
C) setTimeout()
D) All of the above

---

## 🔄 PART 5: Loops on Arrays (Q16–Q20)

### **Q16.** What is the output?

```js
let arr = [1, 2, 3];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

A) 1 2 3
B) 0 1 2
C) undefined
D) Error

---

### **Q17.** What will this print?

```js
let arr = [10, 20, 30];
let i = 0;
while (i < arr.length) {
  console.log(arr[i]);
  i++;
}
```

A) 10 20 30
B) 0 1 2
C) undefined
D) Error

---

### **Q18.** What is the output?

```js
let arr = ["a", "b", "c"];
for (let index in arr) {
  console.log(index);
}
```

A) a b c
B) 0 1 2
C) undefined
D) Error

---

### **Q19.** What is the output?

```js
let arr = ["a", "b", "c"];
for (let value of arr) {
  console.log(value);
}
```

A) 0 1 2
B) a b c
C) undefined
D) Error

---

### **Q20.** Best loop to iterate **values** of an array?

A) for
B) while
C) for...in
D) for...of

---

---

### **Q21.** What will be the output?

```js
let a = 5;
{
  let a = 10;
}
console.log(a);
```

A) 10
B) 5
C) undefined
D) Error

---

### **Q22.** What happens here?

```js
const arr = [1, 2, 3];
arr.push(4);
console.log(arr);
```

A) Error
B) [1,2,3]
C) [1,2,3,4]
D) undefined

---

### **Q23.** What is the output?

```js
let x;
console.log(x);
```

A) null
B) undefined
C) Error
D) 0

---

### **Q24.** Which keyword allows **re-declaration in same scope**?

A) let
B) const
C) var
D) none

---

## ⚙️ PART 7: Operators & Expressions (Q25–Q28)

### **Q25.** What will this print?

```js
console.log(true + false);
```

A) true
B) false
C) 1
D) Error

---

### **Q26.** What is the output?

```js
console.log("5" - 2);
```

A) 3
B) "52"
C) NaN
D) Error

---

### **Q27.** What is the result?

```js
console.log(0 || "JS");
```

A) 0
B) false
C) "JS"
D) undefined

---

### **Q28.** What will this log?

```js
console.log(!!"hello");
```

A) false
B) true
C) "hello"
D) Error

---

## 🔧 PART 8: Functions & Return (Q29–Q32)

### **Q29.** What is the output?

```js
function sum(a, b) {
  console.log(a + b);
}
let result = sum(2, 3);
console.log(result);
```

A) 5 undefined
B) undefined 5
C) 5 5
D) Error

---

### **Q30.** What type of function is this?

```js
const greet = function () {
  console.log("Hi");
};
```

A) Arrow function
B) Named function
C) Anonymous function
D) Callback function

---

### **Q31.** What will be printed?

```js
function test(x) {
  return x * 2;
}
console.log(test());
```

A) NaN
B) undefined
C) 0
D) Error

---

### **Q32.** What happens if a function has no `return`?

A) Returns null
B) Returns 0
C) Returns undefined
D) Throws error

---

## 🔁 PART 9: Callback & Higher Order Functions (Q33–Q36)

### **Q33.** What is the output?

```js
function calculate(a, b, op) {
  return op(a, b);
}

console.log(calculate(3, 4, (x, y) => x + y));
```

A) 7
B) 12
C) undefined
D) Error

---

### **Q34.** What does this code demonstrate?

```js
setTimeout(() => {
  console.log("Done");
}, 1000);
```

A) Synchronous execution
B) Callback function
C) Recursion
D) Loop

---

### **Q35.** Which function returns a **new array**?

A) for
B) while
C) map()
D) push()

---

### **Q36.** What is logged?

```js
[1, 2, 3].forEach((n) => console.log(n * 2));
```

A) 1 2 3
B) 2 4 6
C) [2,4,6]
D) Error

---

## 🔄 PART 10: Loops on Arrays (Q37–Q40)

### **Q37.** What is the output?

```js
let arr = [2, 4, 6];
let sum = 0;

for (let i = 0; i < arr.length; i++) {
  sum += arr[i];
}
console.log(sum);
```

A) 6
B) 10
C) 12
D) Error

---

### **Q38.** What will be printed?

```js
let arr = [1, 2, 3];
for (let i = arr.length - 1; i >= 0; i--) {
  console.log(arr[i]);
}
```

A) 1 2 3
B) 3 2 1
C) undefined
D) Error

---

### **Q39.** What does `break` do in a loop?

A) Skips current iteration
B) Stops the loop completely
C) Restarts loop
D) Does nothing

---

### **Q40.** Best choice to **apply logic on every element** of array?

A) map()
B) if
C) switch
D) break

---

---
