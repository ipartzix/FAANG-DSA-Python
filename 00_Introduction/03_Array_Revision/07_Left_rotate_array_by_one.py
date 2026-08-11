# Left rotate array by one

arr = [ 1,33,45,6,3,2,11,45,68]
print(arr)
first_element  = arr[0]
for i in range(len(arr) - 1):
    arr[i]= arr[i+1]
arr[len(arr) - 1] = first_element

print(arr)