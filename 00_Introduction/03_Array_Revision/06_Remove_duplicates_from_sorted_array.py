# Remove duplicates from sorted array
arr = [4, 33, 50, 7, 6,4, 66, 55, 3, 1]
"""
 at first we short the Array
"""
for j in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1] :
             arr[i], arr[i+1] = arr[i+1],arr[i]

print(arr)

