from math import log10
n = 1234

class Solution:
    def countDigits(self, n: int) -> int:
        return int(log10(n) + 1)
