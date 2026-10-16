"""
Problem: Reverse Words in a Sentence

Description:
Reverse the order of words in a sentence.

Example:
Input:  "I love Python"
Output: "Python love I"
"""


def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


s = "I love Python"
print("Reversed words:", reverse_words(s))
