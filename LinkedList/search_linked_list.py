"""
Problem: Search for an Element

Description:
Return the zero-based position of a target.
Return -1 if the target is absent.

Example:
Input:  [10, 20, 30], target = 20
Output: 1
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


def search_element(head, target):
    current = head
    index = 0
    while current is not None:
        if current.data == target:
            return index
        current = current.next
        index += 1
    return -1


head = create_list([10, 20, 30])
print("Position:", search_element(head, 20))
