"""
Problem: Find an Equilibrium Index

Description:
Find the first index where the sum of elements to its left
equals the sum of elements to its right.
Return -1 if no such index exists.

Example:
Input:  [1, 3, 5, 2, 2]
Output: 2  (left sum = 4, right sum = 4)
"""


def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        right_sum = total - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1


arr = [1, 3, 5, 2, 2]
print(equilibrium_index(arr))
