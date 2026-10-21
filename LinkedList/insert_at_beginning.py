"""
Problem: Insert at the Beginning

Description:
Insert a new node at the beginning of the linked list.

Example:
Input:  [20, 30], value = 10
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


head = create_list([20, 30])
head = insert_at_beginning(head, 10)
print("Updated list:", list_values(head))
