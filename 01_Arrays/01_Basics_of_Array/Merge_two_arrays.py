#   Merge two arrays simple
def merge_arrays(arr1, arr2):
    result = []

    for i in arr1:
        result.append(i)

    for i in arr2:
        result.append(i)

    return result


# Example
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(merge_arrays(arr1, arr2))   # [1, 2, 3, 4, 5, 6]