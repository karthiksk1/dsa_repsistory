"""
Problem: Generate All Subarrays

Description:
Given a list of integers, generate all possible non-empty
contiguous subarrays.

Example:
Input:  [1, 2, 3]
Output: [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
"""


def get_subarrays(arr):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarray = []
            for k in range(i, j + 1):
                subarray.append(arr[k])
            result.append(subarray)
    return result


arr = [1, 2, 3]
result = get_subarrays(arr)
print("Input:", arr)
print("All subarrays:", result)
print("Total subarrays:", len(result))
