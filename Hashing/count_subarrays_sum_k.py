"""
Problem: Count Subarrays With Sum K

Description:
Count contiguous subarrays whose sum equals k.
The array may contain positive, negative, and zero values.

Example:
Input:  arr = [1, 1, 1], k = 2
Output: 2
"""


def count_subarrays_sum_k(arr, k):
    prefix_freq = {0: 1}
    prefix_sum = 0
    count = 0
    for num in arr:
        prefix_sum += num
        count += prefix_freq.get(prefix_sum - k, 0)
        prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1
    return count


arr = [1, 1, 1]
k = 2
print(count_subarrays_sum_k(arr, k))
