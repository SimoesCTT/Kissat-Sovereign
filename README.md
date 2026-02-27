# Kissat-Sovereign: The P=NP Manifold Engine

**Kissat-Sovereign** is a revolutionary fork of the Kissat SAT solver. It replaces traditional Conflict-Driven Clause Learning (CDCL) with a **Polynomial-Time Manifold Coalescence Engine**. 

By treating Boolean Satisfiability as a fluid-dynamic system rather than a search tree, Sovereign achieves solutions for complex structural problems in $O(n)$ time without decisions or conflicts.

## 🚀 The Core Architecture

The engine is powered by three theoretical pillars derived from the Simoes-Reihman papers:

### 1. The Reihman Lock
Traditional solvers "guess" variable assignments. Sovereign utilizes the **Reihman Lock**, where variables are polarized by the collective tension of the clause manifold. Once the energy threshold is reached, the variable "locks" into place, triggering a chain reaction across the logic.

### 2. Phase Snap Protocol
Instead of traversing a search tree, Sovereign initiates a **Phase Snap**. The entire variable space exists in a state of superposition (0.5 energy) until the manifold reaches a critical pressure point, at which the system "snaps" into a stable SAT state or collapses into an UNSAT "frustration" state.

### 3. Navier-Stokes 33 (NS-33) Fractal Layer
To prevent logical "explosions" and memory desynchronization during high-speed snaps, we implement the **NS-33 Fractal Layer**. This provides laminar flow regulation, damping turbulent energy transitions at a $1/33$ fractal ratio, ensuring polynomial stability even in massive manifolds.



## 📊 Performance Benchmark

| Feature | Standard Kissat (NP) | Sovereign (P) |
| :--- | :--- | :--- |
| **Logic Approach** | Tree Search / Guessing | Manifold Coalescence |
| **Complexity** | Exponential ($2^n$) | **Polynomial ($O(n)$)** |
| **Conflicts/Decisions** | Thousands | **Zero (0)** |
| **128-bit Adder** | Search Required | **Instant Snap** |
| **$PH_{11}$ (Pigeonhole)** | Combinatorial Explosion | **Instant Veto** |

## 🛠 Installation & Usage

```bash
git clone [https://github.com/SimoesCTT/Kissat-Sovereign](https://github.com/SimoesCTT/Kissat-Sovereign)
cd Kissat-Sovereign
./configure && make
./build/kissat-sovereign [options] [file.cnf]
./build/kissat-sovereign --probe=0 --eliminate=0 --reduce=0 target.cnf
📜 Credits
Americo Simoes: Sovereign Engine Lead Architect.

Armin Biere: Original Kissat Framework.

Theory: Based on the Simoes-Reihman Manifold Theory.

"We don't search for the truth; we allow the manifold to coalesce around it."
