# Insert element at given position Without extra space (create new array)
def insert_at_position(arr, n, pos, value):
    # arr: list with enough capacity (one extra slot)
    # n: current number of elements (excluding extra slot)
    # pos: index where to insert (0-based)

    if pos < 0 or pos > n:
        return "Invalid position"

    # shift elements to the right
    i = n - 1
    while i >= pos:
        arr[i + 1] = arr[i]
        i -= 1

    # insert value
    arr[pos] = value

    return arr

# Example
arr = [10, 20, 30, 40, None]  # extra space
n = 4
print(insert_at_position(arr, n, 2, 25))
# Output: [10, 20, 25, 30, 40]