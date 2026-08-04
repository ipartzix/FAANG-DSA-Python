# Reverse array (without using built-in functions)
# using 2 pointer method
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # swap elements
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


# Example
arr = [10, 20, 30, 40, 50]
print(reverse_array(arr))