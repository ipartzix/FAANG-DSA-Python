# Count frequency of each element (without dict first, then with dict)
print("without dict ")
arr = [2, 55, 67, 9, 74, 3, 89, 9, 55]

visited = [False] * len(arr)

for i in range(len(arr)):
    if visited[i]:
        continue

    count = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
            visited[j] = True

    print(arr[i], "->", count)

print("with dict ")
arr = [2, 55, 67, 9, 74, 3, 89, 9, 55]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key, value in freq.items():
    print(key, "->", value)