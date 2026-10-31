"""
Problem: Find Common Elements in Two Tuples

Description:
Find the unique common elements between two tuples,
preserving the order in which they appear in the first tuple.

Example:
Input:  (10, 20, 30, 40) and (20, 40, 50)
Output: (20, 40)
"""


def common_elements(t1, t2):
    result = []
    for num in t1:
        if num in t2 and num not in result:
            result.append(num)
    return tuple(result)


t1 = (10, 20, 30, 40)
t2 = (20, 40, 50)
print(common_elements(t1, t2))
