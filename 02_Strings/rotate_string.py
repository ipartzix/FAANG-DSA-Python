# Leetcode  https://leetcode.com/problems/rotate-string/
# 796. Rotate String

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double_string = s + s
        if goal in double_string:
            return True
        else:
            return False
