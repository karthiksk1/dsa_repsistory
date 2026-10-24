"""
Problem: Two Sum in a Sorted Array

Description:
Find two numbers in a sorted array whose sum equals the target.
Return their zero-based indices, or [-1, -1] if no pair exists.

Example:
Input:  arr = [1, 2, 4, 6, 8], target = 10
Output: [1, 4]
"""


def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


arr = [1, 2, 4, 6, 8]
target = 10
print(two_sum_sorted(arr, target))
