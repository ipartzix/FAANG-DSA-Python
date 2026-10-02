# check if string palindrom or mot using recursion / loop

# num = 12321
# original = num
# reverse = 0

# while num != 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print('palindrom ')
# else:
#     print('not palindrom ')

st = "ANBCDDCBNA"
left = 0
right = len(st) - 1


def palindrome(st, left, right):
    if left >= right:
        return True

    if st[left] != st[right]:
        return False

    return palindrome(st, left + 1, right - 1)


print(palindrome(st, left, right))
