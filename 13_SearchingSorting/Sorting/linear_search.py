nums = [1,3,56,8,4,2,6,356,3,6,84]

def linearSearch(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    return -1

print(linearSearch(nums, 84))