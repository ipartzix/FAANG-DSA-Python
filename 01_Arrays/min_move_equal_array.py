class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)


# or


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = nums[0]

        # Find maximum
        for x in nums:
            if x > mx:
                mx = x

        # Calculate total moves
        moves = 0
        for x in nums:
            moves += mx - x

        return moves


# short version
# mx = max(nums)
# return sum(mx - x for x in nums)
