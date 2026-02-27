# Define size
n = 5

# Create array with default value 0
arr = [0] * n   # Only allocation, no append/insert used

# Assign values manually
arr[0] = 10
arr[1] = 20
arr[2] = 30
arr[3] = 40
arr[4] = 50

# Print using loop (DSA style traversal)
for i in range(n):
    print(arr[i])