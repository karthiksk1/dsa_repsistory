"""
Problem: Union of Two Arrays

Description:
Return all distinct elements from both arrays.
Preserve first-appearance order, processing arr1 before arr2.

Example:
Input:  arr1 = [1, 2, 2, 3]
        arr2 = [3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
"""


def union_arrays(arr1, arr2):
    result = []
    seen = set()
    for num in arr1 + arr2:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


arr1 = [1, 2, 2, 3]
arr2 = [3, 4, 4, 5]
print(union_arrays(arr1, arr2))
