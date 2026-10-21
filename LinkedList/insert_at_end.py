"""
Problem: Insert at the End

Description:
Append a new node to the end of the linked list.

Example:
Input:  [10, 20], value = 30
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


def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head


head = create_list([10, 20])
head = insert_at_end(head, 30)
print("Updated list:", list_values(head))
