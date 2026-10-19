class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i]
            preMap[n] = i
        return []


# alternet


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(n):
            reminder = target - nums[i]
            if reminder in hash_map:
                return [hash_map[reminder], i]
            hash_map[nums[i]] = i
