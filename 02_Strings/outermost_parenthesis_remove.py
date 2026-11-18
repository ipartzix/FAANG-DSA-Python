# leetcode : https://leetcode.com/problems/remove-outermost-parentheses/description/
# 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0
        for ch in s:
            if ch == "(":
                count += 1
                if count > 1:
                    result += ch
            else:
                count -= 1
                if count > 0:
                    result += ch
        return result