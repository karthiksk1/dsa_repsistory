"""
Problem: Maximum Subarray Sum

Description:
Find the maximum sum of any non-empty contiguous subarray.

Example:
Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
"""


def maximum_subarray_sum(arr):
    if not arr:
        return None
    max_sum = arr[0]
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(arr))
