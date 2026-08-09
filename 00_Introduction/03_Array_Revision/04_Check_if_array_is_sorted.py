# Check if array is sorted
arr = [12, 5, 4, 5, 6, 7, 8, 9, 97]

is_sorted = True

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")