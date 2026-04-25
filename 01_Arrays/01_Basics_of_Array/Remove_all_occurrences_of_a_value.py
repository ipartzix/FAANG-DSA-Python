# Remove all occurrences of a value
def remove_all(arr, value):
    write = 0  # position to place next valid element

    for read in range(len(arr)):
        if arr[read] != value:
            arr[write] = arr[read]
            write += 1

    # optional: clear remaining positions
    i = write
    while i < len(arr):
        arr[i] = None
        i += 1

    return arr, write  # write = new length

# Example
arr = [1, 2, 3, 2, 4, 2, 5]
result, new_len = remove_all(arr, 2)
print(result)   # [1, 3, 4, 5, None, None, None]
print(new_len)  # 4