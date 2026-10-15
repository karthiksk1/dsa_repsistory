"""
Problem: Remove Duplicates

Description:
Remove duplicate elements from the array and return
only the distinct values in their original order.

Example:
Input:  [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]
"""


class Solution:
    def remove_duplicate(self, arr):
        result = []
        for num in arr:
            if num not in result:
                result.append(num)
        return result


arr = [1, 2, 2, 3, 1, 4]
print(Solution().remove_duplicate(arr))
