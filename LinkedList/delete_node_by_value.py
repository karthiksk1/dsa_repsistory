"""
Problem: Delete a Node by Value

Description:
Delete the first occurrence of a target value.
If absent, leave the list unchanged.

Example:
Input:  [10, 20, 30], target = 20
Output: [10, 30]
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


def delete_by_value(head, target):
    if head is None:
        return None
    if head.data == target:
        return head.next
    current = head
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            return head
        current = current.next
    return head


head = create_list([10, 20, 30])
head = delete_by_value(head, 20)
print("Updated list:", list_values(head))
