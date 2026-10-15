"""
Problem: Reverse an Array

Description:
Reverse the elements of the array in place.

Example:
Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""


class Solution:
    def reverse(self, arr):
        arr.reverse()
        return arr


arr = [1, 2, 3, 4, 5]
print(Solution().reverse(arr))
