# better solution using hash map

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        h_map = {}
        result = []

        for num in nums:
            if num in h_map:
                result.append(num)
            else:
                h_map[num] = 1

        return result

# In-place marking (optimal)

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] = -nums[idx]

        return result
