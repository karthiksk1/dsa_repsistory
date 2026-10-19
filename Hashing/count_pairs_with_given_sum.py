"""
Problem: Count Pairs With a Given Sum

Description:
Count index pairs (i, j), where i < j and arr[i] + arr[j]
equals the target.

Example:
Input:  arr = [1, 5, 7, -1, 5], target = 6
Output: 3
"""


def count_pairs(arr, target):
    freq = {}
    count = 0
    for num in arr:
        complement = target - num
        count += freq.get(complement, 0)
        freq[num] = freq.get(num, 0) + 1
    return count


arr = [1, 5, 7, -1, 5]
target = 6
print(count_pairs(arr, target))
