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

print("Binary Search (O(log n)) - Time_complexity.py:31")
import time

def binary_search(arr, target):
    start = time.time()
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            end = time.time()
            print("Element found at index: - Time_complexity.py:45", mid)
            print("Execution Time: - Time_complexity.py:46", end - start)
            return
        
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    end = time.time()
    print("Element not found - Time_complexity.py:55")
    print("Execution Time: - Time_complexity.py:56", end - start)

# Example
arr = [1,2,3,4,5,6,7,8,9,10]
binary_search(arr, 7)
