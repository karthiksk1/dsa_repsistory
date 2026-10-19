"""
Problem: Longest Subarray With Sum Zero

Description:
Return the maximum length of a contiguous subarray
whose sum is zero.

Example:
Input:  [15, -2, 2, -8, 1, 7, 10]
Output: 5
"""


def longest_zero_sum_subarray(arr):
    first_index = {0: -1}
    prefix_sum = 0
    max_length = 0
    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum in first_index:
            length = i - first_index[prefix_sum]
            max_length = max(max_length, length)
        else:
            first_index[prefix_sum] = i
    return max_length


arr = [15, -2, 2, -8, 1, 7, 10]
print(longest_zero_sum_subarray(arr))
