"""
Problem: Height Checker (LeetCode 1051)

Description:
Count how many students are not standing in the positions
they would occupy if their heights were sorted.

Example:
Input:  [1, 1, 4, 2, 1, 3]
Output: 3
"""


def height_checker(heights):
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count


heights = [1, 1, 4, 2, 1, 3]
print(height_checker(heights))
