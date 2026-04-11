# Find maximum element
numbers = [3, 5, 1, 9, 2, 8]

# Initialize the first element as the maximum
max_element = numbers[0]

# Iterate through the list to find the maximum
for num in numbers:
    if num > max_element:
        max_element = num  # Update the maximum if a larger number is found

print("Maximum element:", max_element)