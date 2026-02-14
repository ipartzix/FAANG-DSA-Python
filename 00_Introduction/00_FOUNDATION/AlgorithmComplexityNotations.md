# Algorithm Complexity Notations

Understanding algorithm efficiency is crucial. These notations describe **time/space growth** as input size increases.

---

## 1. Big-O (O) – Upper Bound
- Describes **worst-case scenario**.
- Tells the maximum time/space an algorithm can take.
- **Notation:** `f(n) = O(g(n))`  
- **Example:** A loop running `n^2 + 3n + 2` → `O(n^2)`

---

## 2. Big-Ω (Ω) – Lower Bound
- Describes **best-case scenario**.
- Tells the minimum time/space an algorithm will take.
- **Notation:** `f(n) = Ω(g(n))`  
- **Example:** Scanning an array of size `n` → `Ω(n)`

---

## 3. Big-Θ (Θ) – Tight Bound
- Describes **exact asymptotic growth**.
- Algorithm grows at the same rate in both best and worst case.
- **Notation:** `f(n) = Θ(g(n))`  
- **Example:** `f(n) = 3n^2 + 5n + 10` → `Θ(n^2)`

---

## Quick Reference

| Notation | Bound Type   | Meaning                  |
|----------|------------|--------------------------|
| O(g(n))  | Upper      | Worst-case              |
| Ω(g(n))  | Lower      | Best-case               |
| Θ(g(n))  | Tight      | Exact asymptotic growth |
