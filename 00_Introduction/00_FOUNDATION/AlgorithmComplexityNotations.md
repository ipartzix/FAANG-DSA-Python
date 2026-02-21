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

```
---

# Time vs Space Trade-off

In algorithm design, improving time complexity often increases space complexity — and vice versa.

This is called a **Time–Space Trade-off**.

---

## 1. What is the Trade-off?

- Faster execution → Usually requires extra memory
- Lower memory usage → May increase computation time

Goal: Choose the optimal balance based on constraints.

---

## 2. Classic Example: Searching

### Approach 1: Linear Search
- Time Complexity: O(n)
- Space Complexity: O(1)

No extra memory, but slower.

---

### Approach 2: Hashing
- Time Complexity: O(1) average
- Space Complexity: O(n)

Faster lookups, but requires additional memory.

---

## 3. Example: Fibonacci

### Recursive (Naive)
- Time: O(2^n)
- Space: O(n) (recursion stack)

### Dynamic Programming (Memoization)
- Time: O(n)
- Space: O(n)

Faster, but uses extra memory.

---

## 4. When to Optimize What?

| Scenario | Optimize |
|----------|----------|
| Memory constrained system | Space |
| Performance-critical system | Time |
| Large input sizes | Time (usually) |
| Embedded systems | Space |

---

## 5. Interview Insight

In technical interviews:
- Always state both time and space complexity.
- If you optimize time, mention the space trade-off.
- Discuss alternatives before coding.

---

## Summary

Efficient algorithm design is not just about speed.
It is about balancing:

Time Efficiency ⚡  
Space Efficiency 💾  
Problem Constraints 🎯

## Writing Optimized DSA Code

Writing efficient DSA solutions is not just about correctness — it is about optimization.

### 1. Minimize Time Complexity
- Prefer O(log n) or O(n) over O(n²)
- Avoid unnecessary nested loops
- Use appropriate data structures (HashMap, Heap, Set, etc.)

### 2. Control Space Usage
- Avoid creating extra arrays if not required
- Use in-place modifications when possible
- Be careful with recursion (stack space)

### 3. Choose the Right Data Structure
- Fast lookup → Hashing
- Ordered data → Tree / BST
- Priority operations → Heap
- Constant access → Array
