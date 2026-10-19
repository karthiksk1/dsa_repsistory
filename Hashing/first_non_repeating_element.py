"""
Problem: First Non-Repeating Element

Description:
Return the first element that appears exactly once.
Return -1 if no such element exists.

Example:
Input:  [4, 5, 1, 2, 1, 4, 5]
Output: 2
"""


def first_non_repeating(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] == 1:
            return num
    return -1


arr = [4, 5, 1, 2, 1, 4, 5]
print(first_non_repeating(arr))
