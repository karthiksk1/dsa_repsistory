"""
Problem: Count the Number of Nodes

Description:
Count the nodes in a singly linked list.

Example:
Input:  [10, 20, 30, 40]
Output: 4
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


def count_nodes(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


head = create_list([10, 20, 30, 40])
print("Total nodes:", count_nodes(head))
