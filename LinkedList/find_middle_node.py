"""
Problem: Find the Middle Node

Description:
Return the middle node's value. For an even-length list,
return the second middle node.

Example:
Input:  [10, 20, 30, 40, 50]
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


def find_middle_node(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    if slow is None:
        return None
    return slow.data


head = create_list([10, 20, 30, 40, 50])
print("Middle node:", find_middle_node(head))
