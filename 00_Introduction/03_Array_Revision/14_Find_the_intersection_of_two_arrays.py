# Find the intersection of two arrays
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

intersection = []

for x in arr1:
    if x in arr2:
        intersection.append(x)

print( "print interseption",intersection)