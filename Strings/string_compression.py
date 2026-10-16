"""
Problem: String Compression

Description:
Replace consecutive repeated characters with the character
followed by its count.

Example:
Input:  "aaabbc"
Output: "a3b2c1"
"""


def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)


s = "aaabbc"
print("Compressed string:", compress_string(s))
