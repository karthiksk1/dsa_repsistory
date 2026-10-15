"""
Problem: Search for Element

Description:
Search for a target element in the array using linear search.
Return its index if found, -1 otherwise.

Example:
Input:  arr = [10, 20, 30, 40], target = 30
Output: 2
"""


class Solution:
    def search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1


arr = [10, 20, 30, 40]
target = 30
print(Solution().search(arr, target))
