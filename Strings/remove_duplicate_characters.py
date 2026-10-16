"""
Problem: Remove Duplicate Characters

Description:
Remove repeated characters while preserving their first occurrence.

Example:
Input:  "programming"
Output: "progamin"
"""


def remove_duplicates(s):
    result = []
    seen = set()
    for ch in s:
        if ch not in seen:
            result.append(ch)
            seen.add(ch)
    return "".join(result)


s = "programming"
print("After removing duplicates:", remove_duplicates(s))
