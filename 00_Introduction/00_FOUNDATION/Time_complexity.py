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


print("Merge Sort (O(n log n)) - Time_complexity.py:63")
import time

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# Example
arr = [38, 27, 43, 3, 9, 82, 10]

start = time.time()
merge_sort(arr, 0, len(arr) - 1)
end = time.time()

print("Sorted array: - Time_complexity.py:117", arr)
print("Execution Time: - Time_complexity.py:118", end - start)

print("Fibonacci Using Recursion (O(2ⁿ)) - Time_complexity.py:120")
import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example
n = 10

start = time.time()
result = fibonacci(n)
end = time.time()

print("Fibonacci of - Time_complexity.py:136", n, "is:", result)
print("Execution Time: - Time_complexity.py:137", end - start)


print("Generate All Permutations (O(n!)) - Time_complexity.py:140")

import time

def permute(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]   # swap
            permute(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]   # backtrack


# Example
arr = [1, 2, 3]

start = time.time()
permute(arr, 0, len(arr) - 1)
end = time.time()

print("Execution Time: - Time_complexity.py:161", end - start)