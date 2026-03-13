print("Reverse String")

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # "olleh"

# Two-pointer method
def reverse_string_manual(s):
    chars = list(s)  # Convert to list (strings are immutable)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

print(reverse_string_manual("hello"))

print("Palindrome Check")
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False


print("Anagram Check")
def is_anagram(s1, s2):
    # Anagrams have same letters, different order
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False


# Better method using Counter
from collections import Counter

def is_anagram_better(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram_better("listen", "silent"))  # True
print(is_anagram_better("hello", "world"))    # False