# Reverse an array
#
# arr = [1, 3, 55, 66, 6, 7, 50, 33, 4]
# arr2 = []
#
# for i in range(len(arr) - 1, -1, -1):
#     arr2.append(arr[i])
#
# print(arr2)


arr = [1, 3, 55, 66, 6, 7, 50, 33, 4]

a = 0
z = len(arr) - 1
while a < z:
    arr[a], arr[z] = arr[z], arr[a]
    a += 1
    z -= 1

print(arr)