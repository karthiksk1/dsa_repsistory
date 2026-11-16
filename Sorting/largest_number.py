"""
Problem: Largest Number (LeetCode 179)

Description:
Arrange non-negative integers to form the largest
possible number.

Example:
Input:  [3, 30, 34, 5, 9]
Output: "9534330"
"""

from functools import cmp_to_key


def largest_number(nums):
    arr = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0

    arr.sort(key=cmp_to_key(compare))
    if arr[0] == "0":
        return "0"
    return "".join(arr)


nums = [3, 30, 34, 5, 9]
print(largest_number(nums))
