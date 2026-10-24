"""
Problem: Remove Duplicates from a Sorted Array

Description:
Modify a sorted array in place so that each distinct value
appears once. Return the number of unique values.

Example:
Input:  [1, 1, 2, 2, 3]
Output: Count: 3, Unique portion: [1, 2, 3]
"""


def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


arr = [1, 1, 2, 2, 3]
count = remove_duplicates(arr)
print("Count:", count)
print("Unique portion:", arr[:count])
