"""
Problem: Check Whether a String Is a Palindrome

Description:
Return True if a string reads the same forward and backward;
otherwise return False.

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
print(is_palindrome(s))
