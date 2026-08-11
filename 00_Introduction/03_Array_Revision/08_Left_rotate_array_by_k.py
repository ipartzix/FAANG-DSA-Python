# Left rotate array by k

arr = [1, 33, 45, 6, 3, 2, 11, 45, 68]
k = 3

# If k is greater than the array length
k = k % len(arr)

for _ in range(k):
    first_element = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[len(arr) - 1] = first_element

print("After left rotation:", arr)