"""
Problem: Rotate Array by K Positions

Description:
Rotate an array to the right by k positions.

Example:
Input:  arr = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
"""


def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return []
    k = k % n
    if k == 0:
        return arr.copy()
    return arr[-k:] + arr[:-k]


arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))
