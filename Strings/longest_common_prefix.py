"""
Problem: Longest Common Prefix

Description:
Find the longest prefix shared by every string in a list.

Example:
Input:  ["flower", "flow", "flight"]
Output: "fl"
"""


def longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


words = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(words))
