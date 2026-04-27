# Find difference between max and min
arr = list(map(int, input("Enter elements Find difference between max and min: ").split()))
# 1 2 4 56 7 78

def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

def find_min(arr):
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element
# Call functions
max_element = find_max(arr)
min_element = find_min(arr)

print(f"difference between max and min is : {max_element - min_element}")