# Count occurrences of a given number
arr = [1, 2, 3, 4, 5, 6, 7, 8,0,66,5,6,4,3,2, 9, 10]
x = int(input("Enter the element to count occurrences:- "))

count = 0

for i in range(len(arr)):
    if arr[i] == x:
        count += 1

print("Occurrences of", x, "=", count)