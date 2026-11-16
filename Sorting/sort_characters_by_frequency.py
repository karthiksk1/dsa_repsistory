"""
Problem: Sort Characters by Frequency (LeetCode 451)

Description:
Sort characters in a string by decreasing frequency.

Example:
Input:  "tree"
Output: "eert"
"""

from collections import Counter


def frequency_sort(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for char, count in sorted_chars:
        result += char * count
    return result


s = "tree"
print(frequency_sort(s))
