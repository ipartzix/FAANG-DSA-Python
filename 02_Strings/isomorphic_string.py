# leetcode : https://leetcode.com/problems/isomorphic-strings/
# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_stot = {}
        mapping_ttos = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check s -> t mapping
            if char_s in mapping_stot:
                if mapping_stot[char_s] != char_t:
                    return False
            else:
                mapping_stot[char_s] = char_t

            # Check t -> s mapping
            if char_t in mapping_ttos:
                if mapping_ttos[char_t] != char_s:
                    return False
            else:
                mapping_ttos[char_t] = char_s

        return True
