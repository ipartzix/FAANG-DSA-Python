# Delete element from given position
def delete_at_position(arr, n, pos):
    # arr: list
    # n: current number of elements
    # pos: index to delete (0-based)

    if pos < 0 or pos >= n:
        return "Invalid position"

    # shift elements to the left
    i = pos
    while i < n - 1:
        arr[i] = arr[i + 1]
        i += 1

    # optional: clear last duplicate
    arr[n - 1] = None

    return arr


# Example
arr = [10, 20, 30, 40, 50]
n = 5
print(delete_at_position(arr, n, 2))
# Output: [10, 20, 40, 50, None]