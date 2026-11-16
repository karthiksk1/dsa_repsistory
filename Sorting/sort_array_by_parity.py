"""
Problem: Sort Array by Parity

Description:
Move all even numbers before odd numbers using two pointers.

Example:
Input:  [3, 1, 2, 4]
Output: [4, 2, 1, 3]  (one valid ordering)
"""


def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums


nums = [3, 1, 2, 4]
print(sort_array_by_parity(nums))
