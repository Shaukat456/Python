Perfect 🚀 Let’s level up from **NumPy → SciPy** while keeping everything **quantum physics focused**.

---

# 🔬 What is SciPy?

- SciPy = **Scientific Python** → it builds on **NumPy**.
- Provides **advanced math tools**:

  - Linear algebra (more than NumPy)
  - Optimization
  - Integration & Differential Equations
  - Fourier transforms
  - Statistics & Probability

In **Quantum Physics**, SciPy is extremely useful for:

- Solving **Schrödinger’s Equation** (time evolution of wavefunctions)
- Finding **eigenvalues/eigenvectors of Hamiltonians**
- Doing **Fourier transforms** (momentum vs position space)
- Optimization in **quantum experiments**

---

# 1️⃣ **Linear Algebra with SciPy**

We already know `np.linalg` → but SciPy gives **faster + more features** in `scipy.linalg`.

### Example: Quantum Harmonic Oscillator Hamiltonian

Hamiltonian (matrix form for truncated basis):

$$
H = \hbar \omega \left(a^\dagger a + \frac{1}{2}\right)
$$

Let’s diagonalize it:

```python
import numpy as np
from scipy.linalg import eigh

# Parameters
hbar = 1
omega = 1

# Truncated basis (5x5 matrix)
N = 5
H = np.diag([hbar * omega * (n + 0.5) for n in range(N)])

# Find eigenvalues/eigenvectors
eigvals, eigvecs = eigh(H)

print("Energy levels:", eigvals)
```

🔹 **Real-world use**: This gives the discrete energy levels of a quantum harmonic oscillator (0.5ħω, 1.5ħω, …).
In real quantum mechanics courses → SciPy can directly calculate them.

---

# 2️⃣ **Differential Equations: Time Evolution**

SciPy has `solve_ivp` (initial value problem solver).

👉 In quantum physics, the **time-dependent Schrödinger equation** is:

$$
i \hbar \frac{d}{dt} \psi(t) = H \psi(t)
$$

We can solve it numerically for small systems.

### Example: Two-level system (Qubit in magnetic field)

Hamiltonian:

$$
H = \frac{\hbar \Omega}{2} \sigma_x
$$

```python
import numpy as np
from scipy.integrate import solve_ivp

# Pauli-X matrix
sigma_x = np.array([[0, 1],
                    [1, 0]])

hbar = 1
Omega = 1  # Rabi frequency

# Hamiltonian
H = (hbar * Omega / 2) * sigma_x

# Schrödinger equation: dψ/dt = -i/H * ψ
def schrodinger(t, psi):
    return -1j * H @ psi

# Initial state |0>
psi0 = np.array([1, 0], dtype=complex)

# Solve from t=0 to 10
sol = solve_ivp(schrodinger, [0, 10], psi0, t_eval=np.linspace(0,10,100))

# Probability of being in |1>
probs = np.abs(sol.y[1])**2
```

🔹 **Real-world use**: This simulates **Rabi oscillations** → exactly what happens when a qubit is driven by a microwave pulse in a quantum computer.

---

# 3️⃣ **Fourier Transforms**

In quantum mechanics, going from **position space** ↔ **momentum space** is done using Fourier transforms.

SciPy has `scipy.fft`.

### Example: Gaussian wave packet in momentum space

```python
from scipy.fft import fft, fftfreq

# Gaussian wave packet in position space
x = np.linspace(-10, 10, 1024)
psi_x = np.exp(-x**2)

# Fourier transform → momentum space
psi_p = fft(psi_x)

# Frequencies (momentum axis)
p = fftfreq(len(x), d=(x[1]-x[0]))
```

🔹 **Real-world use**: This shows how a localized Gaussian in space becomes **spread in momentum space** → fundamental **Heisenberg uncertainty principle**.

---

# 🔑 Summary of SciPy Quantum Usage

- `scipy.linalg` → diagonalizing Hamiltonians (energy levels)
- `scipy.integrate.solve_ivp` → solving Schrödinger’s equation
- `scipy.fft` → switching between position & momentum representations

---

⚡ So, SciPy is basically the **numerical laboratory** for quantum mechanics.
It lets you test, simulate, and visualize quantum systems the way you’d do in a real experiment.

---
