"""
Problem: Find the Length of a Tuple

Description:
Find the number of elements in a tuple without using
the len() function.

Example:
Input:  (10, 20, 30, 40)
Output: 4
"""


def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count


t = (10, 20, 30, 40)
print(tuple_length(t))
