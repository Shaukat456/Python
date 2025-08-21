Perfect 🌌⚛️ — since you’re a physics undergrad and interested in quantum, we’ll learn **NumPy Linear Algebra** but keep examples tied to **quantum mechanics / quantum computing**.

---

# 🔹 **Linear Algebra with NumPy (Physics Focus)**

In physics (especially quantum), we work with **vectors** (states) and **matrices** (operators). NumPy’s `numpy.linalg` gives us tools for that.

---

## 1. **Vector Dot Product**

In quantum mechanics:

- A **state** is represented by a vector (ket |ψ⟩).
- The **inner product** ⟨φ|ψ⟩ is like a dot product.

```python
import numpy as np

psi = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # |ψ⟩ = (1/√2)[1,1]
phi = np.array([1/np.sqrt(2), -1/np.sqrt(2)]) # |φ⟩ = (1/√2)[1,-1]

inner_product = np.dot(np.conjugate(phi), psi)
print(inner_product)
```

✅ Output:

```
0.0
```

👉 These states are **orthogonal** (like spin-up and spin-down in quantum mechanics).

---

## 2. **Matrix-Vector Multiplication (Operator acting on state)**

In quantum mechanics:

- Operators = matrices.
- States = vectors.
- Applying operator = matrix multiplication.

Example: **Pauli-X gate (quantum NOT)**

```python
X = np.array([[0, 1],
              [1, 0]])  # Pauli-X operator
psi = np.array([1, 0])  # |0⟩ state

result = np.dot(X, psi)  # Apply operator
print(result)
```

✅ Output:

```
[0 1]
```

👉 The |0⟩ state became |1⟩.
(That’s exactly how a quantum NOT gate works!)

---

## 3. **Matrix-Matrix Multiplication**

Two operators applied sequentially = multiply matrices.

Example: Pauli-X twice = Identity.

```python
I = np.dot(X, X)
print(I)
```

✅ Output:

```
[[1 0]
 [0 1]]
```

👉 Applying X twice brings state back → like flipping twice.

---

## 4. **Eigenvalues & Eigenvectors**

In quantum mechanics:

- Measurement outcomes = **eigenvalues**.
- Possible states after measurement = **eigenvectors**.

Example: Measuring **Pauli-Z** operator.

```python
Z = np.array([[1, 0],
              [0, -1]])

eigvals, eigvecs = np.linalg.eig(Z)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
```

✅ Output:

```
Eigenvalues: [ 1. -1.]
Eigenvectors:
[[1. 0.]
 [0. 1.]]
```

👉 Meaning:

- Measuring spin-z gives **+1 (spin-up)** or **-1 (spin-down)**.
- Corresponding eigenvectors are |0⟩ and |1⟩.

---

## 5. **Determinant (Quantum Check)**

A unitary operator (quantum gate) has determinant of **magnitude 1**.

```python
det = np.linalg.det(X)
print(det)
```

✅ Output:

```
-1.0
```

👉 Pauli-X is unitary (|det| = 1).

---

## 6. **Inverse (Reversibility of Quantum Gates)**

Quantum gates must be **reversible**, so their inverse exists.

```python
X_inv = np.linalg.inv(X)
print(X_inv)
```

✅ Output:

```
[[0. 1.]
 [1. 0.]]
```

👉 The inverse of X is itself (makes sense: flipping twice = undo).

---

## 🔬 Real-World Quantum Example

Let’s simulate **superposition with Hadamard Gate (H):**

```python
H = (1/np.sqrt(2)) * np.array([[1, 1],
                                [1, -1]])

zero = np.array([1, 0])  # |0⟩ state
superposition = np.dot(H, zero)

print(superposition)
```

✅ Output:

```
[0.70710678 0.70710678]
```

👉 This is (1/√2)(|0⟩ + |1⟩) → the **quantum superposition** state.

---

# ⚡ Why This Matters

- **Dot product** = probability amplitudes.
- **Matrix multiplication** = evolution of quantum states.
- **Eigenvalues** = measurement outcomes.
- **Determinants & inverses** = unitary & reversible operations.

This is exactly the math that underlies **quantum mechanics** and **quantum computing algorithms**.
