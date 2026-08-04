# Find average of array
arr = [1,2,4,5]
total =0
count = 0
for i in arr:

    total += i
    count += 1
avg = total / count
print(f"Sum of the array is {total}")
print(f"The average is {avg}")