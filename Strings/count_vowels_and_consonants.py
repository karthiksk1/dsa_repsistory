"""
Problem: Count Vowels and Consonants

Description:
Count vowels and consonants in an English-letter string.

Example:
Input:  "hello"
Output: Vowels: 2, Consonants: 3
"""


def count_vowels_consonants(s):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


s = "hello"
vowels, consonants = count_vowels_consonants(s)
print("Vowels:", vowels)
print("Consonants:", consonants)
