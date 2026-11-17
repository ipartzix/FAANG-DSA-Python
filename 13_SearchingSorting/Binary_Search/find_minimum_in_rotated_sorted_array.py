# leetcode : 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        mini = float("inf")
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                mini = min(mini, nums[mid])
                high = mid - 1
            else:
                mini = min(mini, nums[low])
                low = mid + 1
        return mini