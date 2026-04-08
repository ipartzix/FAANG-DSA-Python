# print odd even index value of array
arr = [12,444,66,4,78,9,5,78]
print("Even index values :")
i = 0
for _ in arr:
    if i % 2 == 0:
        print(arr[i])
    i += 1

print("Odd index values :")
i =0
for _ in arr:
    if i % 2 != 0:
        print(arr[i])
    i += 1
