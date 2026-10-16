"""
Problem: Minimum Window Substring

Description:
Find the shortest substring of s that contains all characters
in t, including their required frequencies.

Example:
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""


def minimum_window(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    required = {}
    for ch in t:
        required[ch] = required.get(ch, 0) + 1
    window = {}
    have = 0
    need = len(required)
    left = 0
    min_length = float("inf")
    start = 0
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in required and window[ch] == required[ch]:
            have += 1
        while have == need:
            length = right - left + 1
            if length < min_length:
                min_length = length
                start = left
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in required and window[left_ch] < required[left_ch]:
                have -= 1
            left += 1
    if min_length == float("inf"):
        return ""
    return s[start:start + min_length]


s = "ADOBECODEBANC"
t = "ABC"
print("Minimum window:", minimum_window(s, t))
