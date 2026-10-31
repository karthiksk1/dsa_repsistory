"""
Problem: Merge Two Tuples

Description:
Combine two tuples into a single tuple.

Example:
Input:  (1, 2, 3) and (4, 5, 6)
Output: (1, 2, 3, 4, 5, 6)
"""


def merge_tuples(t1, t2):
    return t1 + t2


t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(merge_tuples(t1, t2))
