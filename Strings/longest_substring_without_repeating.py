"""
Problem: Longest Substring Without Repeating Characters

Description:
Find the length of the longest substring containing no
repeated characters.

Example:
Input:  "abcabcbb"
Output: 3
"""


def longest_unique_substring(s):
    seen = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        ch = s[right]
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_length = max(max_length, right - left + 1)
    return max_length


s = "abcabcbb"
print("Longest substring length:", longest_unique_substring(s))
