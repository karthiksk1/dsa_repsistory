"""
Problem: Find the Second Largest Distinct Element

Description:
Find the second-largest distinct element without sorting
the tuple.

Example:
Input:  (10, 40, 20, 40, 30)
Output: 30
"""


def second_largest(t):
    largest = None
    second = None
    for num in t:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second


t = (10, 40, 20, 40, 30)
print(second_largest(t))
