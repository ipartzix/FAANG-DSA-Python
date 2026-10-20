#  Maximum Subarray Sum
# brout force

nums = [-2 , 1 ,-3 ,4 ,-1,2,1,-5 ,4]
def maxSubArray(nums):
    maximum = float("-inf")
    n= len(nums)
    for i in range(0 ,n): 
         total = 0
         for j in range(i,n):
            total = total+ nums[j]
            maximum = max(maximum , total)
    return maximum

print(maxSubArray(nums))


class Solution:
    # Kadane Algorithm
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maximum =  float("- inf")
        total = 0

        for i in range(0 , n):
            total = total+ nums[i]
            maximum = max(maximum, total)
            if total< 0:
                total  = 0
        return maximum