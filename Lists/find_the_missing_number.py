"""
Problem: Find the Missing Number

Description:
Given an array of n-1 distinct integers in the range [1, n],
find the one missing number.

Example:
Input:  [1, 2, 4, 5]
Output: 3
"""


class Solution:
    def find_missing(self, arr):
        n = len(arr) + 1
        total = n * (n + 1) // 2
        return total - sum(arr)


arr = [1, 2, 4, 5]
print(Solution().find_missing(arr))
