# 3. Copy only even elements into new array
arr = [2, 55, 67, 9, 74, 3, 89, 9, 55]

even_arr = []

for num in arr:
    if num % 2 == 0:
        even_arr.append(num)

print("Even elements:", even_arr)