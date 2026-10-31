"""
Problem: Sort a Tuple

Description:
Return a new tuple containing the elements in ascending order.

Example:
Input:  (40, 10, 30, 20)
Output: (10, 20, 30, 40)
"""


def sort_tuple(t):
    return tuple(sorted(t))


t = (40, 10, 30, 20)
print(sort_tuple(t))
