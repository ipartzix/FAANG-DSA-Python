# Find minimum element
arr =[ 12 ,43,6,89, 6,1 ,4]

min_ele =arr[0]
for i in arr:
    if min_ele > i:
        min_ele= i
print("minimum element is :-",min_ele)