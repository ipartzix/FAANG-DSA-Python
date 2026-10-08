# arr = [5, 7, 8, 4, 1, 6, 9, 2]


# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left_arr = arr[:mid]
#     right_arr = arr[mid:]

#     left = merge_sort(left_arr)
#     right = merge_sort(right_arr)

#     return mergeArr(left, right)


# def mergeArr(left, right):

#     result = []

#     i, j = 0, 0

#     n, m = len(left), len(right)

#     while i < n and j < m:

#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1

#         else:
#             result.append(right[j])
#             j += 1

#     while i < n:
#         result.append(left[i])
#         i += 1

#     while j < m:
#         result.append(right[j])
#         j += 1

#     return result


# print(merge_sort(arr))


arr = [5, 7, 8, 4, 1, 6, 9, 2]


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return mergeArr(left, right)


def mergeArr(left, right):

    result = []

    i, j = 0, 0

    n, m = len(left), len(right)

    while i < n and j < m:

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result


print(merge_sort(arr))
