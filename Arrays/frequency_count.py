"""
Problem: Frequency Count

Description:
Count how many times each distinct element appears.

Example:
Input:  [1, 2, 2, 3, 1, 1]
Output: {1: 3, 2: 2, 3: 1}
"""


def frequency_count(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


arr = [1, 2, 2, 3, 1, 1]
print(frequency_count(arr))
