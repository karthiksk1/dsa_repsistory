"""
Problem: Remove a Specific Element

Description:
Remove all occurrences of a target value in place and return
the number of remaining elements.

Example:
Input:  arr = [3, 2, 2, 3], target = 3
Output: Count: 2, Remaining portion: [2, 2]
"""


def remove_element(arr, target):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != target:
            arr[slow] = arr[fast]
            slow += 1
    return slow


arr = [3, 2, 2, 3]
count = remove_element(arr, 3)
print("Count:", count)
print("Remaining portion:", arr[:count])
