# Find the element that appears once

def find_single(arr):
    result = 0

    for num in arr:
        result ^= num

    return result


arr = [2, 3, 5, 4, 5, 3, 4]
print(find_single(arr))