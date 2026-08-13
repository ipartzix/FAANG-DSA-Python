# Find the union of two arrays

def union(arr1, arr2):
    result = []

    for num in arr1 + arr2:
        if num not in result:
            result.append(num)

    return result


arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

print(union(arr1, arr2))