"""
Problem: Same Frequencies

Description:
Check whether two arrays contain exactly the same elements
with the same frequencies, regardless of order.

Example:
Input:  [1, 2, 2, 3], [2, 3, 2, 1]
Output: True
"""


def same_frequencies(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    freq = {}
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    for num in arr2:
        if num not in freq:
            return False
        freq[num] -= 1
        if freq[num] < 0:
            return False
    return True


arr1 = [1, 2, 2, 3]
arr2 = [2, 3, 2, 1]
print(same_frequencies(arr1, arr2))
