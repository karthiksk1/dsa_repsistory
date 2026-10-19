"""
Problem: Count Subarrays With Sum Divisible by K

Description:
Count contiguous subarrays whose sum is divisible by k.
Assume k is a positive integer.

Example:
Input:  arr = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
"""


def count_divisible_subarrays(arr, k):
    remainder_freq = {0: 1}
    prefix_sum = 0
    count = 0
    for num in arr:
        prefix_sum += num
        remainder = prefix_sum % k
        count += remainder_freq.get(remainder, 0)
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
    return count


arr = [4, 5, 0, -2, -3, 1]
k = 5
print(count_divisible_subarrays(arr, k))
