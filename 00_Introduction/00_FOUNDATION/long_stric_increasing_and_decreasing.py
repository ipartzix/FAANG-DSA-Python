# leetcode : https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2026-11-12

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 1
        increasing = 1
        decreasing = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1

            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1

            else:
                increasing = 1
                decreasing = 1

            result = max(result, increasing, decreasing)

        return result
