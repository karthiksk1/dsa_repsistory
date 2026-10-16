"""
Problem: Check Palindrome

Description:
Check whether a string reads the same forward and backward.

Example:
Input:  "madam"
Output: True
"""


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = "madam"
print("Is palindrome:", is_palindrome(s))
