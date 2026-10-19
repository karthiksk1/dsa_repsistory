"""
Problem: Most Frequent Element

Description:
Return the element that occurs most frequently.
If multiple elements tie, return the one that appears
first in the original array.

Example:
Input:  [1, 3, 2, 3, 2, 3, 2]
Output: 3
"""


def most_frequent_element(arr):
    if not arr:
        return -1
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    result = arr[0]
    max_count = freq[result]
    for num in arr:
        if freq[num] > max_count:
            result = num
            max_count = freq[num]
    return result


arr = [1, 3, 2, 3, 2, 3, 2]
print(most_frequent_element(arr))
