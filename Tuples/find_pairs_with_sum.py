"""
Problem: Find Pairs with a Given Sum

Description:
Find all unique value pairs whose sum equals the target.
Do not repeat pairs.

Example:
Input:  t = (1, 2, 3, 4, 5, 6), target = 7
Output: [(1, 6), (2, 5), (3, 4)]
"""


def find_pairs(t, target):
    nums = sorted(set(t))
    left = 0
    right = len(nums) - 1
    result = []
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            result.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return result


t = (1, 2, 3, 4, 5, 6)
target = 7
print(find_pairs(t, target))
