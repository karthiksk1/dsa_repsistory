"""
Problem: Merge Two Sorted Arrays

Description:
Merge two arrays sorted in ascending order into one sorted array.

Example:
Input:  arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
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
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))
