#Print unique elements
arr = [2, 55, 67, 9, 74, 3, 89, 9, 55]

n = len(arr)

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        print(arr[i], end=" ")