"""
Problem: Check Anagrams

Description:
Check whether two strings contain the same characters
with the same frequencies.

Example:
Input:  s1 = "listen", s2 = "silent"
Output: True
"""


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True


s1 = "listen"
s2 = "silent"
print("Are anagrams:", are_anagrams(s1, s2))
