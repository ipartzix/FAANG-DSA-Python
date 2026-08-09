# Find second-largest element
arr = [11,23,55,76,45,3,4,56,9]

first_largest =arr[0]
sec_largest = arr[0]

for i in arr:
    if i > first_largest:
        sec_largest= first_largest
        first_largest = i

    elif i > sec_largest and i != first_largest :
        sec_largest = i


print("First largest number is :-", first_largest)
print("Second Largest number is :-", sec_largest)