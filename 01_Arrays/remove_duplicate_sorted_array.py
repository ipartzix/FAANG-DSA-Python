nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        frequencyMap = {}
        for i in range(0, n):
            frequencyMap[nums[i]] = 0
        j = 0
        for k in frequencyMap:
            nums[j] = k
            j += 1
        return j


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1

        return j