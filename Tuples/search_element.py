"""
Problem: Search for an Element in a Tuple

Description:
Search for a target element and return its index.
Return -1 if it does not exist.

Example:
Input:  t = (10, 20, 30, 40), target = 30
Output: 2
"""


def search_element(t, target):
    for i in range(len(t)):
        if t[i] == target:
            return i
    return -1


t = (10, 20, 30, 40)
print(search_element(t, 30))
