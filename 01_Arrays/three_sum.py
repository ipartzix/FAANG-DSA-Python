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

# better solution 
def threeSum(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        my_set = set()

        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])

            if third in my_set:
                result.add(tuple(sorted([nums[i], nums[j], third])))

            my_set.add(
                nums[j]
            )  # we need to remember previously visited numbers so we can find the third number.

    return result


print(threeSum(nums))
