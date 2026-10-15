"""
Problem: Merge Two Lists

Description:
Merge two lists into one by concatenating them.

Example:
Input:  arr1 = [1, 2, 3]
        arr2 = [4, 5]
Output: [1, 2, 3, 4, 5]
"""


class Solution:
    def merge_list(self, arr1, arr2):
        return arr1 + arr2


arr1 = [1, 2, 3]
arr2 = [4, 5]
print(Solution().merge_list(arr1, arr2))
