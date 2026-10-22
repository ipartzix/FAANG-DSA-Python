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


