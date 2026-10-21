"""
Problem: Find the Nth Node from the End

Description:
Return the nth node's value from the end, where n starts
at 1. Return -1 if n is invalid.

Example:
Input:  [10, 20, 30, 40], n = 2
Output: 30
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list(arr):
    head = None
    tail = None
    for value in arr:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


def list_values(head):
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result


def nth_node_from_end(head, n):
    if n <= 0:
        return -1
    slow = head
    fast = head
    for _ in range(n):
        if fast is None:
            return -1
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow.data


head = create_list([10, 20, 30, 40])
print("Nth node from end:", nth_node_from_end(head, 2))
