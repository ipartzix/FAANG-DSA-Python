# Print unique elements
def print_unique(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count == 1:
            print(arr[i], end=" ")


# Example
arr = [1, 2, 2, 3, 4, 4, 5]
print_unique(arr)   # Output: 1 3 5