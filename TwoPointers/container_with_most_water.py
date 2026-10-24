"""
Problem: Container With Most Water

Description:
Given heights of vertical lines, find the maximum water area
formed by any two lines.

Example:
Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
"""


def max_water_area(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_area(heights))
