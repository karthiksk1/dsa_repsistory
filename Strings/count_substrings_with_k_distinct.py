"""
Problem: Count Substrings With Exactly K Distinct Characters

Description:
Count non-empty contiguous substrings that contain exactly
k distinct characters.

Example:
Input:  s = "pqpqs", k = 2
Output: 7
"""


def count_at_most_k(s, k):
    if k < 0:
        return 0
    freq = {}
    left = 0
    count = 0
    for right in range(len(s)):
        ch = s[right]
        freq[ch] = freq.get(ch, 0) + 1
        while len(freq) > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                del freq[left_ch]
            left += 1
        count += right - left + 1
    return count


def count_exactly_k(s, k):
    return count_at_most_k(s, k) - count_at_most_k(s, k - 1)


s = "pqpqs"
k = 2
print("Substrings with exactly k distinct chars:", count_exactly_k(s, k))
