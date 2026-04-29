# Find common elements
def common_elements_sorted(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result


# Example
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]
print(common_elements_sorted(arr1, arr2))  # [2, 2, 4]