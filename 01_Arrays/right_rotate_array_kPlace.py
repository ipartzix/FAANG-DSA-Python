# using python slicing
nums = [ 1,3,4,56,3,2,5,5,32,13]

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k :] + nums[: n - k]

# standared Loop