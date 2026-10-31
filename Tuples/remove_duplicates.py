"""
Problem: Remove Duplicates from a Tuple

Description:
Create a new tuple containing only the first occurrence of
each element, preserving the original order.

Example:
Input:  (10, 20, 10, 30, 20, 40)
Output: (10, 20, 30, 40)
"""


def remove_duplicates(t):
    result = []
    for num in t:
        if num not in result:
            result.append(num)
    return tuple(result)


t = (10, 20, 10, 30, 20, 40)
print(remove_duplicates(t))
