"""
Problem: Reverse a Singly Linked List

Description:
Reverse the links between nodes without creating
a separate linked list.

Example:
Input:  [10, 20, 30]
Output: [30, 20, 10]
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


def reverse_linked_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


head = create_list([10, 20, 30])
head = reverse_linked_list(head)
print("Reversed list:", list_values(head))
