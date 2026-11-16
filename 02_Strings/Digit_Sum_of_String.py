# Leetcode : 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/

# optimal 

class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            result = []

            for i in range(0, len(s), k):
                group_sum = sum(map(int, s[i : i + k]))
                result.append(str(group_sum))

            s = "".join(result)

        return s
