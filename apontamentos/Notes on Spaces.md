# Notes on Spaces

A running collection of my notes on mathematical spaces.

---

## What is a Space?

A space is a set of things, plus some rules about how those things relate to each other. That's the whole idea.

## Breaking it down

**The set** = the "stuff" in the space.

- Numbers, points, functions, vectors, whatever.

**The rules** = extra structure you add on top.

- How far apart are two things? → distance rule (metric)
- What does "near" mean? → openness rule (topology)
- How long is a thing? → length rule (norm)
- What's the angle between two things? → angle rule (inner product)

## Analogy

Think of a **chessboard**.

- The **set** = all 64 squares.
- Add the rule "a knight moves in an L" → now you have a space with knight-move structure.
- Add "a rook moves in straight lines" → different structure on the same set.

Same set, different rules → different spaces.

## How Many Spaces Are There?

There's no fixed number — "space" is a general term for a set with some added structure. Mathematicians define as many kinds as are useful, and new ones get invented as needed. Below are the most common ones, roughly from least to most structure.

---

## Topological Spaces

- A **topological space** is a set with a collection of "open sets" satisfying certain axioms.
- It's the most general setting where you can talk about **continuity** and **nearness** (but not distance).
- Every other space below is a special case of a topological space.

## Metric Spaces

- A **metric space** is a set with a **distance function** (metric) `d(x, y)` satisfying:
  - `d(x, y) ≥ 0`, and `d(x, y) = 0` iff `x = y`
  - `d(x, y) = d(y, x)` (symmetry)
  - `d(x, z) ≤ d(x, y) + d(y, z)` (triangle inequality)
- **Cauchy sequences and completeness live here** — you need a metric to even define them.
- Every metric space is a topological space, but not every topological space is a metric space.

## Normed Vector Spaces

- A **normed vector space** is a vector space with a **norm** `‖x‖` that measures the "length" of a vector.
- The norm induces a metric via `d(x, y) = ‖x − y‖`, so it's automatically a metric space.
- Adds **linear structure** (you can add vectors and scale them) on top of distance.

## Banach Spaces

- A **Banach space** is a **complete normed vector space**.
- "Complete" means every Cauchy sequence converges within the space.
- Examples: ℝⁿ, ℂⁿ, and many function spaces (e.g., Lᵖ spaces).

## Inner Product Spaces

- An **inner product space** is a vector space with an **inner product** `⟨x, y⟩`, which generalizes the dot product.
- The inner product induces a norm via `‖x‖ = √⟨x, x⟩`, so it's automatically a normed space.
- Lets you talk about **angles** and **orthogonality**.

## Hilbert Spaces

- A **Hilbert space** is a **complete inner product space**.
- The nicest of the bunch — you get distance, length, angles, AND completeness.
- Examples: ℝⁿ, ℂⁿ, and L² spaces.
- Central to quantum mechanics and Fourier analysis.

---

## Quick Hierarchy
Topological space

└── Metric space

└── Normed vector space

└── Banach space (complete)

└── Inner product space

└── Hilbert space (complete)



*(Note: inner product spaces don't strictly sit "under" Banach spaces — an inner product induces a norm, so every inner product space is normed, and a complete one is both Banach and Hilbert.)*

---

<!-- 
Notes to self:
- Add examples for each space.
- Flesh out the relationship between inner product spaces and Banach spaces (Hilbert = Banach + parallelogram law).
- Maybe add: Hausdorff, compact, connected, separable as *properties* spaces can have, not separate "types."
- Add affine spaces, projective spaces, measure spaces later.
-->
