nums = [9,6,4,2,3,5,7,0,1]

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(0 , n+1):
            if i not in nums:
                return i

 # opotimized solution 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum
