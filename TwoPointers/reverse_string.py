"""
Problem: Reverse a String Using Two Pointers

Description:
Reverse a string using two pointers and return the reversed string.

Example:
Input:  "hello"
Output: "olleh"
"""


def reverse_string(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


s = "hello"
print(reverse_string(s))
