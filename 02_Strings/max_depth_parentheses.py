# leetcode : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

# 1614. Maximum Nesting Depth of the Parentheses


class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        dept = 0

        for i in s:
            if i == "(":
                count += 1
                dept = max(dept, count)

            elif i == ")":
                count -= 1

        return dept
