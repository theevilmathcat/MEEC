# Linear Transformations

> Before vomting number crunching, let's understand what this is actually about.

A **linear transformation** `T` is a function that takes vectors from a space **V** and maps them to another space **W**, respecting two rules:

- **Additivity:** `T(u + v) = T(u) + T(v)`
- **Homogeneity:** `T(c · v) = c · T(v)`

---

## Key Definitions

| Term | Meaning |
|------|---------|
| **Map / mapear** | Convert / translate |
| **Function** | A black-box that takes one or more inputs and produces outputs based on an algorithm |
| **Space V → Space W** | Take a list of numbers with one dimensionality and transform it into another list with a different dimensionality |

**Practical example — dimensionality reduction (PCA):**

```
Input V:   athlete_data    = [max_deadlift_kg, max_squats_kg, max_bench_kg]
Output W:  summary_score   = [strength_score, weight_score]
```

We take a multi-dimensional space and compress it into 2D so we can plot it in a scatter diagram.

---

## 1. What is a Vector?

A vector is an **ordered list of numbers** — a 1D array. Think of it as a single row or column of data.

```python
# (a) One observation (one athlete) with multiple features
athlete_data = [140, 160, 100]   # [deadlift, squat, bench] in kg

# (b) One feature across multiple observations
athlete_weights = [60, 80, 90, 110]   # weight of 4 athletes in kg
```

> ⚠️ **Order matters.** `[140, 160, 100]` and `[160, 140, 100]` are different vectors.

---

## 2. Vector Operations

### a) Vector Addition

Add element-by-element. Both vectors must be the same size.

```
athlete_1 = [140, 160, 100]
athlete_2 = [120,  80, 100]
sum       = [260, 240, 200]
```

When a transformation **respects vector addition**, the order doesn't matter:

```
T(athlete_1 + athlete_2) = T(athlete_1) + T(athlete_2)
```

→ Sum first, then transform = Transform first, then sum. Same result either way.

---

### b) Scalar Multiplication

A **scalar** is a plain number (not a list). Multiplying by a scalar stretches or shrinks a vector.

```
x = 2
athlete_weights         = [ 60,  80,  90, 110]
2 × athlete_weights     = [120, 160, 180, 220]
```

When a transformation **respects scalar multiplication**:

```
T(x · athlete_weights) = x · T(athlete_weights)
T(2 · [60, 80, 90, 110]) = 2 · T([60, 80, 90, 110])
```

→ Scale first, then transform = Transform first, then scale. Same result either way.

---

## 3. What Makes a Transformation Linear?

Let's use `T([x, y]) = [2x, y]` — doubles the first element, leaves the second unchanged.

```
u = [1, 2]
v = [3, 5]
```

### a) Check additivity: `T(u + v) = T(u) + T(v)`?

**Path A — sum first, then transform:**
```
u + v      = [1+3, 2+5] = [4, 7]
T([4, 7])  = [2×4, 7]   = [8, 7]
```

**Path B — transform first, then sum:**
```
T([1, 2]) = [2, 2]
T([3, 5]) = [6, 5]
[2, 2] + [6, 5] = [8, 7] ✓
```

### b) Check homogeneity: `T(x · u) = x · T(u)`?

```
u = [1, 2],  x = 3
```

**Path A — scale first, then transform:**
```
3 · [1, 2] = [3, 6]  →  T([3, 6]) = [6, 6]
```

**Path B — transform first, then scale:**
```
T([1, 2]) = [2, 2]  →  3 · [2, 2] = [6, 6] ✓
```

Both rules hold → **`T([x, y]) = [2x, y]` is a linear transformation.**

---

## 4. Notes & Shortcuts

### 4.1 The Zero Vector Test

Any linear transformation must map the zero vector to the zero vector:

```
T([0, 0]) = [0, 0]
```

- `T(0) ≠ 0` → **definitely not linear** (quick rejection test)
- `T(0) = 0` → proves nothing on its own; you still need to verify both main rules

Think of it as a **shortcut to rule things out**, not to rule them in.

---

### 4.2 Every Linear Transformation is a Matrix

`T([x, y]) = [2x, y]` is equivalent to this matrix multiplication:

```
[2  0] · [x]  =  [2x]
[0  1]   [y]     [ y]
```

> **The matrix IS the transformation.** Each column describes what happens to each dimension.

When someone hands you a matrix, they're handing you a linear transformation.

- Input has 2 elements, output has 2 elements → **2×2 matrix**
- Input has 3 elements, output has 2 elements → **2×3 matrix**
