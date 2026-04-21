# Count positive, negative, and zero
numbers = [3, 5, 1, 9, 2, 8]

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zero:", zero_count)