"""
Problem: Bubble Sort

Description:
Sort an array in ascending order by repeatedly swapping
adjacent elements if they are in the wrong order.

Example:
Input:  [5, 2, 8, 1, 3]
Output: [1, 2, 3, 5, 8]
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [5, 2, 8, 1, 3]
print(bubble_sort(arr))
