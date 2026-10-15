"""
Problem: Left Rotate by One

Description:
Rotate the array to the left by one position.
The first element moves to the end.

Example:
Input:  [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
"""


class Solution:
    def left_rotate(self, arr):
        if not arr:
            return arr
        first = arr.pop(0)
        arr.append(first)
        return arr


arr = [1, 2, 3, 4, 5]
print(Solution().left_rotate(arr))
