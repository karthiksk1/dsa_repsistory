"""
Problem: Check Subsequence

Description:
Check whether all characters of the first string appear in the
same order in the second string. They need not be adjacent.

Example:
Input:  s = "ace", t = "abcde"
Output: True
"""


def is_subsequence(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


s = "ace"
t = "abcde"
print("Is subsequence:", is_subsequence(s, t))
