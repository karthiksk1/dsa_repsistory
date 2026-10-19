"""
Problem: Isomorphic Strings

Description:
Check whether characters in one string can be mapped
consistently and one-to-one to characters in another string.

Example:
Input:  s = "egg", t = "add"
Output: True
"""


def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    map_st = {}
    map_ts = {}
    for ch1, ch2 in zip(s, t):
        if ch1 in map_st and map_st[ch1] != ch2:
            return False
        if ch2 in map_ts and map_ts[ch2] != ch1:
            return False
        map_st[ch1] = ch2
        map_ts[ch2] = ch1
    return True


s = "egg"
t = "add"
print(are_isomorphic(s, t))
