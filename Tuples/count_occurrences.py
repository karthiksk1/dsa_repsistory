"""
Problem: Count Occurrences of an Element

Description:
Count how many times a given target appears in a tuple
without using count().

Example:
Input:  t = (10, 20, 10, 30, 10), target = 10
Output: 3
"""


def count_occurrences(t, target):
    count = 0
    for num in t:
        if num == target:
            count += 1
    return count


t = (10, 20, 10, 30, 10)
print(count_occurrences(t, 10))
