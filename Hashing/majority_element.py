"""
Problem: Majority Element

Description:
Find an element appearing more than n // 2 times.
Return -1 if no such element exists.

Example:
Input:  [2, 2, 1, 2, 3, 2, 2]
Output: 2
"""


def majority_element(arr):
    freq = {}
    n = len(arr)
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num
    return -1


arr = [2, 2, 1, 2, 3, 2, 2]
print(majority_element(arr))
