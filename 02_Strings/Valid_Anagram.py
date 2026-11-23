# leetcode : https://leetcode.com/problems/valid-anagram/description/

# 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        map = {}
        for i in s:
            map[i] = map.get(i, 0) + 1

        for ch in t:
            if ch not in map:
                return False
            else:
                if map[ch] == 0:
                    return False
                else:
                    map[ch] -= 1
        return True
