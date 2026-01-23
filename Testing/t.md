---
---

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
