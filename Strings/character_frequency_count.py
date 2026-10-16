"""
Problem: Character Frequency Count

Description:
Count the occurrences of each character in a string.

Example:
Input:  "aabbc"
Output: {'a': 2, 'b': 2, 'c': 1}
"""


def character_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


s = "aabbc"
print("Frequency:", character_frequency(s))
