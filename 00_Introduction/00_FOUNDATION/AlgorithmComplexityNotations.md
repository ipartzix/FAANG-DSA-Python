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

---
 ## Time Efficiency (Time Complexity) ⏱️
 
 How fast does an algorithm run as input size increases.
We measure it using Big-O notation.

| Complexity   | Meaning           | Example                  |
| ------------ | ----------------- | ------------------------ |
| `O(1)`       | Constant time     | Accessing an array index |
| `O(log n)`   | Logarithmic       | Binary search            |
| `O(n)`       | Linear            | Single loop              |
| `O(n log n)` | Efficient sorting | Merge sort               |
| `O(n²)`      | Nested loops      | Bubble sort              |
| `O(2ⁿ)`      | Exponential       | Brute-force recursion    |

---
## Space Complexity
Space complexity measures the **total memory used by an algorithm** relative to input size `n`.

It includes:
- Input space
- Auxiliary (extra) space used by the algorithm

---

## 1. What is Space Complexity?

Space Complexity = Fixed Space + Variable Space

- **Fixed Space** → Constants, simple variables, program instructions  
- **Variable Space** → Depends on input size (arrays, recursion stack, dynamic allocation)

---

## 2. Auxiliary Space

Auxiliary space refers to **extra memory used apart from input data**.

Example:
- Creating a new array of size `n` → `O(n)`
- Using only a few variables → `O(1)`

---

## 3. Common Space Complexities

| Complexity | Meaning |
|------------|----------|
| O(1) | Constant space (no extra memory grows with input) |
| O(n) | Linear space (memory grows proportionally with input) |
| O(n^2) | Quadratic space |
| O(log n) | Logarithmic space (e.g., recursion stack in binary search) |

---

## 4. Examples

### Example 1: Constant Space
```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total