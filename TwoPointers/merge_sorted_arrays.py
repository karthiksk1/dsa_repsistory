"""
Problem: Merge Two Sorted Arrays

Description:
Merge two sorted arrays into one sorted array.

Example:
Input:  [1, 3, 5], [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
"""


def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
