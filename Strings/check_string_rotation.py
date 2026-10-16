"""
Problem: Check String Rotation

Description:
Check whether one string is a rotation of another string.

Example:
Input:  s1 = "abcd", s2 = "cdab"
Output: True
"""


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)


s1 = "abcd"
s2 = "cdab"
print("Is rotation:", is_rotation(s1, s2))
