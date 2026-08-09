# Find maximum element
arr = [11,23,55,76,45,3,4,56,9]

max_ele = arr[0]
for i in arr:
    if max_ele < i:
        max_ele =i

print("Maximum element is:- ",max_ele)