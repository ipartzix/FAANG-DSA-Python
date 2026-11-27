# leetcode : https://leetcode.com/problems/sqrtx/description/

# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
