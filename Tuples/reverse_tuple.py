"""
Problem: Reverse a Tuple

Description:
Reverse the elements of a tuple without modifying
the original tuple.

Example:
Input:  (10, 20, 30, 40)
Output: (40, 30, 20, 10)
"""


def reverse_tuple(t):
    return t[::-1]


t = (10, 20, 30, 40)
print(reverse_tuple(t))
