"""
Problem: Check if Array is Sorted

Description:
Return True if the array is sorted in non-decreasing order,
False otherwise.

Example:
Input:  [1, 2, 2, 4, 5]
Output: True
"""


class Solution:
    def isSorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


arr = [1, 2, 2, 4, 5]
result = Solution().isSorted(arr)
print("Is array sorted:", result)
