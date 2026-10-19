"""
Problem: Frequency Count

Description:
Count how many times each number appears in a list.

Example:
Input:  [1, 2, 2, 3, 1, 1]
Output: {1: 3, 2: 2, 3: 1}
"""


def frequency_count(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq


arr = [1, 2, 2, 3, 1, 1]
print(frequency_count(arr))
