"""
Problem: Group Anagrams

Description:
Group words that contain the same characters with the
same frequencies.

Example:
Input:  ["eat", "tea", "tan", "ate"]
Output: [["eat", "tea", "ate"], ["tan"]]
"""


def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


words = ["eat", "tea", "tan", "ate"]
print("Grouped anagrams:", group_anagrams(words))
