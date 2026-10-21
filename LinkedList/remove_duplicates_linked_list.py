"""
Problem: Remove Duplicates from a Sorted Linked List

Description:
Remove duplicate nodes from a sorted linked list,
keeping one occurrence of each value.

Example:
Input:  [1, 1, 2, 3, 3]
Output: [1, 2, 3]
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


def remove_duplicates(head):
    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


head = create_list([1, 1, 2, 3, 3])
head = remove_duplicates(head)
print("Updated list:", list_values(head))
