"""
Problem: Leaders in an Array

Description:
An element is a leader if it is greater than or equal to every
element to its right. The last element is always a leader.
Return leaders in their original left-to-right order.

Example:
Input:  [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
"""


def leaders_in_array(arr):
    leaders = []
    max_from_right = None
    for num in reversed(arr):
        if max_from_right is None or num >= max_from_right:
            leaders.append(num)
            max_from_right = num
    leaders.reverse()
    return leaders


arr = [16, 17, 4, 3, 5, 2]
print(leaders_in_array(arr))
