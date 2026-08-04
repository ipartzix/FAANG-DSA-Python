arr = [10, 20, 30, 40, 50, 60]

print("Even index values:")
for i, val in enumerate(arr):
    if i % 2 == 0:
        print(val)

print("Odd index values:")
for i, val in enumerate(arr):
    if i % 2 != 0:
        print(val)