# Find second largest element (without sorting)
def second_largest(arr):
    if len(arr) < 2:
        return "Not enough elements"

    first = float('-inf')   # largest
    second = float('-inf')  # second largest

    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x

    if second == float('-inf'):
        return "No second largest"

    return second


# Example
arr = [5, 10, 7, 13]
print(second_largest(arr))  # Output: 10