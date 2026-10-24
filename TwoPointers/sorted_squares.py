"""
Problem: Squares of a Sorted Array

Description:
Given a sorted array that may contain negative numbers,
return a sorted array of their squares.

Example:
Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
"""


def sorted_squares(arr):
    left = 0
    right = len(arr) - 1
    result = [0] * len(arr)
    position = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[position] = arr[left] ** 2
            left += 1
        else:
            result[position] = arr[right] ** 2
            right -= 1
        position -= 1
    return result


arr = [-4, -1, 0, 3, 10]
print(sorted_squares(arr))
