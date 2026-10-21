"""
Problem: Insert at a Given Position

Description:
Insert a node at a zero-based position.
Raise ValueError if the position is invalid.

Example:
Input:  [10, 30], value = 20, position = 1
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


def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node


def insert_at_position(head, value, position):
    if position < 0:
        raise ValueError("Position cannot be negative")
    if position == 0:
        return insert_at_beginning(head, value)
    current = head
    for _ in range(position - 1):
        if current is None:
            raise ValueError("Position out of range")
        current = current.next
    if current is None:
        raise ValueError("Position out of range")
    new_node = Node(value)
    new_node.next = current.next
    current.next = new_node
    return head


head = create_list([10, 30])
head = insert_at_position(head, 20, 1)
print("Updated list:", list_values(head))
