"""
Problem: Detect a Cycle in a Linked List

Description:
Given the head of a linked list, determine whether the list
contains a cycle using slow and fast pointers.

Example:
List: 1 -> 2 -> 3 -> 4, node 4 points back to node 2
Output: True
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
first.next = second
second.next = third
third.next = fourth
fourth.next = second  # Creates a cycle
print(has_cycle(first))
