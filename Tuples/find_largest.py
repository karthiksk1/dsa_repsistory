"""
Problem: Find the Largest Element in a Tuple

Description:
Find the maximum element without using the built-in max() function.

Example:
Input:  (12, 45, 7, 89, 23)
Output: 89
"""


def find_largest(t):
    if not t:
        return None
    largest = t[0]
    for num in t:
        if num > largest:
            largest = num
    return largest


t = (12, 45, 7, 89, 23)
print(find_largest(t))
