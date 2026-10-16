"""
Problem: Count Words in a String

Description:
Count the number of words in a sentence.

Example:
Input:  "I love Python"
Output: 3
"""


def count_words(s):
    words = s.split()
    return len(words)


s = "I love Python"
print("Word count:", count_words(s))
