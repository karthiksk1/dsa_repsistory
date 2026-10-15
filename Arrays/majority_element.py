"""
Problem: Majority Element

Description:
Find the element that appears more than n // 2 times.
Return -1 if no such element exists.

Example:
Input:  [2, 2, 1, 2, 3, 2, 2]
Output: 2
"""


def majority_element(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in freq:
        if freq[num] > len(arr) // 2:
            return num
    return -1


arr = [2, 2, 1, 2, 3, 2, 2]
print(majority_element(arr))
