class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0

        if x < 0:
            return False

        while num > 0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num // 10

        return x == result
