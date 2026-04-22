# Search for an element (linear search)
arr = [2, 55, 67, 9, 74, 3, 89]
x = int(input("Enter the element you want to find:- "))

if x in arr:
    print("Element found at index", arr.index(x))
else:
    print("Element not found")