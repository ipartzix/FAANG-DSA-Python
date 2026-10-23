# Leetcode 2149: Rearrange Array Elements by Sign

nums =[5 ,10,-3,-1,-10,6]


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        positive_index = 0
        negative_index = 1
        for i in nums:
            if i > 0:
                result[positive_index] = i
                positive_index += 2
            else:
                result[negative_index] = i
                negative_index += 2
        return result

# time complexity = O(n)