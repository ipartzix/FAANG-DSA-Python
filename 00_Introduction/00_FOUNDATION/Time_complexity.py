import time

def print_numbers(n):
    start = time.time()
    
    for i in range(1, n + 1):
        print(i)
    
    end = time.time()
    print("Execution Time: - Time_complexity.py:10", end - start)

# Example call
print_numbers(100)

print("Quadratic Time Complexity Example (O(n²)) - Time_complexity.py:15")
import time

def print_pairs(n):
    start = time.time()
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, j)
    
    end = time.time()
    print("Execution Time: - Time_complexity.py:26", end - start)

# Example call
print_pairs(5)