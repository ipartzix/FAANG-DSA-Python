import time

def print_numbers(n):
    start = time.time()
    
    for i in range(1, n + 1):
        print(i)
    
    end = time.time()
    print("Execution Time: - Time_complexity.py:10", end - start)

# Example call
print_numbers(100)