Excellent choice 🚀 — tensor products are the **language of multi-particle quantum systems**.
If you want to understand **2 qubits**, **entanglement**, or **multi-particle wavefunctions**, you need tensor products.

---

# 🔹 Tensor Products in NumPy (Quantum Focus)

In math notation:

$$
|\psi⟩ \otimes |\phi⟩ = |ψφ⟩
$$

This is called the **tensor product** (or **Kronecker product**).

---

## 1. **Why Tensor Products?**

- Single qubit = 2D vector

$$
|0⟩ = \begin{bmatrix}1 \\ 0\end{bmatrix}, \quad |1⟩ = \begin{bmatrix}0 \\ 1\end{bmatrix}
$$

- Two qubits = 4D vector (2×2)
- Three qubits = 8D vector (2×2×2)

So for `n` qubits, dimension = $2^n$.
That’s why quantum computers scale exponentially!

---

## 2. **Tensor Product in NumPy**

Use `np.kron` (Kronecker product).

```python
import numpy as np

# Define basis states
zero = np.array([1, 0])  # |0>
one  = np.array([0, 1])  # |1>

# Two qubit state |0> ⊗ |1>
state = np.kron(zero, one)

print(state)
```

✅ Output:

```
[0 1 0 0]
```

👉 This represents **|01⟩**.

---

## 3. **Superposition Tensor Products**

Example:

$$
|\psi⟩ = \frac{|0⟩ + |1⟩}{\sqrt{2}}
$$

Now let’s make **two superposition qubits**:

```python
psi = (1/np.sqrt(2)) * np.array([1, 1])   # (|0>+|1>)/√2
phi = (1/np.sqrt(2)) * np.array([1, -1])  # (|0>-|1>)/√2

combined = np.kron(psi, phi)

print(combined)
```

✅ Output:

```
[ 0.5 -0.5  0.5 -0.5]
```

👉 This is a **4D state vector** = |ψφ⟩.

---

## 4. **Entangled States (Bell States)**

Entanglement is **not separable** — you can’t write it as `|ψ⟩⊗|φ⟩`.

Example:

$$
|\Phi^+⟩ = \frac{1}{\sqrt{2}}(|00⟩ + |11⟩)
$$

```python
bell = (1/np.sqrt(2)) * (np.kron(zero, zero) + np.kron(one, one))
print(bell)
```

✅ Output:

```
[0.70710678 0.         0.         0.70710678]
```

👉 This is an **entangled state**.

- If you measure qubit A = 0, qubit B must also be 0.
- If A = 1, B must also be 1.

This is the foundation of **quantum teleportation, cryptography, quantum supremacy**.

---

## 5. **Tensor Products of Operators (Multi-Qubit Gates)**

Operators on multi-qubits are also built using tensor products.

Example: Apply Hadamard (H) on the first qubit, Identity (I) on second:

$$
U = H \otimes I
$$

```python
H = (1/np.sqrt(2)) * np.array([[1, 1],
                                [1, -1]])
I = np.eye(2)

U = np.kron(H, I)  # H ⊗ I
print(U.shape)
```

✅ Output:

```
(4, 4)
```

👉 Now `U` can act on 2-qubit states.

---

## 6. **Applying Operators to States**

Let’s apply $H \otimes I$ on |00⟩:

```python
state = np.kron(zero, zero)   # |00>
result = np.dot(U, state)

print(result)
```

✅ Output:

```
[0.70710678 0.         0.70710678 0.        ]
```

👉 This means the result is:

$$
\frac{|00⟩ + |10⟩}{\sqrt{2}}
$$

Interpretation:

- First qubit is in superposition.
- Second qubit still fixed in |0⟩.

---

# 🌌 Real-World Physics Usage

- **Two particles quantum state** = tensor product of wavefunctions.
- **Entanglement** (EPR paradox, Bell’s theorem).
- **Quantum gates on multi-qubit systems**.
- **Spin systems in quantum many-body physics**.

---
