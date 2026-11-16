"""
Problem: Insertion Sort

Description:
Take each element and insert it into its correct position
in the already sorted portion.

Example:
Input:  [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
