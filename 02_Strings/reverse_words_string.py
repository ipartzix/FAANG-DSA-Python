# leetcode https://leetcode.com/problems/reverse-words-in-a-string/description/
# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return " ".join(s)
