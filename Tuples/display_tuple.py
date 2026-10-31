"""
Problem: Create and Display a Tuple

Description:
Create a tuple of integers and display all its elements
using a loop.

Example:
Input:  (10, 20, 30, 40, 50)
Output: 10 20 30 40 50
"""


def display_tuple(t):
    for num in t:
        print(num, end=" ")
    print()


t = (10, 20, 30, 40, 50)
display_tuple(t)
