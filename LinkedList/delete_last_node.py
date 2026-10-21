"""
Problem: Delete the Last Node

Description:
Remove the last node from the linked list.

Example:
Input:  [10, 20, 30]
Output: [10, 20]
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


def delete_last_node(head):
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return head


head = create_list([10, 20, 30])
head = delete_last_node(head)
print("Updated list:", list_values(head))
