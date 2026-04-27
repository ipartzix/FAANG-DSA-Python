# Check if array is sorted
def is_sorted_ASC(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True



# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Decision
if is_sorted_ASC(arr):
    print("Array is sorted in ascending order")
elif is_sorted_DESC(arr):
    print("Array is sorted in descending order")
else:
    print("Array is not sorted")