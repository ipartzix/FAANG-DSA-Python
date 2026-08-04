# Find minimum element
numbers = [3, 5, 1, 9, 2, 8]

# Initialize the first element as the minimum
min_element = numbers[0]

# Iterate through the list to find the minimum
for num in numbers:
    if num < min_element:
        min_element = num  # Update the minimum if a smaller number is found

print("Minimum element:", min_element)