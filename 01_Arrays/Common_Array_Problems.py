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