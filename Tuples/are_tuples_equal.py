"""
Problem: Check Whether Two Tuples Are Equal

Description:
Check whether two tuples contain the same elements
in the same order.

Example:
Input:  (10, 20, 30) and (10, 20, 30)
Output: True
"""


def are_tuples_equal(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True


t1 = (10, 20, 30)
t2 = (10, 20, 30)
print(are_tuples_equal(t1, t2))
