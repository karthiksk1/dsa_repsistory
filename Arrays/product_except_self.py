"""
Problem: Product of Array Except Self

Description:
For each position, calculate the product of all other elements.
Do not use division.

Example:
Input:  [1, 2, 3, 4]
Output: [24, 12, 8, 6]
"""


def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result


arr = [1, 2, 3, 4]
print(product_except_self(arr))
