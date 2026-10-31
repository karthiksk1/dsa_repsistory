"""
Problem: Find the Sum of Tuple Elements

Description:
Calculate the sum of all numeric elements in a tuple.

Example:
Input:  (10, 20, 30, 40)
Output: 100
"""


def tuple_sum(t):
    total = 0
    for num in t:
        total += num
    return total


t = (10, 20, 30, 40)
print(tuple_sum(t))
