# Take array input from user and print in reverse

def num():
    arr = list(map(int, input("Enter array elements (space separated): ").split()))
    # Take space-separated input, split into elements, convert each to integer, and store as a list (array)
    return arr
#  User input → string → list of strings → integers → final array


def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap
        left += 1
        right -= 1
    return arr

arr = num()
# print(reverse_array(arr)) this line is easy to execute
reversed_arr = reverse_array(arr)
print("Reversed Array:", reversed_arr)