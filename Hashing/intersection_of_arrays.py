"""
Problem: Intersection of Two Arrays

Description:
Return the distinct elements present in both arrays.

Example:
Input:  arr1 = [1, 2, 2, 3], arr2 = [2, 3, 4]
Output: [2, 3]
"""


def intersection(arr1, arr2):
    second = set(arr2)
    result = []
    seen = set()
    for num in arr1:
        if num in second and num not in seen:
            result.append(num)
            seen.add(num)
    return result


arr1 = [1, 2, 2, 3]
arr2 = [2, 3, 4]
print(intersection(arr1, arr2))
