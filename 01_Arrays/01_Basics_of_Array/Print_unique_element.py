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


#hash map (dictionary in Python)

# def print_unique(arr):
#     freq = {}
#
#     # Step 1: build frequency map
#     for x in arr:
#         if x in freq:
#             freq[x] += 1
#         else:
#             freq[x] = 1
#
#     # Step 2: print elements with freq = 1
#     for x in arr:
#         if freq[x] == 1:
#             print(x, end=" ")
#
#
# # Example
# arr = [1, 2, 2, 3, 4, 4, 5]
# print_unique(arr)   # Output: 1 3 5