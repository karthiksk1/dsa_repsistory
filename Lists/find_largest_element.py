"""
Problem: Find Largest Element

Description:
Find the largest element in the array.

Example:
Input:  [3, 8, 2, 10, 5]
Output: 10
"""


class Solution:
    def largest(self, arr):
        large = arr[0]
        for num in arr:
            if num > large:
                large = num
        return large


arr = [3, 8, 2, 10, 5]
print(Solution().largest(arr))
