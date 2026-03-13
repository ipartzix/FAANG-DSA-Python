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