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