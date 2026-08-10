# Remove duplicates from sorted array
arr = [4, 33, 50, 7, 6, 4, 66, 55, 3, 1]

# Step 1: Sort the array using Bubble Sort
for j in range(len(arr) - 1):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

print("Sorted array:", arr)

# Step 2: Remove duplicates
unique = 0

for i in range(1, len(arr)):
    if arr[i] != arr[unique]:
        unique += 1
        arr[unique] = arr[i]

# Step 3: Print only the unique portion
print("After removing duplicates:", arr[:unique + 1])