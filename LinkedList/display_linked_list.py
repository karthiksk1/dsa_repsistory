"""
Problem: Display All Elements of a Linked List

Description:
Traverse a singly linked list and display all node values.

Example:
Input:  [10, 20, 30]
Output: [10, 20, 30]
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


def display_linked_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result


head = create_list([10, 20, 30])
print("Linked list:", display_linked_list(head))
