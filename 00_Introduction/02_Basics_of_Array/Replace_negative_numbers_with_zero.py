# Replace all negative numbers with 0 [Implementation (In-place)]
def replace_negative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0

# Example
arr = [3, -1, 5, -7, 2]
replace_negative(arr)
print(arr)   # Output: [3, 0, 5, 0, 2]