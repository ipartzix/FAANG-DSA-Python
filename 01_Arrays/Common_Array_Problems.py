print("Reverse Array:")
# Method 1: Built-in
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]  # [5, 4, 3, 2, 1]

# Method 2: Two pointers
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap
        left += 1
        right -= 1
    return arr

print("Rotate Array:")

# Rotate right by k positions
def rotate_array(arr, k):
    k = k % len(arr)  # Handle k > array length
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print(rotate_array(arr, 2))  # [4, 5, 1, 2, 3]

print("Find Missing Number:")
# Array should have numbers 1 to n, find missing one
def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2  # Sum formula
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1, 2, 4, 5, 6]  # 3 is missing
print(find_missing(arr, 6))  # Output: 3