"""
Problem: Find the Smallest Element in a Tuple

Description:
Find the minimum element without using the built-in min() function.

Example:
Input:  (12, 45, 7, 89, 23)
Output: 7
"""


def find_smallest(t):
    if not t:
        return None
    smallest = t[0]
    for num in t:
        if num < smallest:
            smallest = num
    return smallest


t = (12, 45, 7, 89, 23)
print(find_smallest(t))
