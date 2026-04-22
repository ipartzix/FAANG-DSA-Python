# Find first and last occurrence of an element

arr = [2, 55, 67, 9, 74, 3, 89, 9, 55]
x = int(input("Enter the element:- "))

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == x:
        if first == -1:
            first = i
        last = i

if first == -1:
    print("Element not found")
else:
    print("First occurrence at index:", first)
    print("Last occurrence at index:", last)