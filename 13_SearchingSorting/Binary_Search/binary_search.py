# leetcode 704:- https://leetcode.com/problems/binary-search
# time complexity O(log n)
# Iterative way

nums = [-1,0,3,5,9,19]
target = 9

def binarySearch( nums , target):
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+ high)// 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return - 1


# Recursion
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def binary_search(low, high):
            if low > high:
                return -1

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return binary_search(mid + 1, high)

            else:
                return binary_search(low, mid - 1)

        return binary_search(0, len(nums) - 1)
