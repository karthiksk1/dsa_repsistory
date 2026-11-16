"""
Problem: Kth Largest Element in an Array (LeetCode 215)

Description:
Find the kth largest element without fully sorting
the array.

Example:
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
"""


def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))
