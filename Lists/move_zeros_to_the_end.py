"""
Problem: Move Zeros to the End

Description:
Move all zeros in the array to the end while maintaining
the relative order of non-zero elements.

Example:
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
"""


class Solution:
    def move_zero(self, arr):
        non_zero = []
        zero = []
        for num in arr:
            if num == 0:
                zero.append(num)
            else:
                non_zero.append(num)
        return non_zero + zero


arr = [0, 1, 0, 3, 12]
print(Solution().move_zero(arr))
