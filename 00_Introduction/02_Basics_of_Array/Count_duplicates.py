# Count duplicates

def count_duplicates(arr):
    freq = {}
    duplicates = 0

    for x in arr:
        if x in freq:
            freq[x] += 1
            duplicates += 1   # every repeat counts
        else:
            freq[x] = 1

    return duplicates


# Example
arr = [1, 2, 2, 3, 3, 3]
print(count_duplicates(arr))   # Output: 3  (2→1 extra, 3→2 extras)