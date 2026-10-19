"""
Problem: Longest Consecutive Sequence

Description:
Find the length of the longest sequence of consecutive
integer values. The values do not need to be adjacent in
the original array.

Example:
Input:  [100, 4, 200, 1, 3, 2]
Output: 4
"""


def longest_consecutive(arr):
    nums = set(arr)
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest


arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(arr))
