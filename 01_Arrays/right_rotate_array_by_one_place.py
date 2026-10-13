nums = [5,-2,6,9,23,7,8,4]

def oneRotated (nums):
    nums[:] = nums[-1:]+nums[0:-1] # nums[:] is used for inplace 
    print(nums)


oneRotated(nums)