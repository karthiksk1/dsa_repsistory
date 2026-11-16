"""
Problem: Relative Sort Array (LeetCode 1122)

Description:
Sort arr1 so that elements appearing in arr2 follow the
order of arr2. Place remaining elements in ascending order.

Example:
Input:  arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
        arr2 = [2, 1, 4, 3, 9, 6]
Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
"""


def relative_sort_array(arr1, arr2):
    order = {num: i for i, num in enumerate(arr2)}
    return sorted(
        arr1,
        key=lambda x: (0, order[x]) if x in order else (1, x)
    )


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relative_sort_array(arr1, arr2))
