# Leetcode 128: Longest Consecutive Sequence

nums = [ 1,101 ,99 ,101,3,2,88,98,100,97]

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            count = 1
            current = num

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest


print(longestConsecutive(nums))
