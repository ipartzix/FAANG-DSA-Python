# 3Sum
nums = [-1, 0, 1, 2, -1, -4]

# Brute force solution
def threeSum(nums):
    n = len(nums)
    my_set = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    my_set.add(triplet)

    return list(my_set)


print(threeSum(nums))

# time complexity = O(n^3)