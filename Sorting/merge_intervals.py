"""
Problem: Merge Intervals (LeetCode 56)

Description:
Merge all overlapping intervals and return the
non-overlapping intervals.

Example:
Input:  [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
"""


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
