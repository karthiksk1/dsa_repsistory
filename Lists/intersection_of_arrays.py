"""
Problem: Intersection of Two Arrays

Description:
Return the distinct elements present in both arrays.
Preserve their first-appearance order in arr1.

Example:
Input:  arr1 = [1, 2, 2, 3, 4]
        arr2 = [2, 3, 5]
Output: [2, 3]
"""


def intersection(arr1, arr2):
    second = set(arr2)
    seen = set()
    result = []
    for num in arr1:
        if num in second and num not in seen:
            result.append(num)
            seen.add(num)
    return result


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5]
print(intersection(arr1, arr2))
