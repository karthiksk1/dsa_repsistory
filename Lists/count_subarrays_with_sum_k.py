"""
Problem: Count Subarrays With Sum K

Description:
Count non-empty contiguous subarrays whose sum equals k.
Works with positive, zero, and negative integers.

Example:
Input:  arr = [1, 1, 1], k = 2
Output: 2
"""


def count_subarrays_with_sum_k(arr, k):
    prefix_count = {0: 1}
    prefix_sum = 0
    count = 0
    for num in arr:
        prefix_sum += num
        count += prefix_count.get(prefix_sum - k, 0)
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    return count


arr = [1, 1, 1]
k = 2
print(count_subarrays_with_sum_k(arr, k))
