"""
Problem: Partition an Array into Evens and Odds

Description:
Rearrange an array so that all even numbers appear before
odd numbers. Order within each group does not matter.

Example:
Input:  [3, 1, 2, 4]
Output: [4, 2, 1, 3]  (one possible output)
"""


def partition_even_odd(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1
        while left < right and arr[right] % 2 != 0:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


arr = [3, 1, 2, 4]
print(partition_even_odd(arr))
