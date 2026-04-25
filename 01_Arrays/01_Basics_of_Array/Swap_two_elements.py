# Swap two elements in an Array
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Example
arr = [10, 20, 30, 40]
swap(arr, 1, 2) # index based
print(arr)   # Output: [10, 30, 20, 40]