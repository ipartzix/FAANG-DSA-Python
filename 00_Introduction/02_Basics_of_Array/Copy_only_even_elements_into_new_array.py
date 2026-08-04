# Copy only even elements into a new array

arr = [1, 2, 3, 4, 5, 6, 7, 8]

even_arr = []

for i in arr:
    if i % 2 == 0:
        even_arr.append(i)

print("Original Array:", arr)
print("Even Elements Array:", even_arr)