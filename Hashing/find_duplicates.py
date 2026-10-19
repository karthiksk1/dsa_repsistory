"""
Problem: Find Duplicate Elements

Description:
Return each element that appears more than once, only once
in the order it first becomes a duplicate.

Example:
Input:  [1, 2, 3, 2, 4, 1]
Output: [2, 1]
"""


def find_duplicates(arr):
    seen = set()
    duplicates = set()
    result = []
    for num in arr:
        if num in seen and num not in duplicates:
            result.append(num)
            duplicates.add(num)
        else:
            seen.add(num)
    return result


arr = [1, 2, 3, 2, 4, 1]
print(find_duplicates(arr))
